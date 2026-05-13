"""Windows 安装包构建脚本。

由 build_installer.py 调用。准备 staging 目录，调用 NSIS 生成 .exe 安装包。

前置条件: NSIS 3 已安装（makensis 在 PATH 中）
"""

import os
import shutil
import subprocess
import sys
import zipfile
from pathlib import Path

PYTHON_VERSION = "3.11.9"
PYTHON_TAG = "311"


def build_windows(root_dir: Path, cache_dir: Path, dist_dir: Path, installer_dir: Path):
    """构建 Windows .exe 安装包。"""
    staging = dist_dir / "staging" / "windows"
    win_installer_dir = installer_dir / "windows"

    # 清理 staging
    if staging.exists():
        shutil.rmtree(staging)
    staging.mkdir(parents=True)

    # ── 1. 解压嵌入式 Python ──
    print("[1/6] 解压嵌入式 Python...")
    python_dir = staging / "python"
    python_zip = cache_dir / f"python-{PYTHON_VERSION}-embed-amd64.zip"
    if not python_zip.exists():
        print(f"  错误: 找不到 {python_zip}，请先运行下载步骤")
        sys.exit(1)
    with zipfile.ZipFile(python_zip, "r") as zf:
        zf.extractall(python_dir)
    print(f"  Python 已解压到: {python_dir}")

    # 修改 python311._pth 启用 site-packages
    pth_file = python_dir / f"python{PYTHON_TAG}._pth"
    pth_file.write_text(
        f"python{PYTHON_TAG}.zip\n"
        f".\n"
        f"Lib\n"
        f"Lib\\site-packages\n"
        f"import site\n",
        encoding="utf-8",
    )
    print("  已修改 _pth 启用 site-packages")

    # 创建 Lib/site-packages 目录
    (python_dir / "Lib" / "site-packages").mkdir(parents=True, exist_ok=True)

    # ── 2. 安装 pip 到嵌入式 Python ──
    print("[2/6] 安装 pip...")
    get_pip = cache_dir / "get-pip.py"
    if get_pip.exists():
        subprocess.check_call(
            [str(python_dir / "python.exe"), str(get_pip), "--no-warn-script-location"],
            cwd=str(python_dir),
        )
    else:
        print("  警告: get-pip.py 不存在，尝试用 wheel 文件中的 pip")

    # ── 3. 离线安装依赖 ──
    print("[3/6] 离线安装 Python 依赖...")
    wheels_dir = cache_dir / "wheels_windows"
    if not wheels_dir.exists():
        # 回退到通用 wheels 目录
        wheels_dir = cache_dir / "wheels"
    if not wheels_dir.exists():
        print(f"  错误: 找不到 wheel 文件目录")
        sys.exit(1)

    requirements = root_dir / "requirements.txt"
    pip_exe = str(python_dir / "python.exe")

    install_cmd = [
        pip_exe, "-m", "pip", "install",
        "--no-index",
        "--find-links", str(wheels_dir),
        "-r", str(requirements),
        "--no-warn-script-location",
    ]

    result = subprocess.run(install_cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"  pip install 失败:\n{result.stderr}")
        print("  尝试逐个安装...")
        # 解析 requirements.txt 并逐个安装
        with open(requirements, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#"):
                    subprocess.run(
                        [pip_exe, "-m", "pip", "install", "--no-index",
                         "--find-links", str(wheels_dir), line,
                         "--no-warn-script-location"],
                        capture_output=True,
                    )
    print("  依赖安装完成")

    # ── 4. 复制项目代码和模型 ──
    print("[4/6] 复制项目代码和模型...")
    app_dir = staging / "app"
    model_dir = staging / "model"

    # 项目代码
    includes = [
        "app.py", "config.yaml", "requirements.txt",
        "rag", "scripts", "knowledge", "ui", "services",
    ]
    for item in includes:
        src = root_dir / item
        dst = app_dir / item
        if src.is_dir():
            shutil.copytree(src, dst)
        elif src.exists():
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dst)

    # 复制 write_config.py 到 app/scripts/
    write_config_src = win_installer_dir / "write_config.py"
    if write_config_src.exists():
        shutil.copy2(write_config_src, app_dir / "scripts" / "write_config.py")

    # 模型
    cached_model = cache_dir / "model"
    if cached_model.exists():
        shutil.copytree(cached_model, model_dir)
    else:
        print("  警告: 未找到模型文件，安装包中将不包含 embedding 模型")

    # 修改 config.yaml 指向本地模型
    config_file = app_dir / "config.yaml"
    if config_file.exists():
        import yaml
        with open(config_file, "r", encoding="utf-8") as f:
            config = yaml.safe_load(f)
        config["embedding"]["local_path"] = str((staging / "model").resolve())
        with open(config_file, "w", encoding="utf-8") as f:
            yaml.dump(config, f, default_flow_style=False, allow_unicode=True, sort_keys=False)
        print("  config.yaml 已更新模型路径")

    # ── 5. 复制启动脚本 ──
    print("[5/6] 复制启动脚本...")
    for bat_name in ["launch.bat", "launch_ingest.bat", "stop.bat",
                     "edit_config.bat", "open_knowledge.bat"]:
        src = win_installer_dir / bat_name
        if src.exists():
            shutil.copy2(src, staging / bat_name)

    # 读取版本号
    import yaml
    with open(app_dir / "config.yaml", "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)
    version = config.get("version", "0.8.17")

    # ── 6. 调用 NSIS 构建安装包 ──
    print("[6/6] 调用 NSIS 构建安装包...")
    nsi_script = win_installer_dir / "knowledge_setup.nsi"

    # 检查 NSIS
    makensis = shutil.which("makensis")
    if not makensis:
        print("\n  错误: 未找到 makensis！")
        print("  请安装 NSIS 3: https://nsis.sourceforge.io/Download")
        print("  安装后将 NSIS 目录加入 PATH 环境变量")
        print(f"\n  staging 目录已准备好: {staging}")
        print("  你可以手动运行:")
        print(f'    makensis /DVERSION={version} /DSTAGING_DIR="{staging}" "{nsi_script}"')
        return False

    cmd = [
        makensis,
        f"/DVERSION={version}",
        f"/DSTAGING_DIR={staging}",
        str(nsi_script),
    ]
    print(f"  执行: {' '.join(cmd)}")
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"  NSIS 编译失败:\n{result.stderr}")
        return False

    output_exe = dist_dir / f"knowledge-setup-{version}-windows.exe"
    print(f"\n  安装包已生成: {output_exe}")
    if output_exe.exists():
        size_mb = output_exe.stat().st_size / (1024 * 1024)
        print(f"  大小: {size_mb:.1f} MB")
    return True

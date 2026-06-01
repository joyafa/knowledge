"""Windows 安装包构建脚本（PyInstaller 版本）。

由 build_installer.py 调用。使用 PyInstaller 编译应用为 exe，
然后调用 NSIS 生成 .exe 安装包。

前置条件: PyInstaller 已安装（pip install pyinstaller）
           NSIS 3 已安装（makensis 在 PATH 中）
"""

import shutil
import subprocess
import sys
import time
from pathlib import Path


def _rmtree_robust(path: Path, retries: int = 3, delay: float = 1.0) -> None:
    """Robust rmtree with retry on PermissionError (Windows file lock)."""
    for attempt in range(retries):
        try:
            shutil.rmtree(path)
            return
        except PermissionError:
            if attempt < retries - 1:
                print(f"  删除 {path} 失败，{delay}s 后重试 ({attempt + 1}/{retries})...")
                time.sleep(delay)
            else:
                # 最后尝试：重命名绕过
                backup = path.with_suffix(path.suffix + ".old")
                print(f"  删除失败，尝试重命名为 {backup}")
                try:
                    path.rename(backup)
                except Exception as rename_err:
                    raise PermissionError(f"无法删除或重命名 {path}: {rename_err}") from None


def build_windows(root_dir: Path, cache_dir: Path, dist_dir: Path, installer_dir: Path, skip_models: bool = False):
    """构建 Windows .exe 安装包。

    Steps:
    1. PyInstaller 编译 Python 应用为独立 exe 目录
    2. 修复数据文件位置（PyInstaller 将 datas 放在 _internal/ 中）
    3. 准备 staging 目录
    4. 调用 NSIS 生成安装包
    """
    staging = dist_dir / "staging" / "windows"
    win_installer_dir = installer_dir / "windows"
    spec_file = root_dir / "knowledge_app.spec"

    if not spec_file.exists():
        print(f"  错误: 找不到 PyInstaller spec 文件: {spec_file}")
        sys.exit(1)

    # 1. PyInstaller 编译
    print("[1/4] PyInstaller 编译应用...")
    print(f"  Spec: {spec_file}")
    # 不要使用 capture_output=True — PyInstaller 日志量巨大，管道缓冲区满会导致子进程挂死
    # 改为输出到日志文件
    pyi_log = root_dir / "build" / "pyinstaller.log"
    pyi_log.parent.mkdir(parents=True, exist_ok=True)
    with open(pyi_log, "w", encoding="utf-8") as log_f:
        result = subprocess.run(
            [sys.executable, "-m", "PyInstaller", str(spec_file), "--clean", "--noconfirm"],
            cwd=str(root_dir),
            stdout=log_f,
            stderr=subprocess.STDOUT,
            text=True,
        )
    if result.returncode != 0:
        # 读取日志末尾
        with open(pyi_log, "r", encoding="utf-8", errors="replace") as log_f:
            content = log_f.read()
            tail = content[-2000:] if len(content) > 2000 else content
        print(f"  PyInstaller 编译失败 (日志: {pyi_log}):\n{tail}")
        sys.exit(1)
    print("  PyInstaller 编译完成")

    pyinstaller_output = root_dir / "dist" / "KnowledgeAssistant"
    if not pyinstaller_output.exists():
        print(f"  错误: PyInstaller 输出目录不存在: {pyinstaller_output}")
        sys.exit(1)

    # 2. 修复数据文件位置
    print("[2/4] 修复数据文件位置...")
    internal_dir = pyinstaller_output / "_internal"
    # rag/ui/services 源码已编译进 PYZ，此处仅复制运行时必需的纯数据文件
    for item in ["app.py", "config.yaml", "logo.png"]:
        src = internal_dir / item
        dst = pyinstaller_output / item
        if src.exists() and not dst.exists():
            shutil.copy2(src, dst)
            print(f"  已复制: {item}")

    # 复制本地模型（如果有）
    if not skip_models:
        model_src = root_dir / "model"
        model_dst = pyinstaller_output / "model"
        if model_src.exists() and not model_dst.exists():
            # 只复制模型快照目录
            for model_item in model_src.iterdir():
                if model_item.is_dir() and model_item.name.startswith("models--"):
                    snapshot_dir = model_item / "snapshots"
                    if snapshot_dir.exists():
                        snapshots = sorted(snapshot_dir.iterdir(), key=lambda p: p.stat().st_mtime, reverse=True)
                        if snapshots:
                            model_name = model_item.name.replace("models--", "").replace("--", "/")
                            model_type = "text2vec-base-chinese" if "text2vec" in model_name else "bge-reranker-base"
                            target = model_dst / model_type
                            shutil.copytree(snapshots[0], target)
                            print(f"  已复制模型: {model_type}")
    else:
        print("  (跳过模型复制 — 快速调试模式)")

    # 3. 准备 staging 目录
    print("[3/4] 准备 staging 目录...")
    if staging.exists():
        _rmtree_robust(staging)
    staging.mkdir(parents=True, exist_ok=True)

    print(f"  复制: {pyinstaller_output} -> {staging}")
    shutil.copytree(pyinstaller_output, staging, dirs_exist_ok=True)

    # 读取版本号
    import yaml
    config_file = staging / "config.yaml"
    version = "0.18.18"
    if config_file.exists():
        with open(config_file, "r", encoding="utf-8") as f:
            config = yaml.safe_load(f)
        version = config.get("version", version)

    print(f"  staging 准备完成，版本: {version}")

    # 4. 调用 NSIS 构建安装包
    print("[4/4] 调用 NSIS 构建安装包...")
    nsi_script = win_installer_dir / "knowledge_setup.nsi"

    makensis = shutil.which("makensis")
    if not makensis:
        print("\n  错误: 未找到 makensis！")
        print("  请安装 NSIS 3: https://nsis.sourceforge.io/Download")
        print(f"\n  staging 目录已准备好: {staging}")
        print(f"  你可以手动运行:")
        print(f'    makensis /DVERSION={version} /DSTAGING_DIR="{staging}" /DOUTDIR="{dist_dir}" "{nsi_script}"')
        return False

    cmd = [
        makensis,
        f"/DVERSION={version}",
        f"/DSTAGING_DIR={staging}",
        f"/DOUTDIR={dist_dir}",
        str(nsi_script),
    ]
    print(f"  执行: {' '.join(cmd)}")
    nsis_log = root_dir / "build" / "nsis.log"
    nsis_log.parent.mkdir(parents=True, exist_ok=True)
    with open(nsis_log, "w", encoding="utf-8") as log_f:
        result = subprocess.run(cmd, stdout=log_f, stderr=subprocess.STDOUT, text=True)
    if result.returncode != 0:
        with open(nsis_log, "r", encoding="utf-8", errors="replace") as log_f:
            content = log_f.read()
        print(f"  NSIS 编译失败 (日志: {nsis_log}):\n{content[-2000:]}")
        return False

    output_exe = dist_dir / f"knowledge-setup-{version}-windows.exe"
    print(f"\n  安装包已生成: {output_exe}")
    if output_exe.exists():
        size_mb = output_exe.stat().st_size / (1024 * 1024)
        print(f"  大小: {size_mb:.1f} MB")
    return True

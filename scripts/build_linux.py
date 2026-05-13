"""Linux 安装包构建脚本。

由 build_installer.py 调用。准备 staging 目录，调用 fpm 生成 .deb / .rpm 安装包。

前置条件:
    - ruby + gem install fpm
    - 构建 .rpm 还需要 rpm 工具链

此脚本通常在 Linux 或 WSL 环境中运行。
"""

import os
import shutil
import subprocess
import sys
import tarfile
from pathlib import Path


def build_linux(root_dir: Path, cache_dir: Path, dist_dir: Path, installer_dir: Path):
    """构建 Linux .deb / .rpm 安装包。"""
    staging = dist_dir / "staging" / "linux"
    linux_installer_dir = installer_dir / "linux"

    # 清理 staging
    if staging.exists():
        shutil.rmtree(staging)
    staging.mkdir(parents=True)

    # ── 1. 解压 Python standalone ──
    print("[1/5] 解压 Python standalone...")
    python_tar = cache_dir / "cpython-3.11.10-x86_64-unknown-linux-gnu-install_only.tar.gz"
    if not python_tar.exists():
        print(f"  错误: 找不到 {python_tar}，请先运行下载步骤")
        sys.exit(1)

    python_dest = staging / "opt" / "knowledge-assistant" / "python"
    python_dest.mkdir(parents=True, exist_ok=True)

    with tarfile.open(python_tar, "r:gz") as tf:
        # tar 内部结构: python/install/bin/python3.11 -> ...
        # 需要找到 python 子目录并解压
        members = [m for m in tf.getmembers() if "python/install" in m.name]
        # 去掉前缀，解压到 python_dest
        for member in members:
            # 去掉 "python/install/" 前缀
            parts = member.name.split("/")
            # 找到 "install" 后的部分
            try:
                idx = parts.index("install")
                member.name = "/".join(parts[idx + 1:])
                if member.name:
                    tf.extract(member, str(python_dest))
            except ValueError:
                continue

    print(f"  Python 已解压到: {python_dest}")

    # ── 2. 离线安装依赖 ──
    print("[2/5] 离线安装 Python 依赖...")
    wheels_dir = cache_dir / "wheels_linux"
    if not wheels_dir.exists():
        wheels_dir = cache_dir / "wheels"
    if not wheels_dir.exists():
        print(f"  错误: 找不到 wheel 文件目录")
        sys.exit(1)

    python_bin = python_dest / "bin" / "python3.11"
    if not python_bin.exists():
        python_bin = python_dest / "bin" / "python3"
    if not python_bin.exists():
        print(f"  错误: 找不到 python 可执行文件 in {python_dest / 'bin'}")
        sys.exit(1)

    requirements = root_dir / "requirements.txt"

    install_cmd = [
        str(python_bin), "-m", "pip", "install",
        "--no-index",
        "--find-links", str(wheels_dir),
        "-r", str(requirements),
        "--no-warn-script-location",
    ]

    result = subprocess.run(install_cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"  pip install 失败:\n{result.stderr}")
        # 尝试逐个安装
        with open(requirements, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#"):
                    subprocess.run(
                        [str(python_bin), "-m", "pip", "install", "--no-index",
                         "--find-links", str(wheels_dir), line,
                         "--no-warn-script-location"],
                        capture_output=True,
                    )
    print("  依赖安装完成")

    # ── 3. 复制项目代码和模型 ──
    print("[3/5] 复制项目代码和模型...")
    app_dir = staging / "opt" / "knowledge-assistant" / "app"
    model_dir = staging / "opt" / "knowledge-assistant" / "model"

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

    # 模型
    cached_model = cache_dir / "model"
    if cached_model.exists():
        shutil.copytree(cached_model, model_dir)
    else:
        print("  警告: 未找到模型文件")

    # 修改 config.yaml 指向安装后的绝对路径
    config_file = app_dir / "config.yaml"
    import yaml
    if config_file.exists():
        with open(config_file, "r", encoding="utf-8") as f:
            config = yaml.safe_load(f)
        config["embedding"]["local_path"] = "/opt/knowledge-assistant/model"
        config["vectorstore"]["persist_directory"] = "/var/lib/knowledge-assistant/chroma_db"
        config["knowledge"]["docs_directory"] = "/var/lib/knowledge-assistant/knowledge"
        with open(config_file, "w", encoding="utf-8") as f:
            yaml.dump(config, f, default_flow_style=False, allow_unicode=True, sort_keys=False)
        print("  config.yaml 已更新路径")

    # 读取版本号
    with open(config_file, "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)
    version = config.get("version", "0.8.17")

    # ── 4. 创建系统文件和脚本 ──
    print("[4/5] 创建系统文件...")

    # systemd service
    service_dest = staging / "usr" / "lib" / "systemd" / "system"
    service_dest.mkdir(parents=True, exist_ok=True)
    shutil.copy2(
        linux_installer_dir / "knowledge-assistant.service",
        service_dest / "knowledge-assistant.service",
    )

    # 启动脚本 → /usr/local/bin/
    bin_dest = staging / "usr" / "local" / "bin"
    bin_dest.mkdir(parents=True, exist_ok=True)
    launch_src = linux_installer_dir / "launch.sh"
    if launch_src.exists():
        shutil.copy2(launch_src, bin_dest / "knowledge-launch")
        os.chmod(bin_dest / "knowledge-launch", 0o755)

    # 创建 knowledge-ingest 和 knowledge-stop 命令
    (bin_dest / "knowledge-ingest").write_text(
        '#!/bin/bash\n'
        'cd /opt/knowledge-assistant/app && '
        '/opt/knowledge-assistant/python/bin/python3 scripts/ingest.py "$@"\n',
        encoding="utf-8",
    )
    os.chmod(bin_dest / "knowledge-ingest", 0o755)

    (bin_dest / "knowledge-stop").write_text(
        '#!/bin/bash\n'
        'sudo systemctl stop knowledge-assistant "$@"\n',
        encoding="utf-8",
    )
    os.chmod(bin_dest / "knowledge-stop", 0o755)

    # 配置目录
    config_dest = staging / "etc" / "knowledge-assistant"
    config_dest.mkdir(parents=True, exist_ok=True)
    shutil.copy2(config_file, config_dest / "config.yaml")

    # postinst / prerm
    shutil.copy2(linux_installer_dir / "postinst.sh", staging / "postinst.sh")
    shutil.copy2(linux_installer_dir / "prerm.sh", staging / "prerm.sh")
    os.chmod(staging / "postinst.sh", 0o755)
    os.chmod(staging / "prerm.sh", 0o755)

    # ── 5. 调用 fpm 构建安装包 ──
    print("[5/5] 调用 fpm 构建安装包...")

    fpm = shutil.which("fpm")
    if not fpm:
        print("\n  错误: 未找到 fpm！")
        print("  请安装: gem install fpm")
        print(f"\n  staging 目录已准备好: {staging}")
        print("  你可以手动运行 fpm:")
        print(f'    cd {staging} && fpm -s dir -t deb -n knowledge-assistant -v {version} .')
        return False

    # 构建 .deb
    deb_cmd = [
        fpm,
        "-s", "dir",
        "-t", "deb",
        "-n", "knowledge-assistant",
        "-v", version,
        "--architecture", "amd64",
        "--description", "知识库智能问答系统 — RAG 问答终端",
        "--maintainer", "南昌市星维软件技术中心",
        "--after-install", str(staging / "postinst.sh"),
        "--before-remove", str(staging / "prerm.sh"),
        "--deb-systemd", str(service_dest / "knowledge-assistant.service"),
        "-C", str(staging),
        ".",
    ]
    print(f"  执行: {' '.join(deb_cmd)}")
    result = subprocess.run(deb_cmd, capture_output=True, text=True, cwd=str(dist_dir))
    if result.returncode != 0:
        print(f"  fpm (.deb) 失败:\n{result.stderr}")
    else:
        # fpm 输出到当前目录
        for f in Path(".").glob("knowledge-assistant_*.deb"):
            shutil.move(str(f), str(dist_dir / f.name))
            print(f"  .deb 已生成: {dist_dir / f.name}")

    # 构建 .rpm
    rpm_cmd = deb_cmd.copy()
    rpm_cmd[3] = "rpm"
    rpm_cmd.extend(["--rpm-os", "linux"])
    # 移除 --deb-systemd 参数
    systemd_idx = rpm_cmd.index("--deb-systemd")
    rpm_cmd.pop(systemd_idx)
    rpm_cmd.pop(systemd_idx)  # 移除 service 文件路径

    result = subprocess.run(rpm_cmd, capture_output=True, text=True, cwd=str(dist_dir))
    if result.returncode != 0:
        print(f"  fpm (.rpm) 失败:\n{result.stderr}")
    else:
        for f in Path(".").glob("knowledge-assistant-*.rpm"):
            shutil.move(str(f), str(dist_dir / f.name))
            print(f"  .rpm 已生成: {dist_dir / f.name}")

    # 汇总
    print("\n  Linux 安装包构建完成:")
    for f in dist_dir.glob("knowledge-assistant*"):
        size_mb = f.stat().st_size / (1024 * 1024)
        print(f"    {f.name} ({size_mb:.1f} MB)")

    return True

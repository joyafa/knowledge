"""Linux 安装包 staging 目录准备脚本。

在 Windows 上运行，准备 Linux 安装包所需的所有文件。
生成 staging 目录后，拷贝到 Linux 机器运行 fpm 即可构建 .deb/.rpm。

使用方式:
    python scripts/prepare_linux_staging.py
"""

import os
import shutil
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
DIST_DIR = ROOT_DIR / "dist"
STAGING = DIST_DIR / "staging" / "linux"


def main():
    print("知识库智能问答系统 — Linux 安装包 Staging 准备")
    print()

    # 清理
    if STAGING.exists():
        shutil.rmtree(STAGING)

    version = "0.8.17"
    config_file = ROOT_DIR / "config.yaml"
    if config_file.exists():
        import yaml
        with open(config_file, "r", encoding="utf-8") as f:
            config = yaml.safe_load(f)
        version = config.get("version", version)

    # ── 1. 复制项目代码 ──
    print("[1/3] 复制项目代码...")
    app_dir = STAGING / "opt" / "knowledge-assistant" / "app"

    includes = [
        "app.py", "config.yaml", "requirements.txt", "logo.png",
        "rag", "ui", "services", "scripts",
    ]

    excludes = {"__pycache__", ".git", ".claude", ".pytest_cache", "installer"}

    for item in includes:
        src = ROOT_DIR / item
        dst = app_dir / item
        if src.is_dir():
            shutil.copytree(src, dst, ignore=shutil.ignore_patterns(*excludes))
        elif src.exists():
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dst)

    # 复制 run_app.py 作为启动入口
    shutil.copy2(ROOT_DIR / "run_app.py", app_dir / "run_app.py")

    print(f"  项目代码已复制到: {app_dir}")

    # ── 2. 复制模型 ──
    print("[2/3] 复制本地模型...")
    model_dir = STAGING / "opt" / "knowledge-assistant" / "model"
    src_model = ROOT_DIR / "model"

    if src_model.exists():
        for model_item in src_model.iterdir():
            if model_item.is_dir() and model_item.name.startswith("models--"):
                snapshot_dir = model_item / "snapshots"
                if snapshot_dir.exists():
                    snapshots = sorted(snapshot_dir.iterdir(), key=lambda p: p.stat().st_mtime, reverse=True)
                    if snapshots:
                        if "text2vec" in model_item.name:
                            dst_name = "text2vec-base-chinese"
                        else:
                            dst_name = "bge-reranker-base"
                        shutil.copytree(snapshots[0], model_dir / dst_name)
                        print(f"  已复制: {dst_name}")
    else:
        print("  警告: 未找到本地模型目录")

    # ── 3. 更新 config.yaml 系统路径 ──
    print("[3/3] 更新 Linux 配置路径...")
    config_path = app_dir / "config.yaml"
    import yaml
    with open(config_path, "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)

    # 模型路径：保持 env var 引用，由 run_app.py 运行时自动检测本地模型
    # local_path 在 config.yaml 中已经是 "${EMBEDDING_LOCAL_PATH:-}" 格式，无需修改
    # model_root 同样保持 "${MODEL_ROOT:-model}" 格式
    config["vectorstore"]["persist_directory"] = "/var/lib/knowledge-assistant/chroma_db"
    config["knowledge"]["docs_directory"] = "/var/lib/knowledge-assistant/knowledge"

    with open(config_path, "w", encoding="utf-8") as f:
        yaml.dump(config, f, default_flow_style=False, allow_unicode=True, sort_keys=False)
    print("  config.yaml 已更新为 Linux 系统路径（模型路径保留运行时检测）")

    # 复制安装脚本模板
    installer_dir = ROOT_DIR / "scripts" / "installer" / "linux"
    if installer_dir.exists():
        for f in installer_dir.iterdir():
            dst = STAGING / f.name
            shutil.copy2(f, dst)
            if f.suffix == ".sh":
                os.chmod(dst, 0o755)
        print("  Linux 安装脚本已复制")

    # 创建 systemd 相关目录结构
    service_dest = STAGING / "usr" / "lib" / "systemd" / "system"
    service_dest.mkdir(parents=True, exist_ok=True)
    service_src = STAGING / "knowledge-assistant.service"
    if service_src.exists():
        shutil.move(str(service_src), str(service_dest / "knowledge-assistant.service"))

    bin_dest = STAGING / "usr" / "local" / "bin"
    bin_dest.mkdir(parents=True, exist_ok=True)
    launch_src = STAGING / "launch.sh"
    if launch_src.exists():
        shutil.move(str(launch_src), str(bin_dest / "knowledge-launch"))

    config_dest = STAGING / "etc" / "knowledge-assistant"
    config_dest.mkdir(parents=True, exist_ok=True)
    shutil.copy2(config_path, config_dest / "config.yaml")

    # 移动 postinst/prerm 到 staging 根目录
    for script_name in ["postinst.sh", "prerm.sh"]:
        src = STAGING / script_name
        if src.exists():
            pass  # 已在 staging 根目录

    # 统计大小
    total_size = sum(f.stat().st_size for f in STAGING.rglob("*") if f.is_file())
    size_mb = total_size / (1024 * 1024)

    print()
    print("=" * 50)
    print(f"Staging 准备完成!")
    print(f"  目录: {STAGING}")
    print(f"  版本: {version}")
    print(f"  大小: {size_mb:.1f} MB")
    print()
    print("后续步骤（在 Linux 机器上）:")
    print("  1. 将 staging/linux/ 拷贝到 Linux 机器")
    print("  2. 安装 fpm: gem install fpm")
    print("  3. 构建 .deb:")
    print(f"     cd {STAGING}")
    print(f"     fpm -s dir -t deb -n knowledge-assistant -v {version} \\")
    print("       --architecture amd64 \\")
    print("       --description '知识库智能问答系统' \\")
    print("       --maintainer '南昌市星维软件技术中心' \\")
    print("       --after-install postinst.sh \\")
    print("       --before-remove prerm.sh \\")
    print("       --deb-systemd usr/lib/systemd/system/knowledge-assistant.service \\")
    print("       -C . .")
    print("=" * 50)


if __name__ == "__main__":
    main()

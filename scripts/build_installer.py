"""离线安装包统一构建入口。

在有网络的开发机上运行，下载资源并调用平台构建脚本生成安装包。

使用方式:
    python scripts/build_installer.py --platform windows
    python scripts/build_installer.py --platform linux
    python scripts/build_installer.py --platform both
    python scripts/build_installer.py --platform windows --skip-download  # 复用已有资源

前置条件:
    Windows: NSIS 3 已安装（makensis 在 PATH 中）
    Linux: ruby + fpm 已安装

输出:
    dist/knowledge-setup-{ver}-windows.exe
    dist/knowledge-assistant_{ver}_amd64.deb
"""

import argparse
import os
import shutil
import subprocess
import sys
import urllib.request
from pathlib import Path

# 项目根目录
ROOT_DIR = Path(__file__).resolve().parent.parent
SCRIPTS_DIR = ROOT_DIR / "scripts"
INSTALLER_DIR = SCRIPTS_DIR / "installer"
DIST_DIR = ROOT_DIR / "dist"
CACHE_DIR = ROOT_DIR / "build_cache"

# Python 嵌入式版本
PYTHON_VERSION = "3.11.9"
PYTHON_TAG = "cp311"

# 下载地址
PYTHON_EMBED_URL = f"https://www.python.org/ftp/python/{PYTHON_VERSION}/python-{PYTHON_VERSION}-embed-amd64.zip"
PYTHON_STANDALONE_URL = (
    "https://github.com/indygreg/python-build-standalone/releases/download/"
    "20241016/cpython-3.11.10+20241016-x86_64-unknown-linux-gnu-install_only.tar.gz"
)
GET_PIP_URL = "https://bootstrap.pypa.io/get-pip.py"

# Embedding 模型
EMBEDDING_MODEL = "shibing624/text2vec-base-chinese"


def download_file(url: str, dest: Path, desc: str = ""):
    """下载文件（带进度提示）。"""
    if dest.exists():
        print(f"  已存在，跳过: {dest.name}")
        return
    print(f"  下载: {desc or dest.name} ...")
    dest.parent.mkdir(parents=True, exist_ok=True)
    urllib.request.urlretrieve(url, str(dest))


def download_platform_wheels(platform_name: str, wheels_dir: Path):
    """为指定平台下载 wheel 文件。"""
    wheels_dir.mkdir(parents=True, exist_ok=True)

    platform_map = {
        "windows": {
            "platform": "win_amd64",
            "extra_args": [],
        },
        "linux": {
            "platform": "manylinux2014_x86_64",
            "extra_args": [],
        },
    }

    info = platform_map[platform_name]
    print(f"  为 {platform_name} ({info['platform']}) 下载 wheel 文件...")

    cmd = [
        sys.executable, "-m", "pip", "download",
        "-r", str(ROOT_DIR / "requirements.txt"),
        "-d", str(wheels_dir),
        "--python-version", "3.11",
        "--platform", info["platform"],
        "--only-binary=:all:",
    ] + info["extra_args"]

    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        # 有些纯 Python 包不需要指定平台，回退到普通下载
        print(f"  部分包平台下载失败，使用通用模式...")
        subprocess.check_call([
            sys.executable, "-m", "pip", "download",
            "-r", str(ROOT_DIR / "requirements.txt"),
            "-d", str(wheels_dir),
        ])
        return

    # torch 需要从 CPU 索引下载
    print("  下载 torch CPU 版本...")
    torch_dir = wheels_dir / "_torch_cpu"
    torch_dir.mkdir(exist_ok=True)
    torch_result = subprocess.run([
        sys.executable, "-m", "pip", "download",
        "torch", "torchvision", "torchaudio",
        "-d", str(torch_dir),
        "--index-url", "https://download.pytorch.org/whl/cpu",
        "--python-version", "3.11",
        "--platform", info["platform"],
        "--only-binary=:all:",
    ] + info["extra_args"], capture_output=True, text=True)

    if torch_result.returncode == 0:
        # 用 CPU 版替换之前下载的 torch wheel
        for f in torch_dir.glob("torch-*.whl"):
            for old in wheels_dir.glob("torch-*.whl"):
                if "cpu" not in old.name.lower():
                    old.unlink()
                    print(f"  替换: {old.name} → {f.name}")
            shutil.copy2(f, wheels_dir / f.name)
        for f in torch_dir.glob("torchvision-*.whl"):
            shutil.copy2(f, wheels_dir / f.name)
        for f in torch_dir.glob("torchaudio-*.whl"):
            shutil.copy2(f, wheels_dir / f.name)
        shutil.rmtree(torch_dir, ignore_errors=True)
    else:
        shutil.rmtree(torch_dir, ignore_errors=True)
        print(f"  torch CPU 版下载失败，保留通用版本")


def download_embedding_model(model_dir: Path):
    """下载 embedding 模型。"""
    if model_dir.exists() and any(model_dir.iterdir()):
        print(f"  模型已存在: {model_dir}")
        return
    model_dir.mkdir(parents=True, exist_ok=True)
    os.environ.setdefault("HF_ENDPOINT", "https://hf-mirror.com")
    from sentence_transformers import SentenceTransformer
    print(f"  下载模型: {EMBEDDING_MODEL}")
    model = SentenceTransformer(EMBEDDING_MODEL)
    model.save(str(model_dir))
    print(f"  模型已保存: {model_dir}")


def copy_project_code(dest: Path):
    """复制项目代码到目标目录。"""
    if dest.exists():
        shutil.rmtree(dest)

    includes = [
        "app.py", "config.yaml", "requirements.txt",
        "rag", "scripts", "knowledge", "ui", "services",
    ]

    for item in includes:
        src = ROOT_DIR / item
        dst = dest / item
        if src.is_dir():
            shutil.copytree(src, dst)
        elif src.exists():
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dst)


def phase_download(platforms: list[str], skip_download: bool):
    """Phase 1: 下载所有资源。"""
    print("\n" + "=" * 60)
    print("Phase 1: 下载资源")
    print("=" * 60)

    CACHE_DIR.mkdir(parents=True, exist_ok=True)

    if skip_download:
        print("跳过下载（使用已有资源）")
        return

    # 下载 wheel 文件
    for plat in platforms:
        wheels_dir = CACHE_DIR / f"wheels_{plat}"
        download_platform_wheels(plat, wheels_dir)

    # 下载 embedding 模型
    download_embedding_model(CACHE_DIR / "model")

    # 下载 Python 运行时
    if "windows" in platforms:
        download_file(PYTHON_EMBED_URL, CACHE_DIR / f"python-{PYTHON_VERSION}-embed-amd64.zip",
                      f"Python {PYTHON_VERSION} Embedded (Windows)")

    if "linux" in platforms:
        download_file(PYTHON_STANDALONE_URL,
                      CACHE_DIR / "cpython-3.11.10-x86_64-unknown-linux-gnu-install_only.tar.gz",
                      "Python Standalone (Linux)")

    # 下载 get-pip.py
    download_file(GET_PIP_URL, CACHE_DIR / "get-pip.py", "get-pip.py")

    print("\n所有资源下载完成。")


def phase_build(platforms: list[str]):
    """Phase 2-3: 调用平台构建脚本。"""
    DIST_DIR.mkdir(parents=True, exist_ok=True)

    if "windows" in platforms:
        print("\n" + "=" * 60)
        print("Phase 2: 构建 Windows 安装包")
        print("=" * 60)
        from build_windows import build_windows
        build_windows(
            root_dir=ROOT_DIR,
            cache_dir=CACHE_DIR,
            dist_dir=DIST_DIR,
            installer_dir=INSTALLER_DIR,
        )

    if "linux" in platforms:
        print("\n" + "=" * 60)
        print("Phase 3: 构建 Linux 安装包")
        print("=" * 60)
        from build_linux import build_linux
        build_linux(
            root_dir=ROOT_DIR,
            cache_dir=CACHE_DIR,
            dist_dir=DIST_DIR,
            installer_dir=INSTALLER_DIR,
        )


def main():
    parser = argparse.ArgumentParser(description="构建离线安装包")
    parser.add_argument("--platform", choices=["windows", "linux", "both"],
                        default="both", help="目标平台（默认 both）")
    parser.add_argument("--skip-download", action="store_true",
                        help="跳过资源下载，使用 build_cache 中已有资源")
    args = parser.parse_args()

    platforms = ["windows", "linux"] if args.platform == "both" else [args.platform]

    print("知识库智能问答系统 — 离线安装包构建工具")
    print(f"目标平台: {', '.join(platforms)}")

    # 将 scripts/ 加入 path 以便 import 构建模块
    sys.path.insert(0, str(SCRIPTS_DIR))

    phase_download(platforms, args.skip_download)
    phase_build(platforms)

    print("\n" + "=" * 60)
    print("构建完成！输出目录: dist/")
    print("=" * 60)

    for f in DIST_DIR.iterdir():
        size_mb = f.stat().st_size / (1024 * 1024)
        print(f"  {f.name} ({size_mb:.1f} MB)")


if __name__ == "__main__":
    main()

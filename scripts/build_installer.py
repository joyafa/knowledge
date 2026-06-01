"""离线安装包统一构建入口（PyInstaller 版本）。

使用 PyInstaller 将应用编译为独立 exe，再用 NSIS 打包为安装程序。
无需预下载 Python 运行时或 AI 模型——模型在首次运行时自动下载。

使用方式:
    python scripts/build_installer.py --platform windows
    python scripts/build_installer.py --platform both

前置条件:
    pip install pyinstaller
    Windows: NSIS 3 已安装（makensis 在 PATH 中）
    Linux: ruby + fpm 已安装

输出:
    dist/knowledge-setup-{ver}-windows.exe
    dist/knowledge-assistant_{ver}_amd64.deb
"""

import argparse
import shutil
import subprocess
import sys
from pathlib import Path

# 项目根目录
ROOT_DIR = Path(__file__).resolve().parent.parent
SCRIPTS_DIR = ROOT_DIR / "scripts"
INSTALLER_DIR = SCRIPTS_DIR / "installer"
DIST_DIR = ROOT_DIR / "dist"


def check_dependencies(platforms: list[str]):
    """检查构建依赖是否就绪。"""
    all_ok = True

    # 检查 PyInstaller
    result = subprocess.run(
        [sys.executable, "-m", "PyInstaller", "--version"],
        capture_output=True, text=True
    )
    if result.returncode != 0:
        print("  错误: PyInstaller 未安装，请运行: pip install pyinstaller")
        all_ok = False
    else:
        print(f"  PyInstaller: {result.stdout.strip()}")

    # 检查 NSIS (Windows)
    if "windows" in platforms:
        if not shutil.which("makensis"):
            print("  错误: NSIS (makensis) 未找到，请安装 NSIS 3")
            print("  https://nsis.sourceforge.io/Download")
            all_ok = False
        else:
            result = subprocess.run(["makensis", "/VERSION"], capture_output=True, text=True)
            print(f"  NSIS: {result.stdout.strip()}")

    return all_ok


def phase_build(platforms: list[str], include_models: bool = False):
    """构建阶段：调用平台构建脚本。"""
    DIST_DIR.mkdir(parents=True, exist_ok=True)

    if "windows" in platforms:
        print("\n" + "=" * 60)
        print("Phase 1: 构建 Windows 安装包")
        if not include_models:
            print("  (跳过模型复制 — 模型运行时自动下载)")
        print("=" * 60)
        from build_windows import build_windows
        build_windows(
            root_dir=ROOT_DIR,
            cache_dir=ROOT_DIR / "build_cache",
            dist_dir=DIST_DIR,
            installer_dir=INSTALLER_DIR,
            skip_models=not include_models,
        )

    if "linux" in platforms:
        print("\n" + "=" * 60)
        print("Phase 2: 构建 Linux 安装包")
        print("=" * 60)
        from build_linux import build_linux
        build_linux(
            root_dir=ROOT_DIR,
            cache_dir=ROOT_DIR / "build_cache",
            dist_dir=DIST_DIR,
            installer_dir=INSTALLER_DIR,
        )


def main():
    parser = argparse.ArgumentParser(description="构建离线安装包（PyInstaller 版本）")
    parser.add_argument("--platform", choices=["windows", "linux", "both"],
                        default="windows", help="目标平台（默认 windows）")
    parser.add_argument("--include-models", action="store_true",
                        help="将模型文件也打包进安装包（默认不打包，运行时自动下载）")
    args = parser.parse_args()

    platforms = ["windows", "linux"] if args.platform == "both" else [args.platform]

    print("知识库智能问答系统 — 离线安装包构建工具 (PyInstaller)")
    print(f"目标平台: {', '.join(platforms)}")
    print()

    # 检查依赖
    if not check_dependencies(platforms):
        sys.exit(1)

    # 将 scripts/ 加入 path 以便 import 构建模块
    sys.path.insert(0, str(SCRIPTS_DIR))

    # 直接构建（无需下载资源——PyInstaller 已包含所有依赖，模型运行时自动下载）
    phase_build(platforms, include_models=args.include_models)

    print("\n" + "=" * 60)
    print("构建完成！输出目录: dist/")
    print("=" * 60)

    for f in DIST_DIR.iterdir():
        if f.is_file() and f.suffix in (".exe", ".deb"):
            size_mb = f.stat().st_size / (1024 * 1024)
            print(f"  {f.name} ({size_mb:.1f} MB)")


if __name__ == "__main__":
    main()

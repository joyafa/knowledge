"""离线部署打包脚本。

直接将当前项目目录（含虚拟环境和本地模型缓存）打包为 zip。
目标机器解压后即可运行，无需联网安装。

使用方式:
    python scripts/prepare_offline.py
"""

import os
import shutil
import sys
import zipfile
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent.parent
OUTPUT_ZIP = PROJECT_DIR / "knowledge_offline.zip"

# 排除的目录和文件
EXCLUDES = {
    "__pycache__",
    ".git",
    ".gitignore",
    ".claude",
    ".qoder",
    "node_modules",
    ".venv",
    ".idea",
    ".vscode",
    "*.pyc",
    # 排除旧的 venv（保留 venv311）
}

# 排除的目录名前缀/包含关系
EXCLUDE_DIR_NAMES = {
    "__pycache__",
    ".git",
    ".claude",
    ".qoder",
    ".venv",
    ".idea",
    ".vscode",
    "node_modules",
}


def should_exclude(path: Path, project_root: Path) -> bool:
    """判断文件/目录是否应排除。"""
    rel = path.relative_to(project_root)
    parts = rel.parts

    # 排除顶层的特定目录
    top_level_excludes = {
        "knowledge_offline",
        "knowledge_offline.zip",
        "test_retrieve.py",
    }
    if parts[0] in top_level_excludes:
        return True

    # 任意层级排除
    for part in parts:
        if part in EXCLUDE_DIR_NAMES:
            return True

    # 排除 .pyc 文件
    if path.suffix == ".pyc":
        return True

    # 排除 Streamlit 缓存
    if ".streamlit" in parts:
        return True

    return False


def create_zip():
    """将项目目录打包为 zip。"""
    print("=" * 50)
    print("知识库助手 — 离线部署打包")
    print("=" * 50)
    print(f"项目目录: {PROJECT_DIR}")
    print(f"输出文件: {OUTPUT_ZIP}")
    print()

    file_count = 0
    total_size = 0

    with zipfile.ZipFile(OUTPUT_ZIP, "w", zipfile.ZIP_DEFLATED, compresslevel=6) as zf:
        for root, dirs, files in os.walk(PROJECT_DIR):
            root_path = Path(root)

            # 过滤排除的目录（原地修改 dirs 列表）
            dirs[:] = [d for d in dirs if not should_exclude(root_path / d, PROJECT_DIR)]

            # 跳过被排除的根目录
            if should_exclude(root_path, PROJECT_DIR):
                dirs.clear()
                continue

            for fname in files:
                file_path = root_path / fname
                if should_exclude(file_path, PROJECT_DIR):
                    continue

                arcname = str(file_path.relative_to(PROJECT_DIR))
                file_size = file_path.stat().st_size
                total_size += file_size

                zf.write(file_path, arcname)
                file_count += 1

                if file_count % 100 == 0:
                    print(f"  已打包 {file_count} 个文件...")

    zip_size = OUTPUT_ZIP.stat().st_size
    print()
    print("=" * 50)
    print(f"打包完成！")
    print(f"  文件数: {file_count}")
    print(f"  原始大小: {total_size / (1024*1024):.1f} MB")
    print(f"  压缩后: {zip_size / (1024*1024):.1f} MB")
    print(f"  输出: {OUTPUT_ZIP}")
    print("=" * 50)


def generate_readme():
    """生成部署说明。"""
    readme_path = PROJECT_DIR / "离线部署说明.txt"
    readme_path.write_text("""知识库助手 - 离线部署说明
================================

一、部署步骤（Windows）

  1. 将 knowledge_offline.zip 解压到目标机器（如 D:\\knowledge）
  2. 打开 PowerShell，进入项目目录:
     cd D:\\knowledge
  3. 创建虚拟环境（需要 Python 3.11+）:
     python -m venv venv311
  4. 激活虚拟环境:
     .\\venv311\\Scripts\\Activate.ps1
  5. 离线安装依赖（从 wheels 目录）:
     pip install --no-index --find-links=wheels -r requirements.txt
     若缺少 wheels 目录，可用:
     pip install -r requirements.txt
  6. 文档入库:
     python scripts/ingest.py
  7. 启动服务:
     streamlit run app.py

二、配置说明

  编辑 config.yaml:
  - LLM API 地址和密钥
  - embedding 和 reranker 模型路径（已配置本地缓存路径）

三、注意事项
  - 目标机器需要 Python 3.11+
  - embedding 模型约 400MB，无需 GPU
  - 首次启动加载模型约需 15 秒
""", encoding="utf-8")
    print(f"部署说明已生成: {readme_path}")


if __name__ == "__main__":
    generate_readme()
    create_zip()

"""离线部署打包脚本。

在有网络的机器上运行此脚本，下载所有依赖和模型，生成离线安装包。
然后将整个 output 目录拷贝到目标机器即可。

使用方式:
    python scripts/prepare_offline.py

输出:
    knowledge_offline/
    ├── wheels/          # Python 依赖包（wheel 文件）
    ├── model/           # Embedding 模型文件
    └── project/         # 项目代码
"""

import os
import shutil
import subprocess
import sys
from pathlib import Path

# 离线包输出目录
OUTPUT_DIR = Path("knowledge_offline")
WHEELS_DIR = OUTPUT_DIR / "wheels"
MODEL_DIR = OUTPUT_DIR / "model"
PROJECT_DIR = OUTPUT_DIR / "project"

# Embedding 模型名称
EMBEDDING_MODEL = "shibing624/text2vec-base-chinese"


def download_wheels():
    """下载所有 Python 依赖的 wheel 文件。"""
    print("=" * 50)
    print("[1/3] 下载 Python 依赖包...")
    print("=" * 50)
    WHEELS_DIR.mkdir(parents=True, exist_ok=True)

    subprocess.check_call([
        sys.executable, "-m", "pip", "download",
        "-r", "requirements.txt",
        "-d", str(WHEELS_DIR),
    ])
    print(f"依赖包已下载到: {WHEELS_DIR}")


def download_model():
    """下载 Embedding 模型到本地目录。"""
    print("\n" + "=" * 50)
    print("[2/3] 下载 Embedding 模型...")
    print("=" * 50)
    MODEL_DIR.mkdir(parents=True, exist_ok=True)

    from sentence_transformers import SentenceTransformer
    print(f"正在下载模型: {EMBEDDING_MODEL}")
    model = SentenceTransformer(EMBEDDING_MODEL)
    model.save(str(MODEL_DIR))
    print(f"模型已保存到: {MODEL_DIR}")


def copy_project():
    """拷贝项目代码。"""
    print("\n" + "=" * 50)
    print("[3/3] 打包项目代码...")
    print("=" * 50)

    if PROJECT_DIR.exists():
        shutil.rmtree(PROJECT_DIR)

    # 需要拷贝的文件和目录
    includes = [
        "app.py",
        "config.yaml",
        "requirements.txt",
        "rag",
        "scripts",
        "knowledge",
    ]

    for item in includes:
        src = Path(item)
        dst = PROJECT_DIR / item
        if src.is_dir():
            shutil.copytree(src, dst)
        elif src.exists():
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dst)

    print(f"项目代码已拷贝到: {PROJECT_DIR}")


def generate_install_script():
    """生成离线安装脚本（Windows + Linux 双版本）。"""
    # Windows 版
    win_script = PROJECT_DIR / "install_offline.bat"
    win_script.write_text("""@echo off
chcp 65001 >nul
REM 离线安装脚本 - Windows 版

set SCRIPT_DIR=%~dp0
for %%I in ("%SCRIPT_DIR%..") do set OFFLINE_DIR=%%~fI
set WHEELS_DIR=%OFFLINE_DIR%\\wheels
set MODEL_DIR=%OFFLINE_DIR%\\model

echo ==========================================
echo   知识库助手 - 离线安装 (Windows)
echo ==========================================

REM 1. 创建虚拟环境
echo.
echo [1/3] 创建 Python 虚拟环境...
python -m venv venv
call venv\\Scripts\\activate.bat

REM 2. 离线安装依赖
echo.
echo [2/3] 安装 Python 依赖（离线）...
pip install --no-index --find-links="%WHEELS_DIR%" -r requirements.txt

REM 3. 更新配置，使用本地模型路径
echo.
echo [3/3] 配置本地 Embedding 模型路径...
python -c "import yaml; f=open('config.yaml','r',encoding='utf-8'); c=yaml.safe_load(f); f.close(); c['embedding']['local_path']=r'%MODEL_DIR%'; f=open('config.yaml','w',encoding='utf-8'); yaml.dump(c,f,allow_unicode=True,default_flow_style=False); f.close(); print('已更新 config.yaml')"

echo.
echo ==========================================
echo   安装完成！
echo ==========================================
echo.
echo 后续步骤:
echo   1. 将 Markdown/PDF/TXT 文档放入 knowledge/ 目录
echo   2. 运行入库:  venv\\Scripts\\activate ^&^& python scripts/ingest.py
echo   3. 启动服务:  venv\\Scripts\\activate ^&^& streamlit run app.py --server.port 8501
echo.
pause
""", encoding="utf-8")

    # Linux 版
    install_script = PROJECT_DIR / "install_offline.sh"
    install_script.write_text("""#!/bin/bash
# 离线安装脚本 — 在目标 Linux 机器上运行

set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
OFFLINE_DIR="$(dirname "$SCRIPT_DIR")"
WHEELS_DIR="$OFFLINE_DIR/wheels"
MODEL_DIR="$OFFLINE_DIR/model"

echo "=========================================="
echo "  知识库助手 — 离线安装"
echo "=========================================="

# 1. 创建虚拟环境
echo ""
echo "[1/3] 创建 Python 虚拟环境..."
python3 -m venv venv
source venv/bin/activate

# 2. 离线安装依赖
echo ""
echo "[2/3] 安装 Python 依赖（离线）..."
pip install --no-index --find-links="$WHEELS_DIR" -r requirements.txt

# 3. 更新配置，使用本地模型路径
echo ""
echo "[3/3] 配置本地 Embedding 模型路径..."
python3 -c "
import yaml
with open('config.yaml', 'r', encoding='utf-8') as f:
    config = yaml.safe_load(f)
config['embedding']['local_path'] = '$MODEL_DIR'
with open('config.yaml', 'w', encoding='utf-8') as f:
    yaml.dump(config, f, allow_unicode=True, default_flow_style=False)
print('已更新 config.yaml，Embedding 模型指向本地路径')
"

echo ""
echo "=========================================="
echo "  安装完成！"
echo "=========================================="
echo ""
echo "后续步骤:"
echo "  1. 将 Markdown/PDF/TXT 文档放入 knowledge/ 目录"
echo "  2. 运行入库:  python scripts/ingest.py"
echo "  3. 启动服务:  streamlit run app.py --server.port 8501"
echo ""
""", encoding="utf-8")

    # 也要写一个 Windows 版的安装说明
    readme = OUTPUT_DIR / "部署说明.txt"
    readme.write_text("""知识库助手 - 离线部署说明
================================

一、准备阶段（在有网的机器上）
  1. 运行 python scripts/prepare_offline.py
  2. 将生成的 knowledge_offline/ 整个目录拷贝到 U 盘

二、Windows 部署
  1. 将 knowledge_offline/ 拷贝到目标机器
  2. 进入 knowledge_offline/project/ 目录
  3. 双击运行 install_offline.bat
  4. 将知识库文档放入 knowledge/ 目录
  5. 入库:  venv\\Scripts\\activate && python scripts/ingest.py
  6. 启动:  venv\\Scripts\\activate && streamlit run app.py --server.port 8501

三、Linux 部署
  1. 将 knowledge_offline/ 拷贝到目标机器
  2. 进入 knowledge_offline/project/ 目录
  3. 给安装脚本加执行权限:  chmod +x install_offline.sh
  4. 运行安装:  ./install_offline.sh
  5. 将知识库文档放入 knowledge/ 目录
  6. 入库:  source venv/bin/activate && python scripts/ingest.py
  7. 启动:  source venv/bin/activate && streamlit run app.py --server.port 8501

四、配置 LLM（部署后修改 config.yaml）
  - 外部 API: api_base 填远程地址，api_key 填密钥
  - 本地 vLLM: api_base 填 http://localhost:8000/v1，api_key 填 EMPTY

五、注意事项
  - 目标机器需要 Python 3.10+
  - 如果目标机器架构不同（如 ARM），需要在目标架构上下载 wheel
  - Embedding 模型约 400MB，无需 GPU
""", encoding="utf-8")

    print(f"离线安装脚本已生成: {install_script}")
    print(f"Windows 安装脚本已生成: {win_script}")


def main():
    print("知识库助手 — 离线部署打包工具")
    print()

    if OUTPUT_DIR.exists():
        shutil.rmtree(OUTPUT_DIR)
    OUTPUT_DIR.mkdir()

    # 设置国内镜像
    os.environ["HF_ENDPOINT"] = "https://hf-mirror.com"

    download_wheels()
    download_model()
    copy_project()
    generate_install_script()

    # 统计大小
    total_size = sum(f.stat().st_size for f in OUTPUT_DIR.rglob("*") if f.is_file())
    size_mb = total_size / (1024 * 1024)

    print("\n" + "=" * 50)
    print(f"打包完成！输出目录: {OUTPUT_DIR.absolute()}")
    print(f"总大小: {size_mb:.1f} MB")
    print("=" * 50)
    print("\n将 knowledge_offline/ 目录拷贝到目标机器，运行 install_offline.sh 即可")


if __name__ == "__main__":
    main()

#!/bin/bash
# 知识库智能问答系统 — 启动脚本（前台运行）
# 通过 run_app.py 统一入口，与 Windows 版本保持一致
set -e

APP_DIR="/opt/knowledge-assistant"
CONFIG_DIR="/etc/knowledge-assistant"

echo ""
echo "============================================"
echo "  知识库智能问答系统"
echo "  启动后请用浏览器访问: http://localhost:8501"
echo "  按 Ctrl+C 停止服务"
echo "============================================"
echo ""

# 模型根目录和缓存（run_app.py 内部自动检测本地模型路径）
export MODEL_ROOT="${APP_DIR}/model"
export SENTENCE_TRANSFORMERS_HOME="${APP_DIR}/model"
export HF_ENDPOINT="https://hf-mirror.com"

cd "${APP_DIR}/app"
exec "${APP_DIR}/python/bin/python3" run_app.py

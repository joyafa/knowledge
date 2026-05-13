#!/bin/bash
# 知识库智能问答系统 — 启动脚本（前台运行）
set -e

APP_DIR="/opt/knowledge-assistant"
PYTHON="${APP_DIR}/python/bin/python3"
CONFIG_DIR="/etc/knowledge-assistant"

echo ""
echo "============================================"
echo "  知识库智能问答系统"
echo "  启动后请用浏览器访问: http://localhost:8501"
echo "  按 Ctrl+C 停止服务"
echo "============================================"
echo ""

export HF_ENDPOINT="https://hf-mirror.com"

cd "${APP_DIR}/app"
exec "${PYTHON}" -m streamlit run app.py \
    --server.port 8501 \
    --server.address 0.0.0.0 \
    --server.headless true \
    --browser.gatherUsageStats false \
    --server.enableCORS false

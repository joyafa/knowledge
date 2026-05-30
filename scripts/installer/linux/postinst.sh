#!/bin/bash
# deb/rpm 安装后脚本
set -e

APP_DIR="/opt/knowledge-assistant"
DATA_DIR="/var/lib/knowledge-assistant"
LOG_DIR="/var/log/knowledge-assistant"
CONFIG_DIR="/etc/knowledge-assistant"

# 创建系统用户（不存在时）
if ! id -u knowledge-assistant >/dev/null 2>&1; then
    useradd --system --no-create-home --shell /usr/sbin/nologin knowledge-assistant
fi

# 创建数据目录
mkdir -p "${DATA_DIR}/chroma_db"
mkdir -p "${DATA_DIR}/knowledge"
mkdir -p "${DATA_DIR}/logs"
mkdir -p "${DATA_DIR}/chat_history"
mkdir -p "${LOG_DIR}"

# 复制初始知识库文档（仅当目标目录为空时）
if [ -d "${APP_DIR}/app/knowledge" ] && [ -z "$(ls -A "${DATA_DIR}/knowledge/" 2>/dev/null)" ]; then
    cp -r "${APP_DIR}/app/knowledge/"* "${DATA_DIR}/knowledge/" 2>/dev/null || true
fi

# 创建配置文件（仅首次安装）
mkdir -p "${CONFIG_DIR}"
if [ ! -f "${CONFIG_DIR}/config.yaml" ]; then
    cp "${APP_DIR}/app/config.yaml" "${CONFIG_DIR}/config.yaml"
fi

# 更新 config.yaml 中的系统路径（模型路径由 run_app.py 运行时自动检测）
if command -v python3 >/dev/null 2>&1; then
    python3 -c "
import yaml, sys
p = '${CONFIG_DIR}/config.yaml'
with open(p, 'r', encoding='utf-8') as f:
    c = yaml.safe_load(f)
c['vectorstore']['persist_directory'] = '${DATA_DIR}/chroma_db'
c['knowledge']['docs_directory'] = '${DATA_DIR}/knowledge'
# 模型 local_path 保持 env var 引用，不硬编码
if 'local_path' in c.get('embedding', {}) and c['embedding']['local_path'].startswith('/'):
    c['embedding']['local_path'] = ''
if 'local_path' in c.get('reranker', {}) and c['reranker']['local_path'].startswith('/'):
    c['reranker']['local_path'] = ''
with open(p, 'w', encoding='utf-8') as f:
    yaml.dump(c, f, default_flow_style=False, allow_unicode=True, sort_keys=False)
" 2>/dev/null || true
fi

# 符号链接 config.yaml 到应用目录
if [ ! -L "${APP_DIR}/app/config.yaml" ]; then
    mv "${APP_DIR}/app/config.yaml" "${APP_DIR}/app/config.yaml.bak" 2>/dev/null || true
    ln -s "${CONFIG_DIR}/config.yaml" "${APP_DIR}/app/config.yaml"
fi

# 设置权限
chown -R knowledge-assistant:knowledge-assistant "${DATA_DIR}"
chown -R knowledge-assistant:knowledge-assistant "${LOG_DIR}"
chown -R knowledge-assistant:knowledge-assistant "${APP_DIR}/app/chat_history" 2>/dev/null || true
chmod +x /usr/local/bin/knowledge-* 2>/dev/null || true

# 重载 systemd
systemctl daemon-reload >/dev/null 2>&1 || true

echo ""
echo "安装完成！"
echo "  配置文件: ${CONFIG_DIR}/config.yaml"
echo "  知识库目录: ${DATA_DIR}/knowledge/"
echo ""
echo "  启动服务: sudo systemctl start knowledge-assistant"
echo "  访问地址: http://localhost:8501"
echo "  文档入库: sudo -u knowledge-assistant knowledge-ingest"
echo ""

#!/bin/bash
# deb/rpm 卸载前脚本
set -e

# 停止服务
systemctl stop knowledge-assistant >/dev/null 2>&1 || true
systemctl disable knowledge-assistant >/dev/null 2>&1 || true

# 删除 systemd 服务文件
rm -f /usr/lib/systemd/system/knowledge-assistant.service
systemctl daemon-reload >/dev/null 2>&1 || true

# 删除命令链接
rm -f /usr/local/bin/knowledge-launch
rm -f /usr/local/bin/knowledge-ingest
rm -f /usr/local/bin/knowledge-stop

# 删除系统用户（仅当使用 purge 卸载时）
if [ "$1" = "purge" ] 2>/dev/null; then
    userdel knowledge-assistant >/dev/null 2>&1 || true
    rm -rf /var/lib/knowledge-assistant
    rm -rf /var/log/knowledge-assistant
    rm -rf /etc/knowledge-assistant
fi

"""结构化日志模块。

统一日志输出，支持控制台 + 文件双输出，彩色高亮。
"""

import logging
import sys
from datetime import datetime
from pathlib import Path
from typing import Optional

# 日志目录
LOG_DIR = Path("./logs")

# 审计日志目录
AUDIT_DIR = LOG_DIR / "audit"

# 系统日志文件
SYS_LOG_FILE = LOG_DIR / "system.log"


def _ensure_dirs():
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    AUDIT_DIR.mkdir(parents=True, exist_ok=True)


class ColoredFormatter(logging.Formatter):
    """彩色控制台格式化器。"""
    COLORS = {
        "DEBUG": "\033[36m",
        "INFO": "\033[32m",
        "WARNING": "\033[33m",
        "ERROR": "\033[31m",
        "CRITICAL": "\033[35m",
    }
    RESET = "\033[0m"
    GREY = "\033[90m"

    def format(self, record):
        color = self.COLORS.get(record.levelname, "")
        record.levelname_colored = f"{color}{record.levelname}{self.RESET}"
        record.time_colored = f"{self.GREY}{self.formatTime(record, '%H:%M:%S')}{self.RESET}"
        return super().format(record)


def setup_logging(level: int = logging.INFO) -> logging.Logger:
    """初始化日志系统。"""
    _ensure_dirs()

    logger = logging.getLogger("knowledge")
    logger.setLevel(level)

    if logger.handlers:
        return logger

    # 控制台 handler（彩色）
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(level)
    console_fmt = ColoredFormatter(
        "%(time_colored)s [%(levelname_colored)s] %(name)s | %(message)s"
    )
    console_handler.setFormatter(console_fmt)
    logger.addHandler(console_handler)

    # 文件 handler（完整日志）
    file_handler = logging.FileHandler(SYS_LOG_FILE, encoding="utf-8")
    file_handler.setLevel(logging.DEBUG)
    file_fmt = logging.Formatter(
        "%(asctime)s [%(levelname)s] %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    file_handler.setFormatter(file_fmt)
    logger.addHandler(file_handler)

    return logger


def get_logger(name: str = "knowledge") -> logging.Logger:
    """获取 logger 实例。"""
    logger = logging.getLogger(name)
    if not logger.handlers:
        logger = setup_logging()
    return logger


def audit_log(
    username: str,
    action: str,
    details: str = "",
    query: str = "",
    answer_preview: str = "",
    result_count: int = 0,
    duration_ms: float = 0,
):
    """记录审计日志。

    Args:
        username: 操作用户
        action: 操作类型（query, login, logout, feedback, etc.）
        details: 详细信息
        query: 用户查询原文
        answer_preview: 回答摘要（前200字）
        result_count: 检索结果数
        duration_ms: 处理耗时（毫秒）
    """
    from rag.config import get_config
    config = get_config()
    if not config.audit_enabled:
        return

    _ensure_dirs()
    today = datetime.now().strftime("%Y-%m-%d")
    audit_file = AUDIT_DIR / f"{today}.jsonl"

    import json
    entry = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3],
        "username": username,
        "action": action,
        "details": details,
        "query": query[:500] if query else "",
        "answer_preview": answer_preview[:200] if answer_preview else "",
        "result_count": result_count,
        "duration_ms": round(duration_ms, 1),
    }

    with open(audit_file, "a", encoding="utf-8") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")

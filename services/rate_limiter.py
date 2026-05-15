"""速率限制模块。

简单的内存速率限制器，按用户限制每分钟请求数。
定期清理不活跃用户，防止内存泄漏。
"""

import time
from collections import defaultdict
from typing import Tuple

_user_timestamps: dict[str, list[float]] = defaultdict(list)
_last_cleanup: float = time.time()
# 清理间隔：每 10 分钟清理一次
_CLEANUP_INTERVAL: float = 600.0
# 用户不活跃超时：30 分钟无请求则清理
_USER_INACTIVE_TIMEOUT: float = 1800.0


def _cleanup_stale_users():
    """清理不活跃用户的记录，防止内存无限增长。"""
    global _last_cleanup
    now = time.time()
    if now - _last_cleanup < _CLEANUP_INTERVAL:
        return

    stale_users = []
    for username, timestamps in _user_timestamps.items():
        # 清理过期的时间戳
        window_start = now - 60
        timestamps[:] = [t for t in timestamps if t > window_start]
        # 如果用户没有任何近期请求，标记为可清理
        if not timestamps:
            stale_users.append(username)

    for username in stale_users:
        del _user_timestamps[username]

    _last_cleanup = now
    if stale_users:
        from rag.logging_config import get_logger
        logger = get_logger(__name__)
        logger.debug("清理了 %d 个不活跃用户的速率限制记录", len(stale_users))


def check_rate_limit(username: str, max_per_minute: int = 30) -> Tuple[bool, str]:
    """检查用户是否超过速率限制。

    Args:
        username: 用户名
        max_per_minute: 每分钟最大请求数

    Returns:
        (是否允许, 提示消息)
    """
    # 周期性清理
    _cleanup_stale_users()

    now = time.time()
    window_start = now - 60  # 60秒窗口

    timestamps = _user_timestamps[username]
    # 清理过期记录
    timestamps[:] = [t for t in timestamps if t > window_start]

    if len(timestamps) >= max_per_minute:
        wait_time = int(timestamps[0] + 60 - now) + 1
        return False, f"请求过于频繁，请 {wait_time} 秒后再试（限制: {max_per_minute}次/分钟）"

    timestamps.append(now)
    return True, ""

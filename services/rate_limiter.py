"""速率限制模块。

简单的内存速率限制器，按用户限制每分钟请求数。
"""

import time
from collections import defaultdict
from typing import Tuple

_user_timestamps: dict[str, list[float]] = defaultdict(list)


def check_rate_limit(username: str, max_per_minute: int = 30) -> Tuple[bool, str]:
    """检查用户是否超过速率限制。

    Args:
        username: 用户名
        max_per_minute: 每分钟最大请求数

    Returns:
        (是否允许, 提示消息)
    """
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

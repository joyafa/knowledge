"""速率限制器测试。"""

import time

import services.rate_limiter as rate_limiter

from services.rate_limiter import check_rate_limit, _user_timestamps, _cleanup_stale_users


class TestRateLimiter:
    """速率限制器单元测试。"""

    def setup_method(self):
        """每个测试前清空状态。"""
        _user_timestamps.clear()

    def test_first_request_allowed(self):
        allowed, msg = check_rate_limit("user1", max_per_minute=5)
        assert allowed is True
        assert msg == ""

    def test_within_limit(self):
        for _ in range(4):
            allowed, _ = check_rate_limit("user1", max_per_minute=5)
            assert allowed is True

    def test_exceeds_limit(self):
        for _ in range(5):
            allowed, _ = check_rate_limit("user1", max_per_minute=5)
            assert allowed is True

        # 第 6 次应被拦截
        allowed, msg = check_rate_limit("user1", max_per_minute=5)
        assert allowed is False
        assert "过于频繁" in msg

    def test_different_users_isolated(self):
        # user1 用完配额
        for _ in range(5):
            check_rate_limit("user1", max_per_minute=5)

        # user2 仍可用
        allowed, _ = check_rate_limit("user2", max_per_minute=5)
        assert allowed is True

    def test_cleanup_stale_users(self):
        # 模拟一个用户有旧记录
        _user_timestamps["old_user"] = [time.time() - 120]  # 2分钟前

        # 绕过清理间隔检查，强制触发清理
        rate_limiter._last_cleanup = 0

        _cleanup_stale_users()

        # 旧用户应被清理
        assert "old_user" not in _user_timestamps

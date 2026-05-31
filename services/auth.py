"""用户认证服务模块。

管理用户注册、登录、密码修改等账户操作。
密码使用 PBKDF2-SHA256 加盐哈希存储，不保存明文。
用户数据持久化在 JSON 文件中。

数据结构（data/users.json）:
{
  "users": {
    "admin": {
      "password_hash": "hex...",
      "salt": "hex...",
      "role": "admin",
      "created_at": "2025-01-01T00:00:00"
    }
  }
}
"""

import hashlib
import json
import os
from datetime import datetime
from pathlib import Path
from threading import Lock
from typing import Optional


try:
    from rag.logging_config import get_logger
    logger = get_logger(__name__)
except ImportError:
    import logging
    logger = logging.getLogger(__name__)


# ── 密码哈希 ──

def _hash_password(password: str, salt: Optional[str] = None) -> tuple[str, str]:
    """PBKDF2-SHA256 加盐哈希。

    Returns:
        (password_hash_hex, salt_hex)
    """
    if salt is None:
        salt = os.urandom(16).hex()
    dk = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode("utf-8"),
        bytes.fromhex(salt),
        100_000,
    )
    return dk.hex(), salt


def _verify_password(password: str, salt_hex: str, hash_hex: str) -> bool:
    """验证密码是否匹配。"""
    computed, _ = _hash_password(password, salt_hex)
    return computed == hash_hex


# ── 用户管理器 ──

class UserManager:
    """用户账户管理器（线程安全）。"""

    def __init__(self, users_file: str = "data/users.json"):
        self._file = Path(users_file)
        self._lock = Lock()
        self._data: dict = {}
        self._load()

    # ── 文件读写 ──

    def _load(self):
        """从文件加载用户数据。"""
        if self._file.exists():
            try:
                raw = self._file.read_text(encoding="utf-8")
                self._data = json.loads(raw)
            except (json.JSONDecodeError, OSError) as e:
                logger.warning("用户数据文件损坏，初始化空库: %s", e)
                self._data = {"users": {}}
        else:
            self._data = {"users": {}}

    def _save(self):
        """将用户数据写入文件。"""
        self._file.parent.mkdir(parents=True, exist_ok=True)
        self._file.write_text(
            json.dumps(self._data, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )

    # ── 公开接口 ──

    def authenticate(self, username: str, password: str) -> bool:
        """验证用户名和密码。"""
        with self._lock:
            user = self._data.get("users", {}).get(username)
            if not user:
                return False
            return _verify_password(password, user["salt"], user["password_hash"])

    def register(self, username: str, password: str) -> tuple[bool, str]:
        """注册新用户。

        Returns:
            (success, message)
        """
        username = username.strip()
        if not username:
            return False, "用户名不能为空"
        if len(username) < 2:
            return False, "用户名至少需要 2 个字符"
        if len(username) > 32:
            return False, "用户名不能超过 32 个字符"
        if not password or len(password) < 4:
            return False, "密码至少需要 4 个字符"

        with self._lock:
            users = self._data.setdefault("users", {})
            if username in users:
                return False, "用户名已存在"

            pwd_hash, salt = _hash_password(password)
            # 首个注册用户自动设为管理员
            role = "admin" if len(users) == 0 else "user"
            users[username] = {
                "password_hash": pwd_hash,
                "salt": salt,
                "role": role,
                "created_at": datetime.now().strftime("%Y-%m-%dT%H:%M:%S"),
            }
            self._save()

        logger.info("新用户注册: %s (角色: %s)", username, role)
        return True, "注册成功" + ("（已自动设为管理员）" if role == "admin" else "")

    def change_password(self, username: str, old_password: str, new_password: str) -> tuple[bool, str]:
        """修改密码。"""
        if not new_password or len(new_password) < 4:
            return False, "新密码至少需要 4 个字符"

        with self._lock:
            user = self._data.get("users", {}).get(username)
            if not user:
                return False, "用户不存在"
            if not _verify_password(old_password, user["salt"], user["password_hash"]):
                return False, "原密码错误"

            pwd_hash, salt = _hash_password(new_password)
            user["password_hash"] = pwd_hash
            user["salt"] = salt
            self._save()

        logger.info("用户 %s 修改了密码", username)
        return True, "密码修改成功"

    def reset_password(self, username: str, new_password: str) -> tuple[bool, str]:
        """管理员重置用户密码（无需旧密码）。

        Returns:
            (success, message)
        """
        if not new_password or len(new_password) < 4:
            return False, "新密码至少需要 4 个字符"

        with self._lock:
            user = self._data.get("users", {}).get(username)
            if not user:
                return False, "用户不存在"

            pwd_hash, salt = _hash_password(new_password)
            user["password_hash"] = pwd_hash
            user["salt"] = salt
            self._save()

        logger.info("管理员重置了用户 %s 的密码", username)
        return True, f"已重置 {username} 的密码"

    def get_role(self, username: str) -> str:
        """获取用户角色。"""
        with self._lock:
            user = self._data.get("users", {}).get(username)
            return user.get("role", "user") if user else "user"

    def is_admin(self, username: str) -> bool:
        """判断是否为管理员。"""
        return self.get_role(username) == "admin"

    def list_users(self) -> list[dict]:
        """列出所有用户（仅管理员可调用）。"""
        with self._lock:
            result = []
            for name, info in self._data.get("users", {}).items():
                result.append({
                    "username": name,
                    "role": info.get("role", "user"),
                    "created_at": info.get("created_at", ""),
                })
            # 按注册时间排序
            result.sort(key=lambda u: u["created_at"])
            return result

    def delete_user(self, username: str) -> tuple[bool, str]:
        """删除用户。"""
        with self._lock:
            users = self._data.get("users", {})
            if username not in users:
                return False, "用户不存在"
            if users[username].get("role") == "admin":
                # 检查是否还有其他管理员
                other_admins = [
                    n for n, u in users.items()
                    if n != username and u.get("role") == "admin"
                ]
                if not other_admins:
                    return False, "不能删除最后一个管理员账户"
            del users[username]
            self._save()

        logger.info("删除了用户: %s", username)
        return True, f"已删除用户 {username}"

    def user_exists(self, username: str) -> bool:
        """检查用户是否存在。"""
        with self._lock:
            return username in self._data.get("users", {})

    def user_count(self) -> int:
        """返回注册用户总数。"""
        with self._lock:
            return len(self._data.get("users", {}))


# ── 全局单例 ──

_user_manager: Optional[UserManager] = None
_lock_singleton = Lock()


def get_user_manager(users_file: str = "data/users.json") -> UserManager:
    """获取全局 UserManager 单例。"""
    global _user_manager
    if _user_manager is None:
        with _lock_singleton:
            if _user_manager is None:
                _user_manager = UserManager(users_file)
    return _user_manager

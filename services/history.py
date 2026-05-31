"""聊天记录服务 — 按用户、会话隔离持久化。

支持多会话管理、JSON 持久化、导出功能。
"""

import json
import uuid
from datetime import datetime
from pathlib import Path
from typing import Optional

from rag.logging_config import get_logger, audit_log

logger = get_logger(__name__)

CHAT_HISTORY_DIR = Path("./chat_history")


# ── 会话管理 ──

def _user_dir(username: str) -> Path:
    d = CHAT_HISTORY_DIR / username
    d.mkdir(parents=True, exist_ok=True)
    return d


def _sessions_file(username: str) -> Path:
    return _user_dir(username) / "_sessions.json"


def _session_file(username: str, session_id: str) -> Path:
    d = _user_dir(username) / "sessions"
    d.mkdir(parents=True, exist_ok=True)
    return d / f"{session_id}.json"


def list_sessions(username: str) -> list[dict]:
    """列出用户的所有会话。"""
    sf = _sessions_file(username)
    if not sf.exists():
        return []
    try:
        data = json.loads(sf.read_text(encoding="utf-8"))
        # 兼容两种格式: 直接的 list 或 {"sessions": [...]}
        if isinstance(data, list):
            sessions = data
        else:
            sessions = data.get("sessions", [])
        sessions.sort(key=lambda s: s.get("updated_at", ""), reverse=True)
        return sessions
    except (json.JSONDecodeError, OSError) as e:
        logger.warning("会话文件损坏 %s: %s", sf, e)
        return []


def get_active_session_id(username: str) -> Optional[str]:
    """获取用户当前活跃会话 ID。"""
    sf = _sessions_file(username)
    if sf.exists():
        try:
            data = json.loads(sf.read_text(encoding="utf-8"))
            active = data.get("active_session")
            if active:
                return active
        except (json.JSONDecodeError, OSError) as e:
            logger.warning("读取活跃会话失败 %s: %s", sf, e)
    # 默认创建或获取第一个会话
    sessions = list_sessions(username)
    if sessions:
        return sessions[0]["id"]
    return create_session(username)


def create_session(username: str, title: str = "") -> str:
    """创建新会话，返回会话 ID。"""
    session_id = uuid.uuid4().hex[:12]
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    sessions = list_sessions(username)
    sessions.append({
        "id": session_id,
        "title": title or "新会话",
        "created_at": now,
        "updated_at": now,
        "message_count": 0,
    })

    _save_sessions(username, sessions)
    logger.info("创建会话: %s -> %s", username, session_id)
    return session_id


def update_session_title(username: str, session_id: str, title: str):
    """更新会话标题（如根据首次提问自动命名）。"""
    sf = _sessions_file(username)
    data = {"sessions": [], "active_session": session_id}
    if sf.exists():
        try:
            old = json.loads(sf.read_text(encoding="utf-8"))
            if isinstance(old, list):
                data["sessions"] = old
            else:
                data = old
        except (json.JSONDecodeError, OSError) as e:
            logger.warning("读取会话数据失败 %s: %s", sf, e)

    for sess in data.get("sessions", []):
        if sess["id"] == session_id:
            sess["title"] = title[:30]  # 限制30字
            sess["updated_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            break

    sf.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


def switch_session(session_id: str, username: str = ""):
    """切换活跃会话（仅更新活跃标记）。

    Args:
        session_id: 目标会话 ID
        username: 用户名（可选，不传则从 Streamlit session_state 获取）
    """
    if not username:
        username = _get_username_from_state() or ""
    if not username:
        return
    sf = _sessions_file(username)
    data = {"sessions": [], "active_session": session_id}
    if sf.exists():
        try:
            old = json.loads(sf.read_text(encoding="utf-8"))
            if isinstance(old, list):
                data["sessions"] = old
            else:
                data = old
            data["active_session"] = session_id
        except (json.JSONDecodeError, OSError) as e:
            logger.warning("切换会话失败 %s: %s", sf, e)
    sf.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


def _save_sessions(username: str, sessions: list[dict]):
    """持久化会话列表。"""
    sf = _sessions_file(username)
    data = {"sessions": sessions}
    # 保留活跃会话
    if sf.exists():
        try:
            old = json.loads(sf.read_text(encoding="utf-8"))
            data["active_session"] = old.get("active_session")
        except (json.JSONDecodeError, OSError) as e:
            logger.warning("读取旧会话失败 %s: %s", sf, e)
    sf.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


def _get_username_from_state() -> Optional[str]:
    """从 streamlit session_state 获取当前用户名。"""
    try:
        import streamlit as st
        return st.session_state.get("username", "")
    except Exception:
        return None


# ── 消息持久化（兼容旧按日期的格式） ──

def get_today_history_file(username: str) -> Path:
    """兼容旧接口：获取今日历史文件路径。"""
    return _user_dir(username) / f"{datetime.now().strftime('%Y-%m-%d')}.json"


def load_history(username: str) -> list[dict]:
    """加载今日对话历史（兼容旧格式）。"""
    history_file = get_today_history_file(username)
    if history_file.exists():
        try:
            return json.loads(history_file.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError) as e:
            logger.warning("加载历史记录失败 %s: %s", history_file, e)
            return []
    return []


def load_session_history(username: str, session_id: str) -> list[dict]:
    """加载指定会话的对话历史。"""
    sf = _session_file(username, session_id)
    if sf.exists():
        try:
            return json.loads(sf.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError) as e:
            logger.warning("加载会话历史失败 %s: %s", sf, e)
            return []
    return []


def save_message(
    username: str,
    content: str,
    role: str = "user",
    timestamp: str = "",
    session_id: str = "",
    sources: list = None,
):
    """保存一条消息到当前会话。"""
    if not timestamp:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    msg = {"role": role, "content": content, "timestamp": timestamp}
    if sources:
        msg["sources"] = sources

    # 新格式：按会话存储
    if session_id:
        sf = _session_file(username, session_id)
        history = load_session_history(username, session_id)
        history.append(msg)
        sf.write_text(json.dumps(history, ensure_ascii=False, indent=2), encoding="utf-8")

    # 兼容旧格式：也存到按日期的文件
    old_file = get_today_history_file(username)
    old_history = []
    if old_file.exists():
        try:
            old_history = json.loads(old_file.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            old_history = []
    old_history.append(msg)
    old_file.write_text(json.dumps(old_history, ensure_ascii=False, indent=2), encoding="utf-8")


def load_all_history_dates(username: str) -> list[str]:
    """列出所有有历史记录的日期。"""
    user_dir = _user_dir(username)
    dates = []
    for f in user_dir.glob("*.json"):
        if f.name.startswith("_"):
            continue
        dates.append(f.stem)
    return sorted(dates, reverse=True)


def load_history_by_date(username: str, date_str: str) -> list[dict]:
    """加载指定日期的历史记录。"""
    history_file = _user_dir(username) / f"{date_str}.json"
    if history_file.exists():
        try:
            return json.loads(history_file.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            return []
    return []


# ── 导出功能 ──

def export_session_markdown(username: str, session_id: str) -> str:
    """将会话导出为 Markdown 文本。"""
    history = load_session_history(username, session_id)
    if not history:
        return "（空会话）"

    lines = [f"# 会话导出", f"", f"- 用户: {username}", f"- 时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", f"", "---", ""]
    for msg in history:
        role = "**▶ 提问**" if msg["role"] == "user" else "**◆ 回答**"
        ts = msg.get("timestamp", "")
        lines.append(f"{role} · {ts}")
        lines.append("")
        lines.append(msg["content"])
        lines.append("")
        lines.append("---")
        lines.append("")
    return "\n".join(lines)


def export_session_json(username: str, session_id: str) -> str:
    """将会话导出为 JSON 文本。"""
    history = load_session_history(username, session_id)
    return json.dumps(history, ensure_ascii=False, indent=2)


# ── 管理员功能 ──

def list_all_users_with_history() -> list[dict]:
    """管理员视图：列出所有有聊天记录的用户。

    Returns:
        [{username, session_count, last_active, total_messages}]
    """
    users = []
    if not CHAT_HISTORY_DIR.exists():
        return users

    for user_dir in sorted(CHAT_HISTORY_DIR.iterdir()):
        if not user_dir.is_dir():
            continue
        username = user_dir.name

        # 统计会话数
        sessions = list_sessions(username)
        session_count = len(sessions)

        # 统计消息总数
        total_messages = 0
        for sess in sessions:
            total_messages += sess.get("message_count", 0)

        # 最后活跃时间
        last_active = ""
        if sessions:
            last_active = sessions[0].get("updated_at", "")

        # 统计旧格式的日期文件
        date_files = list(user_dir.glob("*.json"))
        old_count = len([f for f in date_files if not f.name.startswith("_")])

        users.append({
            "username": username,
            "session_count": session_count,
            "total_messages": total_messages,
            "last_active": last_active[:10] if last_active else "未知",
            "old_files": old_count,
        })

    # 按最后活跃时间降序
    users.sort(key=lambda u: u.get("last_active", ""), reverse=True)
    return users


def load_user_history_for_admin(username: str) -> list[dict]:
    """管理员视图：加载指定用户的所有历史消息（合并会话和旧格式）。

    Returns:
        按时间排序的消息列表
    """
    all_messages = []

    # 加载新格式会话消息
    sessions = list_sessions(username)
    for sess in sessions:
        msgs = load_session_history(username, sess["id"])
        for msg in msgs:
            msg["_session_id"] = sess["id"]
            msg["_session_title"] = sess.get("title", "")
        all_messages.extend(msgs)

    # 加载旧格式日期文件
    user_dir = _user_dir(username)
    for f in sorted(user_dir.glob("*.json")):
        if f.name.startswith("_"):
            continue
        try:
            day_msgs = json.loads(f.read_text(encoding="utf-8"))
            if isinstance(day_msgs, list):
                for msg in day_msgs:
                    msg["_date"] = f.stem
                all_messages.extend(day_msgs)
        except (json.JSONDecodeError, OSError) as e:
            logger.warning("加载日期历史失败 %s: %s", f, e)

    # 按时间排序
    all_messages.sort(key=lambda m: m.get("timestamp", ""))
    return all_messages

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
    except Exception:
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
        except Exception:
            pass
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
        "title": title or f"会话 {len(sessions) + 1}",
        "created_at": now,
        "updated_at": now,
        "message_count": 0,
    })

    _save_sessions(username, sessions)
    logger.info("创建会话: %s -> %s", username, session_id)
    return session_id


def switch_session(session_id: str):
    """切换活跃会话（仅更新活跃标记）。"""
    username = _get_username_from_state()
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
        except Exception:
            pass
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
        except Exception:
            pass
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
        except Exception:
            return []
    return []


def load_session_history(username: str, session_id: str) -> list[dict]:
    """加载指定会话的对话历史。"""
    sf = _session_file(username, session_id)
    if sf.exists():
        try:
            return json.loads(sf.read_text(encoding="utf-8"))
        except Exception:
            return []
    return []


def save_message(
    username: str,
    content: str,
    role: str = "user",
    timestamp: str = "",
    session_id: str = "",
):
    """保存一条消息到当前会话。"""
    if not timestamp:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # 新格式：按会话存储
    if session_id:
        sf = _session_file(username, session_id)
        history = load_session_history(username, session_id)
        history.append({"role": role, "content": content, "timestamp": timestamp})
        sf.write_text(json.dumps(history, ensure_ascii=False, indent=2), encoding="utf-8")

    # 兼容旧格式：也存到按日期的文件
    old_file = get_today_history_file(username)
    old_history = []
    if old_file.exists():
        try:
            old_history = json.loads(old_file.read_text(encoding="utf-8"))
        except Exception:
            old_history = []
    old_history.append({"role": role, "content": content, "timestamp": timestamp})
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
        except Exception:
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

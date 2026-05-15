"""聊天记录服务测试。"""

import tempfile
import shutil
from pathlib import Path

import services.history as history


class TestSessionManagement:
    """会话管理测试。"""

    def setup_method(self):
        self._tmpdir = tempfile.mkdtemp()
        history.CHAT_HISTORY_DIR = Path(self._tmpdir)

    def teardown_method(self):
        shutil.rmtree(self._tmpdir, ignore_errors=True)

    def test_create_session(self):
        session_id = history.create_session("test_user")
        assert session_id
        assert len(session_id) == 12  # uuid4 hex[:12]

        sessions = history.list_sessions("test_user")
        assert len(sessions) == 1
        assert sessions[0]["id"] == session_id

    def test_list_sessions_empty(self):
        sessions = history.list_sessions("nonexistent_user")
        assert sessions == []

    def test_get_active_session_creates_default(self):
        session_id = history.get_active_session_id("new_user")
        assert session_id
        sessions = history.list_sessions("new_user")
        assert len(sessions) == 1

    def test_save_and_load_message(self):
        session_id = history.create_session("test_user", "测试会话")
        history.save_message("test_user", "你好", role="user",
                            session_id=session_id, timestamp="2026-01-01 12:00:00")
        history.save_message("test_user", "你好！有什么可以帮你的？", role="assistant",
                            session_id=session_id, timestamp="2026-01-01 12:00:01")

        msgs = history.load_session_history("test_user", session_id)
        assert len(msgs) == 2
        assert msgs[0]["role"] == "user"
        assert msgs[0]["content"] == "你好"
        assert msgs[1]["role"] == "assistant"

    def test_switch_session(self):
        session1 = history.create_session("test_user", "会话1")
        session2 = history.create_session("test_user", "会话2")

        history.switch_session(session2, username="test_user")
        active = history.get_active_session_id("test_user")
        assert active == session2


class TestExportFunctions:
    """导出功能测试。"""

    def setup_method(self):
        self._tmpdir = tempfile.mkdtemp()
        history.CHAT_HISTORY_DIR = Path(self._tmpdir)

    def teardown_method(self):
        shutil.rmtree(self._tmpdir, ignore_errors=True)

    def test_export_markdown_empty(self):
        result = history.export_session_markdown("user", "nonexistent")
        assert "空会话" in result

    def test_export_markdown_with_content(self):
        session_id = history.create_session("test_user")
        history.save_message("test_user", "问题内容", role="user",
                            session_id=session_id)
        history.save_message("test_user", "回答内容", role="assistant",
                            session_id=session_id)

        md = history.export_session_markdown("test_user", session_id)
        assert "▶ 提问" in md
        assert "◆ 回答" in md
        assert "问题内容" in md
        assert "回答内容" in md

    def test_export_json(self):
        session_id = history.create_session("test_user")
        history.save_message("test_user", "测试", role="user",
                            session_id=session_id)

        import json
        json_str = history.export_session_json("test_user", session_id)
        data = json.loads(json_str)
        assert len(data) == 1
        assert data[0]["content"] == "测试"

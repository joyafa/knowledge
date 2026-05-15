"""侧边栏模块。

使用 Streamlit 原生 st.sidebar，专业的导航体验。
"""

import streamlit as st
from datetime import datetime

from rag import __version__
from rag.config import get_config
from rag.vectorstore import VectorStore
from rag.loader import get_knowledge_files_meta
from ui import render_logo_img
from services.history import (
    load_all_history_dates,
    load_history_by_date,
    get_today_history_file,
    get_active_session_id,
    list_sessions,
    create_session,
    switch_session,
)
from services.knowledge_service import read_full_content


def render_sidebar(config):
    """渲染侧边栏。"""
    ui_cfg = config.ui
    username = st.session_state.get("username", "?")
    is_admin = username in config.admin_users

    with st.sidebar:
        # ── Logo 区域 ──
        st.markdown(f"""
        <div style="text-align:center; padding: 16px 0 8px 0;">
            {render_logo_img(width=72)}
            <div style="font-size:0.95em; font-weight:600; margin-top:8px;">{ui_cfg.title}</div>
            <div style="font-size:0.7em; color:#888; margin-top:2px;">v{__version__}</div>
        </div>
        """, unsafe_allow_html=True)

        st.divider()

        # ── 用户区 ──
        c1, c2 = st.columns([3, 1])
        with c1:
            admin_badge = " 🔰" if is_admin else ""
            st.markdown(f"**👤 {username}{admin_badge}**")
        with c2:
            current_theme = st.session_state.get("theme", ui_cfg.default_theme)
            theme_label = "☀️" if current_theme == "dark" else "🌙"
            if st.button(theme_label, help=f"切换到{'亮色' if current_theme == 'dark' else '暗色'}主题"):
                st.session_state.theme = "light" if current_theme == "dark" else "dark"
                st.rerun()

        # ── 导航 ──
        st.markdown("---")
        page = st.session_state.get("page", "chat")

        if st.button("💬 智能问答" if page != "chat" else "▸ 💬 智能问答",
                     use_container_width=True,
                     type="primary" if page == "chat" else "secondary"):
            st.session_state.page = "chat"
            st.rerun()

        if st.button("📊 仪表盘" if page != "dashboard" else "▸ 📊 仪表盘",
                     use_container_width=True,
                     type="primary" if page == "dashboard" else "secondary"):
            st.session_state.page = "dashboard"
            st.rerun()

        st.markdown("---")

        # ── 会话管理 ──
        st.caption("📋 会话")

        sessions = list_sessions(username)
        active_id = get_active_session_id(username)

        if st.button("＋ 新建会话", use_container_width=True):
            new_id = create_session(username)
            switch_session(new_id)
            st.session_state.messages = []
            st.session_state.pop("history_loaded", None)
            st.rerun()

        if sessions:
            for sess in sessions[:8]:
                is_active = sess["id"] == active_id
                label = f"{'▸ ' if is_active else '  '}{sess['title'][:20]}"
                if st.button(label, key=f"sess_{sess['id']}", use_container_width=True,
                            type="primary" if is_active else "secondary"):
                    if not is_active:
                        switch_session(sess["id"])
                        st.session_state.messages = []
                        st.session_state.pop("history_loaded", None)
                        st.rerun()

        st.markdown("---")

        # ── 知识库文档 ──
        st.caption("📚 知识库文档")

        with st.expander("文档列表", expanded=False):
            files = get_knowledge_files_meta(config.knowledge.docs_directory)
            if not files:
                st.info("暂无文档")
            else:
                search_query = st.text_input("搜索", placeholder="关键词...", key="sidebar_doc_search", label_visibility="collapsed")
                filtered = files
                if search_query:
                    filtered = [f for f in files
                               if search_query.lower() in f["title"].lower()
                               or search_query.lower() in f["path"].lower()]
                st.caption(f"{len(filtered)}/{len(files)} 篇")

                for f in filtered[:80]:
                    size_label = f"{f['size'] // 1024}KB" if f['size'] >= 1024 else f"{f['size']}B"
                    with st.expander(f"{f['icon']} {f['title'][:30]} ({size_label})"):
                        st.caption(f"`{f['path']}`")
                        content = read_full_content(config.knowledge.docs_directory, f["path"])
                        if content:
                            preview = content[:600]
                            if len(content) > 600:
                                preview += "\n\n..."
                            st.markdown(preview)

        # ── 历史记录 ──
        with st.expander("📅 历史记录", expanded=False):
            all_dates = load_all_history_dates(username)
            if all_dates:
                for date_str in all_dates[:10]:
                    label = date_str + (" · 今天" if date_str == datetime.now().strftime("%Y-%m-%d") else "")
                    with st.expander(label):
                        day_history = load_history_by_date(username, date_str)
                        if not isinstance(day_history, list):
                            day_history = []
                        for msg in day_history[-15:]:
                            role_icon = "▶" if msg["role"] == "user" else "◆"
                            st.caption(f"{role_icon} {msg.get('timestamp', '')}")
                            st.markdown(msg["content"][:150])
                            st.markdown("---")
            else:
                st.caption("暂无记录")

        st.markdown("---")

        # ── 系统状态 ──
        st.caption("⚙️ 系统")
        llm_cfg = config.llm
        st.markdown(f"**模型** `{llm_cfg.model}`")
        st.markdown(f"**接口** `{llm_cfg.api_base[:40]}...`")
        try:
            if st.session_state.get("chain_initialized"):
                vs = VectorStore.from_config()
                s = vs.get_stats()
                st.success(f"✅ 向量库已就绪 ({s['total_chunks']}块)")
            else:
                st.info("⏳ 检索引擎加载中...")
        except Exception:
            st.warning("⚠️ 向量库未就绪")

        # ── 操作按钮 ──
        st.markdown("---")

        if st.button("🧹 清除会话", use_container_width=True):
            st.session_state.messages = []
            st.session_state.pop("history_loaded", None)
            hf = get_today_history_file(username)
            if hf.exists():
                hf.write_text("{}", encoding="utf-8")
            st.rerun()

        if st.button("🚪 断开连接", use_container_width=True):
            # 安全退出：保留 chain 和 theme，清除用户状态
            preserved = {}
            for k in ("chain", "chain_initialized", "theme"):
                if k in st.session_state:
                    preserved[k] = st.session_state[k]
            st.session_state.clear()
            for k, v in preserved.items():
                st.session_state[k] = v
            st.rerun()

        # ── 落款 ──
        if ui_cfg.company_name:
            copyright_text = f"© {datetime.now().year} {ui_cfg.company_name}"
            if ui_cfg.company_url:
                copyright_text += f" | {ui_cfg.company_url}"
            st.markdown(f"""
            <div style="text-align:center; padding:20px 0 8px 0; color:#888; font-size:0.7em;">
                {copyright_text}
            </div>
            """, unsafe_allow_html=True)

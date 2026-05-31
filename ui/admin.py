"""管理员面板模块。

提供用户管理、密码重置、查看所有用户聊天记录等功能。
仅管理员可访问。
"""

from datetime import datetime

import streamlit as st

from rag import __version__
from ui import render_logo_img


def render_admin_panel(config):
    """渲染管理员面板（全功能）。"""
    ui_cfg = config.ui
    auth_cfg = config.auth
    username = st.session_state.get("username", "?")

    # ── 页面头 ──
    st.markdown(f"""
    <div style="padding: 12px 0 4px 0;">
        {render_logo_img(width=48)}
        <span style="font-size:1.3em;font-weight:600;margin-left:8px;">{ui_cfg.title}</span>
        <span style="color:var(--text-secondary);font-size:0.8em;margin-left:16px;">🔰 管理员控制台</span>
        <span style="color:var(--text-muted);font-size:0.75em;margin-left:12px;">v{__version__}</span>
    </div>
    """, unsafe_allow_html=True)

    st.divider()

    # ── 功能 Tab ──
    tab_names = ["👥 用户管理", "📋 聊天记录", "📊 系统概览"]
    tabs = st.tabs(tab_names)

    with tabs[0]:
        _render_user_management(auth_cfg, username)

    with tabs[1]:
        _render_history_browser()

    with tabs[2]:
        _render_system_overview(config)


# ════════════════════════════════════════════
# Tab 1: 用户管理
# ════════════════════════════════════════════

def _render_user_management(auth_cfg, current_admin):
    """渲染用户管理界面：用户列表、密码重置、删除。"""
    from services.auth import get_user_manager

    um = get_user_manager(auth_cfg.users_file)
    users = um.list_users()

    # ── 统计卡片 ──
    c1, c2, c3 = st.columns(3)
    c1.metric("总用户数", len(users))
    admin_count = sum(1 for u in users if u["role"] == "admin")
    c2.metric("管理员", admin_count)
    c3.metric("普通用户", len(users) - admin_count)

    st.divider()

    if not users:
        st.info("暂无注册用户")
        return

    # ── 用户列表 ──
    st.markdown("### 用户列表")

    for i, user in enumerate(users):
        uname = user["username"]
        role = user["role"]
        created = user.get("created_at", "")[:10]
        is_current = uname == current_admin
        role_badge = "🔰 管理员" if role == "admin" else "👤 用户"

        with st.container():
            col_info, col_actions = st.columns([3, 2])

            with col_info:
                current_tag = " *(当前)*" if is_current else ""
                st.markdown(f"**{uname}**{current_tag} — {role_badge} — 注册于 {created}")

            with col_actions:
                btn_cols = st.columns([1, 1, 1])
                with btn_cols[0]:
                    if st.button("🔑 重置密码", key=f"reset_{uname}"):
                        st.session_state[f"reset_dialog_{uname}"] = True

                with btn_cols[1]:
                    if st.button("🗑 删除", key=f"del_{uname}", disabled=is_current):
                        st.session_state[f"delete_confirm_{uname}"] = True

            # ── 重置密码弹窗 ──
            if st.session_state.get(f"reset_dialog_{uname}"):
                _show_reset_password_dialog(um, uname, current_admin)

            # ── 删除确认弹窗 ──
            if st.session_state.get(f"delete_confirm_{uname}"):
                _show_delete_confirm(um, uname, current_admin)

            st.markdown("<hr style='margin:8px 0; opacity:0.3;'>", unsafe_allow_html=True)


def _show_reset_password_dialog(um, target_user: str, current_admin: str):
    """显示重置密码对话框。"""
    st.markdown(f"#### 🔑 重置密码：{target_user}")

    new_pwd = st.text_input(
        "新密码",
        type="password",
        placeholder="输入新密码（至少4个字符）",
        key=f"newpwd_{target_user}",
    )

    confirm_pwd = st.text_input(
        "确认密码",
        type="password",
        placeholder="再次输入新密码",
        key=f"confirmpwd_{target_user}",
    )

    c1, c2 = st.columns(2)
    with c1:
        if st.button("✅ 确认重置", key=f"confirm_reset_{target_user}", type="primary"):
            if not new_pwd:
                st.warning("请输入新密码")
            elif not confirm_pwd:
                st.warning("请再次输入密码确认")
            elif new_pwd != confirm_pwd:
                st.error("两次输入的密码不一致，请重新输入")
            else:
                success, msg = um.reset_password(target_user, new_pwd)
                if success:
                    st.success(msg)
                    st.session_state.pop(f"reset_dialog_{target_user}", None)
                    st.rerun()
                else:
                    st.error(msg)

    with c2:
        if st.button("取消", key=f"cancel_reset_{target_user}"):
            st.session_state.pop(f"reset_dialog_{target_user}", None)
            st.rerun()

    st.divider()


def _show_delete_confirm(um, target_user: str, current_admin: str):
    """显示删除确认对话框。"""
    st.markdown(f"#### ⚠️ 确认删除：{target_user}")

    st.warning(f"此操作将删除用户 **{target_user}** 的账户，无法恢复。")

    c1, c2 = st.columns(2)
    with c1:
        if st.button("✅ 确认删除", key=f"confirm_del_{target_user}", type="primary"):
            success, msg = um.delete_user(target_user)
            if success:
                st.success(msg)
                st.session_state.pop(f"delete_confirm_{target_user}", None)
                st.rerun()
            else:
                st.error(msg)

    with c2:
        if st.button("取消", key=f"cancel_del_{target_user}"):
            st.session_state.pop(f"delete_confirm_{target_user}", None)
            st.rerun()

    st.divider()


# ════════════════════════════════════════════
# Tab 2: 聊天记录浏览器
# ════════════════════════════════════════════

def _render_history_browser():
    """管理员查看所有用户的聊天记录。"""
    from services.history import list_all_users_with_history, load_user_history_for_admin

    st.markdown("### 📋 用户聊天记录")

    chat_users = list_all_users_with_history()

    if not chat_users:
        st.info("暂无用户聊天记录")
        return

    # ── 用户选择 ──
    user_options = [u["username"] for u in chat_users]
    selected_user = st.selectbox(
        "选择用户",
        options=user_options,
        key="admin_history_user",
    )

    if not selected_user:
        return

    # 找到选中用户的统计
    user_stats = next((u for u in chat_users if u["username"] == selected_user), None)

    if user_stats:
        c1, c2, c3 = st.columns(3)
        c1.metric("会话数", user_stats["session_count"])
        c2.metric("消息数", user_stats["total_messages"])
        c3.metric("最后活跃", user_stats["last_active"])

    st.divider()

    # ── 加载并显示消息 ──
    with st.spinner(f"加载 {selected_user} 的聊天记录..."):
        messages = load_user_history_for_admin(selected_user)

    if not messages:
        st.info(f"{selected_user} 暂无聊天记录")
        return

    st.caption(f"共 {len(messages)} 条消息")

    # 分页显示
    page_size = 20
    total_pages = (len(messages) + page_size - 1) // page_size

    page_key = f"history_page_{selected_user}"
    if page_key not in st.session_state:
        st.session_state[page_key] = 1

    col_pg1, col_pg2, col_pg3 = st.columns([1, 2, 1])
    with col_pg2:
        page = st.number_input(
            "页码",
            min_value=1,
            max_value=max(1, total_pages),
            value=st.session_state[page_key],
            key=f"pg_input_{selected_user}",
            label_visibility="collapsed",
        )
        st.session_state[page_key] = page

    start = (page - 1) * page_size
    end = start + page_size
    page_messages = messages[start:end]

    st.caption(f"第 {page}/{total_pages} 页 · 显示 {start+1}-{min(end, len(messages))} 条")

    # ── 消息展示 ──
    for i, msg in enumerate(page_messages):
        role = msg.get("role", "user")
        content = msg.get("content", "")
        ts = msg.get("timestamp", "")
        session_title = msg.get("_session_title", "")
        date_tag = msg.get("_date", "")

        # 用户消息和助手消息不同样式
        if role == "user":
            icon = "▶"
            color = "#4fc3f7"
        elif role == "assistant":
            icon = "◆"
            color = "#81c784"
        else:
            icon = "●"
            color = "var(--text-muted)"

        with st.container():
            st.markdown(
                f"<span style='color:{color};'>{icon}</span> "
                f"<small style='color:var(--text-secondary);'>{ts}</small>",
                unsafe_allow_html=True,
            )

            # 显示来源信息
            tags = []
            if session_title:
                tags.append(f"📋 {session_title}")
            if date_tag:
                tags.append(f"📅 {date_tag}")
            if tags:
                st.caption(" · ".join(tags))

            st.markdown(content[:1000])
            if len(content) > 1000:
                st.caption("... (内容已截断)")

            st.markdown("<hr style='margin:4px 0; opacity:0.2;'>", unsafe_allow_html=True)

    # 导出按钮
    st.divider()
    export_data = "\n\n---\n\n".join(
        f"[{m.get('timestamp', '')}] {'▶' if m.get('role') == 'user' else '◆'} "
        f"{m.get('content', '')}"
        for m in messages
    )
    st.download_button(
        label=f"📥 导出 {selected_user} 的全部记录 (TXT)",
        data=export_data,
        file_name=f"history_{selected_user}_{datetime.now().strftime('%Y%m%d')}.txt",
        mime="text/plain",
    )


# ════════════════════════════════════════════
# Tab 3: 系统概览
# ════════════════════════════════════════════

def _render_system_overview(config):
    """系统信息概览。"""
    st.markdown("### 📊 系统概览")

    from services.auth import get_user_manager
    from services.history import list_all_users_with_history

    # ── 用户统计 ──
    um = get_user_manager(config.auth.users_file)
    all_users = um.list_users()
    chat_users = list_all_users_with_history()

    c1, c2, c3 = st.columns(3)
    c1.metric("注册用户", len(all_users))
    c2.metric("有聊天记录的用户", len(chat_users))
    c3.metric("活跃用户(7天)", _count_active_users(chat_users, 7))

    st.divider()

    # ── 向量库状态 ──
    st.markdown("### 向量库状态")
    try:
        from rag.vectorstore import VectorStore
        vs = VectorStore.from_config()
        s = vs.get_stats()
        st.success("✅ 向量库正常")
        c1, c2, c3 = st.columns(3)
        c1.metric("文档块", s["total_chunks"])
        c2.metric("文件数", s["total_files"])
        c3.metric("集合名", s.get("collection_name", config.vectorstore.collection_name))
    except Exception as e:
        st.warning(f"向量库状态获取失败: {e}")

    st.divider()

    # ── LLM 配置 ──
    st.markdown("### LLM 配置")
    st.markdown(f"- **模型**: `{config.llm.model}`")
    st.markdown(f"- **接口**: `{config.llm.api_base}`")
    st.markdown(f"- **上下文窗口**: {config.llm.context_window}")
    st.markdown(f"- **Embedding**: `{config.embedding.model}`")
    st.markdown(f"- **Reranker**: `{config.reranker.model}`")

    st.divider()

    # ── 配置信息 ──
    st.markdown("### 系统配置")
    st.markdown(f"- **版本**: v{__version__}")
    st.markdown(f"- **数据目录**: `{config.vectorstore.persist_directory}`")
    st.markdown(f"- **知识库目录**: `{config.knowledge.docs_directory}`")
    st.markdown(f"- **分块大小/重叠**: {config.knowledge.chunk_size}/{config.knowledge.chunk_overlap}")
    st.markdown(f"- **检索 Top-K**: {config.vectorstore.top_k}")
    st.markdown(f"- **速率限制**: {'启用' if config.rate_limit.enabled else '禁用'} ({config.rate_limit.max_requests_per_minute}次/分)")
    st.markdown(f"- **认证**: {'启用' if config.auth.enabled else '禁用'} (最短密码 {config.auth.min_password_length}字符)")


def _count_active_users(chat_users: list[dict], days: int) -> int:
    """统计最近 N 天活跃的用户数。"""
    from datetime import timedelta
    cutoff = (datetime.now() - timedelta(days=days)).strftime("%Y-%m-%d")
    count = 0
    for u in chat_users:
        last = u.get("last_active", "")
        if last and last >= cutoff:
            count += 1
    return count

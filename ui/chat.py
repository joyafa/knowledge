"""对话面板模块。"""

import time
from datetime import datetime

import streamlit as st

from rag.config import get_config
from rag.logging_config import audit_log
from rag.preload import is_done, get_error as preload_error, get_error_detail, get_chain as preload_get_chain, reset as preload_reset, start as preload_start
from services.history import (
    load_session_history,
    save_message,
    get_active_session_id,
    update_session_title,
)


def render_chat_panel():
    """渲染对话面板。"""
    config = get_config()
    username = st.session_state.get("username", "anonymous")

    # 等待 chain 加载
    if not st.session_state.get("chain_initialized"):
        if not is_done():
            st.markdown("""
            <div style="display:flex;flex-direction:column;align-items:center;justify-content:center;padding:100px 0;">
                <div style="font-size:2.5em;margin-bottom:16px;">⏳</div>
                <div style="font-size:1.1em;font-weight:500;">系统初始化中，正在加载检索引擎...</div>
                <div style="font-size:0.8em;color:var(--text-muted);margin-top:8px;">首次加载约需 15 秒，请稍候</div>
            </div>
            """, unsafe_allow_html=True)
            time.sleep(1.5)
            st.rerun()
        else:
            # 线程已完成，再检查一次 chain（防止竞态：线程在 init_session_state
            # 之后、本检查之前恰好完成，此时 is_done 为 True 但 chain 已就绪）
            chain = preload_get_chain()
            if chain is not None:
                st.session_state.chain = chain
                st.session_state.chain_initialized = True
                st.rerun()
            err = preload_error()
            err_detail = get_error_detail()
            st.error(f"❌ 系统初始化失败: {err}")
            st.caption("请检查 config.yaml 中的 LLM API 配置和网络连接")
            with st.expander("📋 错误详情", expanded=True):
                st.code(err_detail or "（无额外错误信息）", language="text")
            if st.button("🔄 重试加载"):
                preload_reset()
                preload_start()
                st.rerun()
            return
        return

    # 加载持久化会话历史
    if "history_loaded" not in st.session_state:
        session_id = get_active_session_id(username)
        session_history = load_session_history(username, session_id)
        for msg in session_history:
            st.session_state.messages.append({
                "role": msg["role"],
                "content": msg["content"],
                "timestamp": msg.get("timestamp", ""),
                "sources": msg.get("sources", []),
            })
        st.session_state.history_loaded = True

    # 渲染消息列表
    for i, message in enumerate(st.session_state.messages):
        with st.chat_message(message["role"]):
            ts = message.get("timestamp", "")
            if ts:
                st.caption(ts)
            st.markdown(message["content"])

            # 渲染参考来源（可点击展开查看）
            if message["role"] == "assistant" and message.get("sources"):
                _render_message_sources(message["sources"], i, config)

            if message["role"] == "assistant" and message.get("content", "").strip():
                _render_feedback(i, username, message)

    # 输入框
    if prompt := st.chat_input("输入查询指令..."):
        _process_query(prompt, username, config)


def _render_feedback(i: int, username: str, message: dict):
    fb_key = f"feedback_{i}"
    if fb_key not in st.session_state:
        st.session_state[fb_key] = None
    c1, c2, c3 = st.columns([0.5, 0.5, 9])
    with c1:
        if st.button("👍", key=f"up_{i}", help="有帮助"):
            if st.session_state[fb_key] != "up":
                st.session_state[fb_key] = "up"
                audit_log(username, "feedback", details="positive",
                          query=message.get("content", "")[:100])
                st.toast("👍 感谢反馈！", icon="✅")
    with c2:
        if st.button("👎", key=f"down_{i}", help="无帮助"):
            if st.session_state[fb_key] != "down":
                st.session_state[fb_key] = "down"
                audit_log(username, "feedback", details="negative",
                          query=message.get("content", "")[:100])
                st.toast("👎 已记录", icon="⚠️")


def _process_query(prompt: str, username: str, config):
    now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    rate_cfg = config.rate_limit

    # 防重复：如果最后一条消息就是当前 prompt，跳过
    if st.session_state.messages and st.session_state.messages[-1].get("content") == prompt and st.session_state.messages[-1].get("role") == "user":
        return

    if len(prompt) > rate_cfg.max_input_length:
        with st.chat_message("assistant"):
            st.error(f"输入过长（最大 {rate_cfg.max_input_length} 字符）")
        return

    if rate_cfg.enabled:
        from services.rate_limiter import check_rate_limit
        allowed, msg = check_rate_limit(username, rate_cfg.max_requests_per_minute)
        if not allowed:
            with st.chat_message("assistant"):
                st.warning(msg)
            return

    st.session_state.messages.append({"role": "user", "content": prompt, "timestamp": now_str})
    with st.chat_message("user"):
        st.caption(now_str)
        st.markdown(prompt)
    session_id = get_active_session_id(username)
    save_message(username, prompt, role="user", timestamp=now_str, session_id=session_id)

    # 首次提问时自动以问题内容命名会话
    session_msgs = load_session_history(username, session_id)
    user_msg_count = sum(1 for m in session_msgs if m.get("role") == "user")
    if user_msg_count == 1:
        short_title = prompt.strip()[:25] + ("..." if len(prompt.strip()) > 25 else "")
        update_session_title(username, session_id, short_title)

    if not st.session_state.get("chain_initialized"):
        with st.chat_message("assistant"):
            st.error("系统初始化失败，请刷新页面重试。")
        return

    conversation_history = [
        {"role": m["role"], "content": m["content"]}
        for m in st.session_state.messages[:-1]
        if m.get("role") in ("user", "assistant")
    ]
    max_turns = getattr(config, 'max_conversation_turns', 10)
    conversation_history = conversation_history[-(max_turns * 2):]

    with st.chat_message("assistant"):
        answer_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        full_response = ""
        placeholder = st.empty()
        sources_info = []

        try:
            for event in st.session_state.chain.query_stream_with_status(
                prompt,
                history=conversation_history,
                username=username,
            ):
                status = event["status"]
                if status == "searching":
                    placeholder.info("🔍 正在检索知识库...")
                elif status == "generating":
                    chunk = event.get("chunk", "")
                    if chunk:
                        full_response += chunk
                        placeholder.markdown(full_response)
                elif status == "done":
                    sources_info = event.get("sources", [])
                    if not full_response:
                        full_response = f"知识库中暂无与「{prompt[:50]}」相关的内容。\n\n请确认文档已入库，或尝试换一种问法。"
                        placeholder.info(full_response)
                    else:
                        placeholder.markdown(full_response)
                elif status == "error":
                    full_response = f"系统异常: {event.get('message', '未知错误')}"
                    placeholder.error(full_response)
        except Exception as e:
            full_response = f"生成回答时出错: {str(e)}"
            placeholder.error(full_response)

    st.session_state.messages.append({
        "role": "assistant", "content": full_response, "timestamp": answer_time,
        "sources": sources_info,
    })
    save_message(username, full_response, role="assistant", timestamp=answer_time, session_id=session_id, sources=sources_info)

    # 立即渲染参考来源（首次响应时消息循环还未包含本条消息）
    if sources_info:
        msg_index = len(st.session_state.messages) - 1
        _render_message_sources(sources_info, msg_index, config)


def _render_message_sources(sources: list, msg_index: int, config):
    """渲染参考来源列表（仅显示来源信息，不展开查看文件内容）。

    Args:
        sources: [{"source": str, "title": str}, ...]
        msg_index: 消息索引（用于生成唯一 key）
        config: 应用配置
    """
    if not sources:
        return

    st.markdown("**📖 参考来源：**")

    for j, s in enumerate(sources):
        source_path = s["source"]
        title = s.get("title", "")
        display_name = title if title else source_path
        st.caption(f"📄 {display_name}  `{source_path}`")

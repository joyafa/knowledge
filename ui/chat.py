"""对话面板模块。"""

import time
from datetime import datetime

import streamlit as st

from rag.config import get_config
from rag.logging_config import audit_log
from services.history import (
    load_session_history,
    save_message,
    get_active_session_id,
)


def render_chat_panel():
    """渲染对话面板。"""
    config = get_config()
    username = st.session_state.get("username", "anonymous")

    # 等待 chain 加载
    if not st.session_state.get("chain_initialized"):
        if not _preload_state_done():
            st.markdown("""
            <div style="display:flex; flex-direction:column; align-items:center; justify-content:center; padding:100px 0;">
                <div style="font-size:2.5em; margin-bottom:16px;">⏳</div>
                <div style="font-size:1.1em; font-weight:500; color:#888;">系统初始化中，正在加载检索引擎...</div>
                <div style="font-size:0.8em; color:#aaa; margin-top:8px;">首次加载约需 15 秒，请稍候</div>
            </div>
            """, unsafe_allow_html=True)
            time.sleep(1.5)
            st.rerun()
        else:
            st.error(f"系统初始化失败: {_preload_state_error()}")
            if st.button("🔄 重试"):
                _reload_chain()
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
            })
        st.session_state.history_loaded = True

    # 渲染消息列表
    for i, message in enumerate(st.session_state.messages):
        with st.chat_message(message["role"]):
            ts = message.get("timestamp", "")
            if ts:
                st.caption(ts)
            st.markdown(message["content"])

            # 反馈按钮（仅对助手消息）
            if message["role"] == "assistant" and message.get("content", "").strip():
                _render_feedback(i, username, message)

    # 输入框
    if prompt := st.chat_input("输入查询指令..."):
        _process_query(prompt, username, config)


def _render_feedback(i: int, username: str, message: dict):
    """渲染反馈按钮。"""
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
    """处理用户查询。"""
    now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    rate_cfg = config.rate_limit

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

    # 显示用户消息
    with st.chat_message("user"):
        st.caption(now_str)
        st.markdown(prompt)

    st.session_state.messages.append({"role": "user", "content": prompt, "timestamp": now_str})
    session_id = get_active_session_id(username)
    save_message(username, prompt, role="user", timestamp=now_str, session_id=session_id)

    if not st.session_state.get("chain_initialized"):
        with st.chat_message("assistant"):
            st.error("系统初始化失败，请刷新页面重试。")
        return

    # 构建对话历史
    conversation_history = [
        {"role": m["role"], "content": m["content"]}
        for m in st.session_state.messages[:-1]
        if m.get("role") in ("user", "assistant")
    ]
    max_turns = getattr(config, 'max_conversation_turns', 10)
    conversation_history = conversation_history[-(max_turns * 2):]

    # 流式生成
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
                        full_response = "知识库中暂无匹配内容，请确认文档已入库。"
                        placeholder.warning(full_response)
                    else:
                        if sources_info:
                            src = "\n\n---\n**📖 参考来源：**\n"
                            for s in sources_info:
                                src += f"- `{s['source']}`"
                                if s.get("title"):
                                    src += f"（{s['title']}）"
                                src += "\n"
                            full_response += src
                        placeholder.markdown(full_response)
                elif status == "error":
                    full_response = f"系统异常: {event.get('message', '未知错误')}"
                    placeholder.error(full_response)
        except Exception as e:
            full_response = f"生成回答时出错: {str(e)}"
            placeholder.error(full_response)

    st.session_state.messages.append({
        "role": "assistant", "content": full_response, "timestamp": answer_time,
    })
    save_message(username, full_response, role="assistant", timestamp=answer_time, session_id=session_id)


# ── 预加载桥接 ──

def _preload_state_done() -> bool:
    """检查预加载是否完成。"""
    import app
    return app._preload_state.get("done", False)


def _preload_state_error() -> str:
    """获取预加载错误信息。"""
    import app
    return app._preload_state.get("error", "未知错误")


def _reload_chain():
    """强制重新加载 chain。"""
    import app
    app._preload_state["chain"] = None
    app._preload_state["done"] = False
    app._preload_state["error"] = None
    import threading
    t = threading.Thread(target=app._preload_chain, daemon=True)
    t.start()
    if "chain" in st.session_state:
        del st.session_state["chain"]
    if "chain_initialized" in st.session_state:
        del st.session_state["chain_initialized"]

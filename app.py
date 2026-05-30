"""API 智能助手 — Streamlit Web 界面。

架构：ui/（界面组件） + services/（业务逻辑） + rag/（检索引擎）
"""

import os
import sys
from datetime import datetime
from pathlib import Path

# ChromaDB: 禁用遥测，避免 posthog 版本不兼容导致 capture() 参数错误
os.environ.setdefault("CHROMA_TELEMETRY", "False")
os.environ.setdefault("ANONYMIZED_TELEMETRY", "False")
# 使用国内 HuggingFace 镜像
os.environ.setdefault("HF_ENDPOINT", "https://hf-mirror.com")

import streamlit as st

sys.path.insert(0, str(Path(__file__).resolve().parent))

from rag.config import get_config
from rag.logging_config import setup_logging
from rag.preload import start as start_preload, is_done, get_chain


def init_session_state():
    """初始化 session_state。"""
    if "theme" not in st.session_state:
        st.session_state.theme = get_config().ui.default_theme
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "page" not in st.session_state:
        st.session_state.page = "chat"

    # 启动后台预加载（幂等）
    start_preload()

    # 从预加载获取 chain
    if "chain" not in st.session_state:
        chain = get_chain()
        if chain is not None:
            st.session_state.chain = chain
            st.session_state.chain_initialized = True


def do_logout():
    """安全退出：只清除用户相关状态，保留 chain 和 theme。"""
    preserved = {}
    for key in ("chain", "chain_initialized", "theme"):
        if key in st.session_state:
            preserved[key] = st.session_state[key]
    st.session_state.clear()
    for key, val in preserved.items():
        st.session_state[key] = val


def main():
    config = get_config()
    ui_cfg = config.ui

    # 浏览器标签页图标：优先使用 logo.png，回退到文字
    _logo_path = Path(__file__).resolve().parent / "logo.png"
    _page_icon = str(_logo_path) if _logo_path.exists() else ui_cfg.logo_text

    st.set_page_config(
        page_title=ui_cfg.title,
        page_icon=_page_icon,
        layout="wide",
        initial_sidebar_state="expanded",
    )

    from ui.theme import apply_theme
    apply_theme(st.session_state.get("theme", ui_cfg.default_theme))

    setup_logging()
    init_session_state()

    username = st.session_state.get("username", "")

    if not username:
        from ui.login import render_login_screen
        render_login_screen(config)
        return

    from ui.sidebar import render_sidebar
    render_sidebar(config)

    page = st.session_state.get("page", "chat")
    if page == "dashboard":
        _render_dashboard()
    else:
        _render_chat_page(config)


def _render_chat_page(config):
    ui_cfg = config.ui
    from ui import render_logo_img
    from rag import __version__
    st.markdown(f"""
    <div style="padding: 12px 0 4px 0;">
        {render_logo_img(width=48)}
        <span style="font-size:1.3em;font-weight:600;margin-left:8px;">{ui_cfg.title}</span>
        <span style="color:#888;font-size:0.8em;margin-left:16px;">{ui_cfg.subtitle}</span>
        <span style="color:#aaa;font-size:0.75em;margin-left:12px;">v{__version__}</span>
    </div>
    """, unsafe_allow_html=True)

    from ui.chat import render_chat_panel
    render_chat_panel()


def _render_dashboard():
    from services.analytics import get_dashboard_stats
    config = get_config()
    username = st.session_state.get("username", "")
    is_admin = username in config.admin_users

    # 顶栏：返回 + 管理员切换
    col_back, col_toggle = st.columns([1, 5])
    with col_back:
        if st.button("← 返回对话"):
            st.session_state.page = "chat"
            st.rerun()
    view_global = False
    if is_admin:
        with col_toggle:
            view_global = st.checkbox("查看全局数据（所有用户）", key="dashboard_global")

    # 根据视图加载数据
    filter_user = None if view_global else username
    with st.spinner("正在加载统计数据..."):
        stats = get_dashboard_stats(days=7, username=filter_user)

    view_label = "全局仪表盘" if view_global else "我的仪表盘"
    view_desc = "所有用户" if view_global else username
    st.markdown(f"## 📊 {view_label}")
    st.caption(f"查询统计 · {view_desc}")

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("7天查询量", stats["total_queries"])
    c2.metric("活跃用户" if view_global else "平均结果数", stats.get("unique_users", 0) if view_global else stats["avg_result_count"])
    c3.metric("零结果查询", stats["no_result_count"])
    c4.metric("平均延迟", f"{stats['avg_latency_ms']}ms")

    c5, c6 = st.columns(2)
    c5.metric("👍 好评", stats["total_feedback_positive"])
    c6.metric("👎 差评", stats["total_feedback_negative"])

    st.divider()
    st.markdown("### 日查询趋势")
    if stats["daily_queries"]:
        for date, count in stats["daily_queries"].items():
            bar = "█" * min(count, 50)
            st.markdown(f"`{date}` {bar} **{count}**")
    else:
        st.caption("暂无数据")

    st.divider()
    a1, a2 = st.columns(2)
    with a1:
        label = "热门查询 Top 10" if view_global else "我的热门查询 Top 10"
        st.markdown(f"### {label}")
        for item in stats.get("top_queries", []):
            st.markdown(f"- `{item['query']}` · **{item['count']}**次")
    with a2:
        st.markdown("### 知识库状态")
        try:
            from rag.vectorstore import VectorStore
            vs = VectorStore.from_config()
            s = vs.get_stats()
            st.success("✅ 向量库正常")
            st.markdown(f"- 文档块: **{s['total_chunks']}**")
            st.markdown(f"- 文件数: **{s['total_files']}**")
            st.markdown(f"- LLM: `{config.llm.model}`")
            st.markdown(f"- Embedding: `{config.embedding.model}`")
        except Exception as e:
            st.warning(f"向量库状态获取失败: {e}")

    st.divider()
    st.markdown("### 📥 导出")
    from services.history import export_session_markdown, get_active_session_id
    session_id = get_active_session_id(username)
    md_content = export_session_markdown(username, session_id)
    st.download_button(
        label="📄 下载当前会话 Markdown",
        data=md_content,
        file_name=f"chat_export_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md",
        mime="text/markdown",
    )


if __name__ == "__main__":
    main()

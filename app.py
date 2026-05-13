"""API 智能助手 — Streamlit Web 界面。

架构：ui/（界面组件） + services/（业务逻辑） + rag/（检索引擎）
"""

import os
import sys
import threading
from datetime import datetime
from pathlib import Path

import streamlit as st

sys.path.insert(0, str(Path(__file__).resolve().parent))

from rag.config import get_config
from rag.logging_config import setup_logging

# 使用国内 HuggingFace 镜像
os.environ.setdefault("HF_ENDPOINT", "https://hf-mirror.com")

# ── 后台预加载（使用可变容器避免 Streamlit rerun 重置） ──
_preload_state: dict = {"chain": None, "error": None, "done": False}


def _preload_chain():
    """后台线程：预加载 RAGChain（主要是 embedding 模型）。"""
    try:
        from rag.chain import RAGChain
        chain = RAGChain.from_config()
        _preload_state["chain"] = chain
    except Exception as e:
        _preload_state["error"] = str(e)
    finally:
        _preload_state["done"] = True


def init_session_state():
    """初始化 session_state。"""
    # 主题
    if "theme" not in st.session_state:
        st.session_state.theme = get_config().ui.default_theme

    # 消息
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # 页面
    if "page" not in st.session_state:
        st.session_state.page = "chat"

    # 后台预加载（只启动一次）
    if not _preload_state.get("started"):
        _preload_state["started"] = True
        t = threading.Thread(target=_preload_chain, daemon=True)
        t.start()

    # 从预加载获取 chain
    if "chain" not in st.session_state and _preload_state["chain"] is not None:
        st.session_state.chain = _preload_state["chain"]
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

    st.set_page_config(
        page_title=ui_cfg.title,
        page_icon=ui_cfg.logo_text,
        layout="wide",
        initial_sidebar_state="expanded",
    )

    # 应用主题
    from ui.theme import apply_theme
    apply_theme(st.session_state.get("theme", ui_cfg.default_theme))

    setup_logging()
    init_session_state()

    username = st.session_state.get("username", "")

    # 未登录
    if not username:
        from ui.login import render_login, render_login_screen
        render_login_screen(config)
        return

    # 已登录 — 侧边栏 + 主区域
    from ui.sidebar import render_sidebar
    render_sidebar(config)

    # 主区域
    page = st.session_state.get("page", "chat")

    if page == "dashboard":
        _render_dashboard()
    else:
        _render_chat_page(config)


def _render_chat_page(config):
    """渲染对话页面。"""
    ui_cfg = config.ui

    # 页面头部
    st.markdown(f"""
    <div style="padding: 12px 0 4px 0;">
        <span style="font-size: 1.6em; font-weight: 700;">{ui_cfg.logo_text}</span>
        <span style="font-size: 1.3em; font-weight: 600; margin-left: 8px;">{ui_cfg.title}</span>
        <span style="color: #888; font-size: 0.8em; margin-left: 16px;">{ui_cfg.subtitle}</span>
    </div>
    """, unsafe_allow_html=True)

    from ui.chat import render_chat_panel
    render_chat_panel()


def _render_dashboard():
    """渲染仪表盘页面。"""
    from services.analytics import get_dashboard_stats
    config = get_config()

    if st.button("← 返回对话"):
        st.session_state.page = "chat"
        st.rerun()

    st.markdown("## 📊 系统仪表盘")
    st.caption("查询统计 · 用户活跃度 · 知识库状态")

    with st.spinner("正在加载统计数据..."):
        stats = get_dashboard_stats(days=7)

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("7天查询量", stats["total_queries"])
    col2.metric("活跃用户", stats["unique_users"])
    col3.metric("零结果查询", stats["no_result_count"])
    col4.metric("平均延迟", f"{stats['avg_latency_ms']}ms")

    col5, col6 = st.columns(2)
    col5.metric("👍 好评", stats["total_feedback_positive"])
    col6.metric("👎 差评", stats["total_feedback_negative"])

    st.divider()
    st.markdown("### 日查询趋势")
    if stats["daily_queries"]:
        for date, count in stats["daily_queries"].items():
            bar = "█" * min(count, 50)
            st.markdown(f"`{date}` {bar} **{count}**")
    else:
        st.caption("暂无数据")

    st.divider()
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("### 热门查询 Top 10")
        for item in stats.get("top_queries", []):
            st.markdown(f"- `{item['query']}` · **{item['count']}**次")
    with c2:
        st.markdown("### 知识库状态")
        try:
            from rag.vectorstore import VectorStore
            vs = VectorStore.from_config()
            s = vs.get_stats()
            st.success("✅ 向量库正常")
            st.markdown(f"- **文档块**: {s['total_chunks']}")
            st.markdown(f"- **文件数**: {s['total_files']}")
            st.markdown(f"- **LLM**: `{config.llm.model}`")
            st.markdown(f"- **Embedding**: `{config.embedding.model}`")
        except Exception as e:
            st.warning(f"向量库状态获取失败: {e}")

    st.divider()
    st.markdown("### 📥 导出")
    from services.history import export_session_markdown, get_active_session_id
    username = st.session_state.get("username", "")
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

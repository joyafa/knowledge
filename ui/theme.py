"""主题模块 — 企业级暗色 & 亮色双主题。

通过 config.yaml 的 ui.default_theme 和运行时切换控制。
"""

import streamlit as st

# ── 暗色主题（专业企业暗色） ──

DARK_THEME = """
<style>
/* ── 语义化颜色变量（供内联 HTML 通过 var() 引用） ── */
.stApp {
    --text-primary: #e2e8f0;
    --text-secondary: #94a3b8;
    --text-muted: #64748b;
    --bg-card: rgba(30, 30, 50, 0.7);
    --border-color: rgba(99, 102, 241, 0.15);
}

/* 全局基底 */
.stApp {
    background: linear-gradient(135deg, #0f0f1a 0%, #1a1a2e 50%, #16213e 100%) !important;
    color: #e2e8f0 !important;
}

/* 侧边栏 */
[data-testid="stSidebar"] {
    background: rgba(15, 15, 30, 0.95) !important;
    border-right: 1px solid rgba(99, 102, 241, 0.15) !important;
    backdrop-filter: blur(12px) !important;
}

/* 标题 */
h1, h2, h3 { color: #a78bfa !important; font-weight: 600 !important; }
h4, h5, h6 { color: #818cf8 !important; }

/* 聊天气泡 */
.stChatMessage {
    background: rgba(30, 30, 50, 0.7) !important;
    border: 1px solid rgba(99, 102, 241, 0.15) !important;
    border-radius: 12px !important;
    padding: 16px !important;
    backdrop-filter: blur(8px) !important;
}
.stChatMessage[data-testid="stChatMessage-user"] {
    border-left: 3px solid #a78bfa !important;
    background: rgba(99, 102, 241, 0.08) !important;
}
.stChatMessage[data-testid="stChatMessage-assistant"] {
    border-left: 3px solid #06b6d4 !important;
    background: rgba(6, 182, 212, 0.06) !important;
}

/* 输入框 */
.stChatInput textarea {
    background: rgba(30, 30, 50, 0.8) !important;
    border: 1px solid rgba(99, 102, 241, 0.25) !important;
    border-radius: 12px !important;
    color: #e2e8f0 !important;
    padding: 12px 16px !important;
}
.stChatInput textarea::placeholder { color: #64748b !important; }

/* 按钮 */
.stButton > button {
    border-radius: 8px !important;
    font-weight: 500 !important;
    transition: all 0.2s !important;
    border: 1px solid rgba(99, 102, 241, 0.3) !important;
    background: rgba(99, 102, 241, 0.1) !important;
    color: #c4b5fd !important;
}
.stButton > button:hover {
    background: rgba(99, 102, 241, 0.25) !important;
    border-color: #a78bfa !important;
    transform: translateY(-1px) !important;
}
.stButton > button[kind="primary"] {
    background: linear-gradient(135deg, #6366f1, #8b5cf6) !important;
    color: #fff !important;
    border: none !important;
}

/* 展开面板 */
.streamlit-expanderHeader {
    color: #a78bfa !important;
    background: rgba(99, 102, 241, 0.06) !important;
    border-radius: 8px !important;
    border: 1px solid rgba(99, 102, 241, 0.1) !important;
}

/* 分隔线 */
hr { border-color: rgba(99, 102, 241, 0.15) !important; }

/* 状态提示 */
.stSuccess { background: rgba(34, 197, 94, 0.1) !important; border-color: rgba(34, 197, 94, 0.3) !important; color: #4ade80 !important; }
.stWarning { background: rgba(251, 191, 36, 0.1) !important; border-color: rgba(251, 191, 36, 0.3) !important; color: #fbbf24 !important; }
.stInfo { background: rgba(6, 182, 212, 0.1) !important; border-color: rgba(6, 182, 212, 0.3) !important; color: #22d3ee !important; }
.stError { background: rgba(239, 68, 68, 0.1) !important; border-color: rgba(239, 68, 68, 0.3) !important; color: #f87171 !important; }

/* Metric 卡片 */
[data-testid="stMetric"] {
    background: rgba(30, 30, 50, 0.6) !important;
    border: 1px solid rgba(99, 102, 241, 0.12) !important;
    border-radius: 12px !important;
    padding: 16px !important;
}
[data-testid="stMetricValue"] { color: #a78bfa !important; }

/* 链接 & 代码 */
a { color: #818cf8 !important; }
code { color: #c4b5fd !important; background: rgba(99, 102, 241, 0.12) !important; padding: 2px 6px !important; border-radius: 4px !important; }

/* 滚动条 */
::-webkit-scrollbar { width: 6px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb { background: rgba(99, 102, 241, 0.25); border-radius: 3px; }
</style>
"""

# ── 亮色主题（专业企业亮色） ──

LIGHT_THEME = """
<style>
/* ── 语义化颜色变量（供内联 HTML 通过 var() 引用） ── */
.stApp {
    --text-primary: #1e293b;
    --text-secondary: #475569;
    --text-muted: #64748b;
    --bg-card: #ffffff;
    --border-color: #e2e8f0;
}

.stApp {
    background: linear-gradient(135deg, #f8fafc 0%, #f1f5f9 50%, #e2e8f0 100%) !important;
    color: #1e293b !important;
}
[data-testid="stSidebar"] {
    background: #ffffff !important;
    border-right: 1px solid #e2e8f0 !important;
}
h1, h2, h3 { color: #4f46e5 !important; font-weight: 600 !important; }
h4, h5, h6 { color: #6366f1 !important; }
.stChatMessage {
    background: #ffffff !important;
    border: 1px solid #e2e8f0 !important;
    border-radius: 12px !important;
    padding: 16px !important;
}
.stChatMessage[data-testid="stChatMessage-user"] {
    border-left: 3px solid #4f46e5 !important;
    background: #eef2ff !important;
}
.stChatMessage[data-testid="stChatMessage-assistant"] {
    border-left: 3px solid #0891b2 !important;
    background: #ecfeff !important;
}
.stChatInput textarea {
    background: #ffffff !important;
    border: 1px solid #cbd5e1 !important;
    border-radius: 12px !important;
    color: #1e293b !important;
    padding: 12px 16px !important;
}
.stChatInput textarea::placeholder { color: #94a3b8 !important; }
.stButton > button {
    border-radius: 8px !important;
    font-weight: 500 !important;
    transition: all 0.2s !important;
    border: 1px solid #cbd5e1 !important;
    background: #f8fafc !important;
    color: #475569 !important;
}
.stButton > button:hover {
    background: #e2e8f0 !important;
    border-color: #6366f1 !important;
}
.stButton > button[kind="primary"] {
    background: linear-gradient(135deg, #4f46e5, #6366f1) !important;
    color: #fff !important;
    border: none !important;
}
.streamlit-expanderHeader {
    color: #4f46e5 !important;
    background: #f8fafc !important;
    border-radius: 8px !important;
    border: 1px solid #e2e8f0 !important;
}
hr { border-color: #e2e8f0 !important; }
.stSuccess { background: #f0fdf4 !important; border-color: #bbf7d0 !important; color: #16a34a !important; }
.stWarning { background: #fefce8 !important; border-color: #fef08a !important; color: #ca8a04 !important; }
.stInfo { background: #ecfeff !important; border-color: #a5f3fc !important; color: #0891b2 !important; }
.stError { background: #fef2f2 !important; border-color: #fecaca !important; color: #dc2626 !important; }
[data-testid="stMetric"] {
    background: #ffffff !important;
    border: 1px solid #e2e8f0 !important;
    border-radius: 12px !important;
    padding: 16px !important;
}
[data-testid="stMetricValue"] { color: #4f46e5 !important; }
a { color: #6366f1 !important; }
code { color: #7c3aed !important; background: #f5f3ff !important; padding: 2px 6px !important; border-radius: 4px !important; }
</style>
"""


def apply_theme(theme: str = "dark"):
    """应用主题样式。"""
    if theme == "light":
        st.markdown(LIGHT_THEME, unsafe_allow_html=True)
    else:
        st.markdown(DARK_THEME, unsafe_allow_html=True)

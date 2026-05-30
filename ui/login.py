"""登录页面模块。"""

from datetime import datetime

import streamlit as st
from ui import render_logo_img


def render_login_screen(config=None):
    """渲染全屏登录界面（企业风格）。"""
    if config is None:
        from rag.config import get_config
        config = get_config()
    ui_cfg = config.ui

    # 居中容器
    st.markdown("""
    <style>
    .login-container {
        display: flex;
        justify-content: center;
        align-items: center;
        min-height: 70vh;
    }
    .login-card {
        max-width: 420px;
        width: 100%;
        padding: 48px 40px;
        border-radius: 16px;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

    _, col_center, _ = st.columns([1, 2, 1])

    with col_center:
        st.markdown("<br><br>", unsafe_allow_html=True)

        st.markdown(f"""
        <div style="text-align:center;">
            {render_logo_img(width=96)}
            <h2 style="margin:8px 0 4px 0;">{ui_cfg.title}</h2>
            <p style="color:#888; margin:0 0 32px 0; font-size:0.9em;">{ui_cfg.subtitle}</p>
        </div>
        """, unsafe_allow_html=True)

        username = st.text_input(
            "用户名",
            placeholder="请输入你的姓名或工号",
            label_visibility="collapsed",
        )

        if st.button("🔓 接入系统", use_container_width=True, type="primary"):
            if username.strip():
                st.session_state.username = username.strip()
                st.rerun()
            else:
                st.warning("用户名不能为空")

        if ui_cfg.company_name:
            copyright_text = f"Copyright © {datetime.now().year} {ui_cfg.company_name}. All rights reserved."
            st.markdown(f"""
            <div style="text-align:center; margin-top:40px; color:#888; font-size:0.75em;">
                {copyright_text}
            </div>
            """, unsafe_allow_html=True)


# 兼容旧接口
def render_login():
    render_login_screen(None)

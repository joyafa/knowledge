"""登录页面模块。

支持登录和注册双模式：
- 登录模式：输入用户名 + 密码，验证后进入系统
- 注册模式：输入用户名 + 密码 + 确认密码，注册新账户
"""

from datetime import datetime

import streamlit as st
from ui import render_logo_img


def render_login_screen(config=None):
    """渲染全屏登录/注册界面（企业风格）。"""
    if config is None:
        from rag.config import get_config
        config = get_config()
    ui_cfg = config.ui
    auth_cfg = config.auth

    # ── 页面样式 ──
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

    # ── 模式切换状态 ──
    if "login_mode" not in st.session_state:
        st.session_state.login_mode = "login"  # "login" | "register"

    _, col_center, _ = st.columns([1, 2, 1])

    with col_center:
        st.markdown("<br><br>", unsafe_allow_html=True)

        # ── Logo + 标题 ──
        st.markdown(f"""
        <div style="text-align:center;">
            {render_logo_img(width=96)}
            <h2 style="margin:8px 0 4px 0;">{ui_cfg.title}</h2>
            <p style="color:var(--text-secondary); margin:0 0 32px 0; font-size:0.9em;">{ui_cfg.subtitle}</p>
        </div>
        """, unsafe_allow_html=True)

        if not auth_cfg.enabled:
            # ── 无密码模式（兼容旧版） ──
            _render_no_auth_login()
        elif st.session_state.login_mode == "register":
            _render_register_form(auth_cfg)
        else:
            _render_login_form(auth_cfg)

        # ── 版权 ──
        if ui_cfg.company_name:
            copyright_text = f"Copyright © {datetime.now().year} {ui_cfg.company_name}. All rights reserved."
            st.markdown(f"""
            <div style="text-align:center; margin-top:40px; color:var(--text-secondary); font-size:0.75em;">
                {copyright_text}
            </div>
            """, unsafe_allow_html=True)


# ── 无密码登录（auth.enabled=false 兼容模式） ──

def _render_no_auth_login():
    """无密码登录模式（仅输入用户名）。"""
    username = st.text_input(
        "用户名",
        placeholder="请输入你的姓名或工号",
        label_visibility="collapsed",
    )

    if st.button("🔓 接入系统", use_container_width=True, type="primary"):
        if username.strip():
            st.session_state.username = username.strip()
            st.session_state.authenticated = True
            st.rerun()
        else:
            st.warning("用户名不能为空")


# ── 登录表单 ──

def _render_login_form(auth_cfg):
    """渲染登录表单（用户名 + 密码）。"""
    username = st.text_input(
        "用户名",
        placeholder="请输入用户名",
        label_visibility="collapsed",
        key="login_username",
    )

    password = st.text_input(
        "密码",
        type="password",
        placeholder="请输入密码",
        label_visibility="collapsed",
        key="login_password",
    )

    c1, c2 = st.columns([3, 2])
    with c1:
        if st.button("🔐 登录", use_container_width=True, type="primary"):
            if not username.strip():
                st.warning("请输入用户名")
            elif not password:
                st.warning("请输入密码")
            else:
                _do_login(username.strip(), password, auth_cfg)

    with c2:
        if st.button("注册新账户", use_container_width=True):
            st.session_state.login_mode = "register"
            # 预填用户名
            if username.strip():
                st.session_state.prefill_username = username.strip()
            st.rerun()


# ── 注册表单 ──

def _render_register_form(auth_cfg):
    """渲染注册表单（用户名 + 密码 + 确认密码）。"""
    prefill = st.session_state.pop("prefill_username", "")

    username = st.text_input(
        "用户名",
        value=prefill,
        placeholder="2-32 个字符",
        label_visibility="collapsed",
        key="reg_username",
    )

    password = st.text_input(
        "密码",
        type="password",
        placeholder=f"至少 {auth_cfg.min_password_length} 个字符",
        label_visibility="collapsed",
        key="reg_password",
    )

    confirm = st.text_input(
        "确认密码",
        type="password",
        placeholder="再次输入密码",
        label_visibility="collapsed",
        key="reg_confirm",
    )

    c1, c2 = st.columns([3, 2])
    with c1:
        if st.button("✅ 注册", use_container_width=True, type="primary"):
            if not username.strip():
                st.warning("请输入用户名")
            elif not password:
                st.warning("请输入密码")
            elif password != confirm:
                st.error("两次输入的密码不一致")
            else:
                _do_register(username.strip(), password, auth_cfg)

    with c2:
        if st.button("← 返回登录", use_container_width=True):
            st.session_state.login_mode = "login"
            if username.strip():
                st.session_state.prefill_login = username.strip()
            st.rerun()


# ── 核心操作 ──

def _do_login(username: str, password: str, auth_cfg):
    """执行登录验证。"""
    from services.auth import get_user_manager

    um = get_user_manager(auth_cfg.users_file)

    if not um.user_exists(username):
        st.error("账户不存在，请检查用户名或注册新账户")
    elif um.authenticate(username, password):
        st.session_state.username = username
        st.session_state.authenticated = True
        # 清理登录临时状态
        st.session_state.pop("login_mode", None)
        st.session_state.pop("reg_username", None)
        st.session_state.pop("reg_password", None)
        st.session_state.pop("reg_confirm", None)
        st.session_state.pop("login_username", None)
        st.session_state.pop("login_password", None)
        st.rerun()
    else:
        st.error("密码错误，请重试")


def _do_register(username: str, password: str, auth_cfg):
    """执行用户注册。"""
    from services.auth import get_user_manager

    um = get_user_manager(auth_cfg.users_file)
    success, message = um.register(username, password)

    if success:
        st.success(message)
        # 注册成功后自动登录
        st.session_state.username = username
        st.session_state.authenticated = True
        st.session_state.pop("login_mode", None)
        st.session_state.pop("reg_username", None)
        st.session_state.pop("reg_password", None)
        st.session_state.pop("reg_confirm", None)
        st.rerun()
    else:
        st.error(message)


# 兼容旧接口
def render_login():
    render_login_screen(None)

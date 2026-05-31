"""侧边栏模块。

使用 Streamlit 原生 st.sidebar，专业的导航体验。
支持树形折叠的知识库文档清单。
"""

import re
import os
import streamlit as st
from datetime import datetime
from pathlib import Path

from rag import __version__
from rag.config import get_config
from rag.preload import is_done, get_error
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


def render_sidebar(config):
    """渲染侧边栏。"""
    ui_cfg = config.ui
    username = st.session_state.get("username", "?")

    # 管理员判断：优先使用 auth 服务，兼容旧 config.admin_users
    is_admin = _check_admin(username, config)

    with st.sidebar:
        # ── Logo 区域 ──
        st.markdown(f"""
        <div style="text-align:center; padding: 16px 0 8px 0;">
            {render_logo_img(width=72)}
            <div style="font-size:0.95em; font-weight:600; margin-top:8px;">{ui_cfg.title}</div>
            <div style="font-size:0.7em; color:var(--text-secondary); margin-top:2px;">v{__version__}</div>
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
            if st.button(theme_label, key="nav_theme", help=f"切换到{'亮色' if current_theme == 'dark' else '暗色'}主题"):
                st.session_state.theme = "light" if current_theme == "dark" else "dark"
                st.rerun()

        # ── 导航 ──
        st.markdown("---")
        page = st.session_state.get("page", "chat")

        if st.button("💬 智能问答" if page != "chat" else "▸ 💬 智能问答",
                     key="nav_chat",
                     use_container_width=True,
                     type="primary" if page == "chat" else "secondary"):
            st.session_state.page = "chat"
            st.rerun()

        if st.button("📊 仪表盘" if page != "dashboard" else "▸ 📊 仪表盘",
                     key="nav_dashboard",
                     use_container_width=True,
                     type="primary" if page == "dashboard" else "secondary"):
            st.session_state.page = "dashboard"
            st.rerun()

        if is_admin:
            if st.button("🔰 管理面板" if page != "admin" else "▸ 🔰 管理面板",
                         key="nav_admin",
                         use_container_width=True,
                         type="primary" if page == "admin" else "secondary"):
                st.session_state.page = "admin"
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

        # ── 知识库文档（树形折叠） ──
        st.caption("📚 知识库文档")

        # 缓存文件元数据：仅目录有变化时才重新扫描
        files = _load_files_meta_cached(config.knowledge.docs_directory)
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

            # 构建树并渲染
            tree = _build_file_tree(filtered)
            _render_file_tree(tree, config, depth=0)

        # ── 历史记录 ──
        with st.expander("📅 历史记录", expanded=False):
            all_dates = load_all_history_dates(username)
            if all_dates:
                for date_str in all_dates[:10]:
                    label = date_str + (" · 今天" if date_str == datetime.now().strftime("%Y-%m-%d") else "")
                    st.markdown(f"**{label}**")
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
                # VectorStore 单例已缓存，但 stats 涉及 ChromaDB 查询 - 缓存 30 秒
                cached_stats = st.session_state.get("sidebar_vs_stats")
                if cached_stats:
                    st.success(f"✅ 向量库已就绪 ({cached_stats['total_chunks']}块)")
                else:
                    vs = VectorStore.from_config()
                    s = vs.get_stats()
                    st.session_state["sidebar_vs_stats"] = s
                    st.success(f"✅ 向量库已就绪 ({s['total_chunks']}块)")
            elif is_done():
                # 线程已完成但 chain 未就绪 → 竞态或真实错误
                err = get_error()
                st.warning(f"⚠️ 初始化失败: {err[:50]}")
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
            copyright_text = f"Copyright © {datetime.now().year} {ui_cfg.company_name}. All rights reserved."
            st.markdown(f"""
            <div style="text-align:center; padding:20px 0 8px 0; color:var(--text-secondary); font-size:0.7em;">
                {copyright_text}
            </div>
            """, unsafe_allow_html=True)


# ── 文档树构建与渲染 ──


def _get_dir_fingerprint(docs_dir: str) -> str:
    """计算目录指纹（基于文件数量 + 最新修改时间），用于缓存失效判断。"""
    try:
        root = Path(docs_dir)
        if not root.exists():
            return ""
        latest = 0.0
        count = 0
        for p in root.rglob("*"):
            if p.is_file():
                count += 1
                mtime = p.stat().st_mtime
                if mtime > latest:
                    latest = mtime
        return f"{count}_{latest}"
    except Exception:
        return ""


def _load_files_meta_cached(docs_dir: str) -> list[dict]:
    """带缓存的获取文件元数据，仅在目录变化时重新扫描。"""
    cache_key = "sidebar_files_meta"
    fp_key = "sidebar_files_fingerprint"
    fingerprint = _get_dir_fingerprint(docs_dir)
    if (
        cache_key in st.session_state
        and fp_key in st.session_state
        and st.session_state[fp_key] == fingerprint
    ):
        return st.session_state[cache_key]
    files = get_knowledge_files_meta(docs_dir)
    st.session_state[cache_key] = files
    st.session_state[fp_key] = fingerprint
    return files


# Doxygen 编码映射
_DOXYGEN_EXT_MAP = {
    "_8c": ".c", "_8cc": ".cc", "_8cpp": ".cpp", "_8cxx": ".cxx",
    "_8h": ".h", "_8hpp": ".hpp", "_8hxx": ".hxx",
    "_8md": ".md", "_8txt": ".txt", "_8pdf": ".pdf",
}
_DOXYGEN_EXT_RE = re.compile("|".join(map(re.escape, sorted(_DOXYGEN_EXT_MAP.keys(), key=len, reverse=True))))

# Doxygen 类型前缀
_TYPE_PREFIXES = re.compile(
    r'^(class|struct|namespace|dir_|group__|examples_|index_|pages_|deprecated_|todo_|test_|bug_)'
)


def _parse_doxygen_name(filename: str) -> list[str] | None:
    """将 Doxygen 文件名解析为树路径。

    例如:
      classmuduo_1_1net_1_1_buffer.md  → ['muduo', 'net', 'Buffer']
      ace_2logging_2client_8cc.md       → ['ace', 'logging', 'client.cc']
      _buffer_8cc.md                    → ['📁 源文件文档', 'Buffer.cc']
      TCPIP详解 卷1.pdf                 → ['TCPIP详解 卷1.pdf']
    """
    name = filename

    # 跳过 README / 目录页 / index
    if name.lower() == "readme.md":
        return None
    if name.startswith("dir_") or name.startswith("index_"):
        return None

    # ── 去掉扩展名 ──
    ext = ""
    for e in (".md", ".pdf", ".txt"):
        if name.endswith(e):
            ext = e
            name = name[:-len(e)]
            break

    # ── 拆分路径：先按 _2（Doxygen 目录分隔符）再按 _1_1（Doxygen ::） ──
    # 例: ace_2logging_2client → ['ace', 'logging', 'client']
    # 例: muduo_1_1net_1_1Buffer → ['muduo', 'net', 'Buffer']
    if "_2" in name:
        parts = name.split("_2")
    elif "_1_1" in name:
        parts = name.split("_1_1")
    else:
        parts = [name]

    # ── 清理每个部分 ──
    cleaned = []
    for p in parts:
        # 去掉 Doxygen 类型前缀
        p = _TYPE_PREFIXES.sub("", p)
        # 还原扩展名: _8cc → .cc 等
        p = _DOXYGEN_EXT_RE.sub(lambda m: _DOXYGEN_EXT_MAP[m.group()], p)
        # 还原双下划线 → 单下划线
        p = p.replace("__", "_")
        # 去掉残留的 _1_ 等后缀
        p = re.sub(r"_1_[a-z0-9]*$", "", p)
        # 去掉首尾下划线
        p = p.strip("_")
        if p:
            cleaned.append(p)

    if not cleaned:
        return [filename]

    # ── 分类：文件文档页 → "源文件文档" 分组 ──
    # _X_Y.md 模式（以 _ 开头，不含 _2 或 _1_1 路径分隔符）
    if filename.startswith("_") and "_2" not in filename and "_1_1" not in filename:
        # _buffer_8cc.md → Buffer.cc
        display = cleaned[-1] if len(cleaned) == 1 else "/".join(cleaned)
        return ["📁 源文件文档", display]

    # 同样处理 ace_2logging_2client_8cc.md 这类（无下划线开头但含 _2）
    # 它们也是文件文档页，按路径分组即可

    return cleaned


def _build_file_tree(files: list[dict]) -> dict:
    """将文件列表构建为树结构。

    Returns:
        {name: {type: 'dir'|'file', children: {...}, meta: {...}}}
    """
    tree = {"": {"type": "dir", "children": {}, "count": 0}}

    for f in files:
        name = f["name"]
        path_parts = _parse_doxygen_name(name)
        if path_parts is None:
            continue  # 跳过的文件

        node = tree[""]
        # 遍历到叶子前一层
        for part in path_parts[:-1]:
            if part not in node["children"]:
                node["children"][part] = {"type": "dir", "children": {}, "count": 0}
            node = node["children"][part]
            node["count"] += 1

        # 叶子节点
        leaf_name = path_parts[-1]
        if leaf_name not in node["children"]:
            node["children"][leaf_name] = {
                "type": "file",
                "children": {},
                "count": 0,
                "files": [],
            }
        leaf = node["children"][leaf_name]
        leaf["count"] += 1
        leaf.setdefault("files", []).append(f)
        node["count"] += 1

    return tree[""]["children"]


def _render_file_tree(tree: dict, config, depth: int = 0):
    """递归渲染文件树（HTML details/summary 实现，绕过 Streamlit expander 嵌套限制）。"""
    import html as _html
    docs_dir = config.knowledge.docs_directory

    # 按名称排序：目录在前，文件在后
    items = sorted(tree.items(), key=lambda x: (x[1]["type"] != "dir", x[0].lower()))

    html_parts = []

    for name, node in items:
        is_dir = node["type"] == "dir"
        count = node.get("count", 0)
        files_list = node.get("files", [])
        children = node.get("children", {})

        # 如果目录下只有一个文件且无子目录，直接展平为文件
        if is_dir and len(files_list) == 1 and not children:
            html_parts.append(_render_file_html(files_list[0], docs_dir))
            continue

        if is_dir:
            icon = "📂"
            label = f"{name} ({count})" if count > 0 else name
            child_html = []
            # 该目录下的文件
            for f in files_list:
                child_html.append(_render_file_html(f, docs_dir))
            # 子目录（递归）
            if children:
                child_html.append(_render_tree_html(children, config, docs_dir, depth + 1))
            body = "".join(child_html)
            open_attr = " open" if depth == 0 else ""
            html_parts.append(
                f"<details{open_attr} style='margin-left:{depth * 12}px;'>"
                f"<summary style='cursor:pointer;padding:2px 0;color:var(--text-primary);'>{icon} {_html.escape(label)}</summary>"
                f"<div style='margin-left:16px;'>{body}</div>"
                f"</details>"
            )
        else:
            if files_list:
                for f in files_list:
                    html_parts.append(_render_file_html(f, docs_dir))

    html_str = "".join(html_parts)
    if html_str:
        st.markdown(html_str, unsafe_allow_html=True)


def _render_tree_html(tree: dict, config, docs_dir: str, depth: int) -> str:
    """递归生成树节点的 HTML 字符串（不直接渲染，由父级组装）。"""
    import html as _html
    items = sorted(tree.items(), key=lambda x: (x[1]["type"] != "dir", x[0].lower()))
    parts = []
    for name, node in items:
        is_dir = node["type"] == "dir"
        count = node.get("count", 0)
        files_list = node.get("files", [])
        children = node.get("children", {})
        if is_dir and len(files_list) == 1 and not children:
            parts.append(_render_file_html(files_list[0], docs_dir))
            continue
        if is_dir:
            icon = "📂"
            label = f"{name} ({count})" if count > 0 else name
            child_html = []
            for f in files_list:
                child_html.append(_render_file_html(f, docs_dir))
            if children:
                child_html.append(_render_tree_html(children, config, docs_dir, depth + 1))
            body = "".join(child_html)
            parts.append(
                f"<details style='margin-left:{depth * 12}px;'>"
                f"<summary style='cursor:pointer;padding:2px 0;color:var(--text-primary);'>{icon} {_html.escape(label)}</summary>"
                f"<div style='margin-left:16px;'>{body}</div>"
                f"</details>"
            )
        else:
            if files_list:
                for f in files_list:
                    parts.append(_render_file_html(f, docs_dir))
    return "".join(parts)


def _render_file_html(f: dict, docs_dir: str) -> str:
    """生成单个文件条目的 HTML 字符串（不含预览内容，避免每次渲染读取全部文件）。"""
    import html as _html
    size_label = f"{f['size'] // 1024}KB" if f['size'] >= 1024 else f"{f['size']}B"
    icon = f.get("icon", "📄")
    title = f["title"][:28]

    return (
        f"<details style='margin:1px 0;'>"
        f"<summary style='cursor:pointer;padding:1px 0;font-size:0.85em;color:var(--text-secondary);'>"
        f"{icon} {_html.escape(title)} ({size_label})"
        f"</summary>"
        f"<div style='margin-left:20px;'>"
        f"<small><code>{_html.escape(f['path'])}</code></small>"
        f"</div>"
        f"</details>"
    )


def _check_admin(username: str, config) -> bool:
    """判断用户是否为管理员。

    优先使用 auth 服务的角色信息，
    兼容旧版 config.admin_users 配置。
    """
    # auth 服务
    if config.auth.enabled:
        from services.auth import get_user_manager
        um = get_user_manager(config.auth.users_file)
        if um.user_exists(username):
            return um.is_admin(username)

    # 兼容旧版 admin_users 列表
    return username in config.admin_users

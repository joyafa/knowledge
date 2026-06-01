# -*- mode: python ; coding: utf-8 -*-
"""PyInstaller 打包规格文件 — 知识库智能问答系统。

用法:
    pyinstaller knowledge_app.spec

输出:
    dist/KnowledgeAssistant/（单目录模式）
"""

import sys
import os
from pathlib import Path
from PyInstaller.utils.hooks import copy_metadata, collect_dynamic_libs, collect_data_files, collect_submodules

# PyInstaller spec 文件中 __file__ 不可用，使用 SPECPATH
ROOT = Path(SPECPATH)

# ── 需要作为数据文件包含的项目资源 ──
# app.py 必须作为数据文件保留（Streamlit 需要文件路径来运行）
# config.yaml 用户可编辑，也作为数据文件
datas = [
    (str(ROOT / "app.py"), "."),
    (str(ROOT / "config.yaml"), "."),
]

# logo.png
logo = ROOT / "logo.png"
if logo.exists():
    datas.append((str(logo), "."))

# 项目模块（rag/ui/services 已通过 hiddenimports 编译进 PYZ，无需作为源码文件打包）

# knowledge/ 和 data/knowledge/ 不再打包进安装包（部署时通过 ingest 入库）

# ── 复制包元数据（解决 PyInstaller 打包后 importlib.metadata 找不到包信息的问题） ──
# streamlit 启动时通过 importlib.metadata.version('streamlit') 检查版本，必须包含 dist-info
datas += copy_metadata('streamlit')
datas += copy_metadata('pydantic')
datas += copy_metadata('sentence_transformers')
datas += copy_metadata('chromadb')
datas += copy_metadata('torch')
datas += copy_metadata('transformers')
datas += copy_metadata('openai')

# ── 收集 Streamlit 前端静态资源（HTML/JS/CSS/字体等） ──
# PyInstaller 没有内置 streamlit hook，必须显式收集 static/ 目录，
# 否则运行时报错: FileNotFoundError: streamlit/static/index.html
datas += collect_data_files('streamlit')

# ── 收集 PyTorch 动态库（c10.dll, torch_cpu.dll 等） ──
# PyInstaller 的自动依赖分析可能遗漏 torch 的核心 DLL，导致运行时：[WinError 1114] DLL 初始化失败
binaries = collect_dynamic_libs('torch')

# ── 隐藏导入 ──
# Streamlit 及其依赖
hiddenimports = [
    # Streamlit
    "streamlit",
    "streamlit.web",
    "streamlit.web.cli",
    "streamlit.runtime",
    "streamlit.runtime.scriptrunner",
    "streamlit.runtime.scriptrunner.magic_funcs",
    "streamlit.runtime.scriptrunner.magic",
    "streamlit.runtime.scriptrunner.exec_code",
    "streamlit.runtime.scriptrunner.script_cache",
    "streamlit.watcher",
    "streamlit.watcher.local_sources_watcher",
    "streamlit.elements",
    "streamlit.commands",
    # PyTorch
    "torch",
    "torchvision",
    "torchaudio",
    # Sentence Transformers
    "sentence_transformers",
    "sentence_transformers.models",
    # Transformers
    "transformers",
    "transformers.models",
    # 标准库（运行时可能被动态引用）
    "modulefinder",
    # ChromaDB 命名空间包（无 __init__.py，collect_submodules 只能部分收录）
    # 通过 _s.py 全量扫描得出，确保无一遗漏
    "chromadb",
    "chromadb.api",
    "chromadb.utils",
    "chromadb.migrations.embeddings_queue",
    "chromadb.migrations.metadb",
    "chromadb.migrations.sysdb",
    "chromadb.db.impl.grpc",
    "chromadb.db.impl.grpc.client",
    "chromadb.db.impl.grpc.server",
    "chromadb.execution.executor.distributed",
    "chromadb.execution.executor.local",
    "chromadb.logservice",
    "chromadb.logservice.logservice",
    "chromadb.segment.impl.distributed",
    "chromadb.segment.impl.distributed.segment_directory",
    "chromadb.segment.impl.metadata",
    "chromadb.segment.impl.metadata.grpc_segment",
    "chromadb.segment.impl.metadata.sqlite",
    "chromadb.segment.impl.vector.grpc_segment",
    # 其他
    "openai",
    "yaml",
    "pydantic",
    "loguru",
    "jieba",
    "markdown",
    "pymupdf",
    "httpx",
    "tiktoken",
    # 项目模块
    "rag",
    "rag.config",
    "rag.chain",
    "rag.vectorstore",
    "rag.embeddings",
    "rag.preload",
    "rag.loader",
    "rag.logging_config",
    "ui",
    "ui.theme",
    "ui.login",
    "ui.sidebar",
    "ui.chat",
    "ui.admin",
    "services",
    "services.analytics",
    "services.auth",
    "services.history",
    "services.knowledge_service",
    "services.rate_limiter",
]

# ── ChromaDB 动态加载的 embedding function 子模块 ──
# ChromaDB 存在大量字符串驱动的动态导入（config.py 用 importlib.import_module()），
# 包括 api/segment、db/sqlite、telemetry/posthog、execution/executor、quota、ingest 等。
# PyInstaller 无法静态分析，必须一次性收集所有 95 个子模块，避免逐一排查遗漏。
hiddenimports += collect_submodules("chromadb")

# ── ChromaDB 命名空间包的数据文件（无 __init__.py 的目录） ──
# chromadb/migrations/* 目录含 SQL 迁移文件，由 importlib.resources.files() 动态加载，
# collect_submodules 扫不到命名空间包，必须显式收集数据文件。
datas += collect_data_files("chromadb.migrations.embeddings_queue")
datas += collect_data_files("chromadb.migrations.metadb")
datas += collect_data_files("chromadb.migrations.sysdb")

# ── 排除的模块（减小体积） ──
excludes = [
    "matplotlib",
    "pandas",
    "numpy.tests",
    "torch.utils.tensorboard",
    "tensorflow",
    "tensorboard",
    "IPython",
    "jupyter",
    "notebook",
    "tkinter",
    "test",
    "torch.classes",  # C++ 扩展命名空间，PyInstaller 无法分析，排除以消除警告
]

a = Analysis(
    [str(ROOT / "run_app.py")],
    pathex=[str(ROOT)],
    binaries=binaries,
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[str(ROOT / "scripts/hooks")],
    hooksconfig={},
    runtime_hooks=[str(ROOT / "scripts/hooks/runtime_hook_chromadb.py")],
    excludes=excludes,
    noarchive=False,
    optimize=0,
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],  # binaries 由 COLLECT 统一管理，EXE 不内嵌
    [],  # zipfiles 为空
    [],  # datas 由 COLLECT 统一管理，EXE 不内嵌
    name="KnowledgeAssistant",
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=None,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=False,
    upx_exclude=[],
    name="KnowledgeAssistant",
)

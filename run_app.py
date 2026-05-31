"""PyInstaller 入口脚本 — 知识库智能问答系统启动器。

检测 frozen 模式（PyInstaller 打包），自动设置路径、环境变量，
检查/下载 AI 模型，然后启动 Streamlit 服务。

开发模式：直接 `python run_app.py`
打包模式：PyInstaller 编译后运行 exe
"""

import os
import sys
from datetime import datetime
from pathlib import Path


def _patch_importlib_metadata():
    """Monkey-patch importlib.metadata.version 以处理 PyInstaller 打包后元数据缺失的问题。

    PyInstaller 打包时可能漏掉某些包的 dist-info 目录，
    导致 importlib.metadata.version() 抛出 PackageNotFoundError。
    此补丁使缺失元数据的包返回占位版本号，避免崩溃。
    """
    import importlib.metadata
    _original_version = importlib.metadata.version

    def _patched_version(package_name):
        try:
            return _original_version(package_name)
        except importlib.metadata.PackageNotFoundError:
            # PyInstaller 打包后可能缺少 dist-info，返回安全默认值
            _FALLBACKS = {
                'streamlit': '1.0.0',
                'pydantic': '2.0.0',
                'torch': '2.0.0',
                'sentence_transformers': '2.0.0',
                'chromadb': '0.4.0',
                'transformers': '4.0.0',
                'openai': '1.0.0',
            }
            if package_name in _FALLBACKS:
                return _FALLBACKS[package_name]
            raise

    importlib.metadata.version = _patched_version
    # 同时补丁 metadata() 函数（某些库使用）
    if hasattr(importlib.metadata, 'metadata'):
        _original_metadata = importlib.metadata.metadata
        def _patched_metadata(package_name):
            try:
                return _original_metadata(package_name)
            except importlib.metadata.PackageNotFoundError:
                from email.message import EmailMessage
                msg = EmailMessage()
                msg['Name'] = package_name
                msg['Version'] = '1.0.0'
                return msg
        importlib.metadata.metadata = _patched_metadata


# 在导入任何第三方库之前先打补丁
_patch_importlib_metadata()


def get_app_root() -> Path:
    """获取应用根目录。

    PyInstaller 打包后，exe 所在目录即为 app root。
    开发模式下，脚本所在目录（项目根目录）为 app root。
    """
    if getattr(sys, "frozen", False):
        # PyInstaller 打包模式
        return Path(sys.executable).parent.resolve()
    else:
        # 开发模式
        return Path(__file__).parent.resolve()


def _patch_dll_search_path(app_root: Path) -> None:
    """修复 PyInstaller 打包后 DLL 搜索路径问题。

    问题背景：
    PyInstaller 将 Python 扩展模块（.pyd）和第三方 DLL 收集到 _internal/ 目录，
    但 Windows 默认只在 exe 所在目录查找 DLL，不会自动搜索其子目录。
    同时，torch 等库内部按构建机器的绝对路径查找 DLL（如 c10.dll），
    导致目标机器上出现 DLL 加载失败、模块导入失败等问题。

    此函数将 _internal 自身及其下所有包含 DLL 的目录加入系统 DLL 搜索路径，
    确保 Windows 和 Python 能在正确的目录中找到所有依赖库。
    """
    if not getattr(sys, "frozen", False):
        return

    internal = app_root / "_internal"
    if not internal.exists():
        print(f"  [DLL] 警告: _internal 目录不存在: {internal}")
        return

    # 1) 首先将 _internal/ 本身加入 DLL 搜索路径
    #    PyInstaller 将 python3.dll, sqlite3.dll 等核心 DLL 直接放在 _internal/ 根目录
    os.add_dll_directory(str(internal))
    print(f"  [DLL] 已添加 _internal 根路径: {internal}")

    # 2) torch/lib 包含 c10.dll, torch_cpu.dll, fbgemm.dll 等
    torch_lib = internal / "torch" / "lib"
    if torch_lib.is_dir():
        os.add_dll_directory(str(torch_lib))
        print(f"  [DLL] 已添加 torch 库路径: {torch_lib}")

    # 3) 扫描 _internal 下所有子目录，注册任何包含 .dll 的目录
    #    处理 torchvision、numpy 等可能有独立 .libs 目录的包
    try:
        for item in internal.iterdir():
            if item.is_dir():
                # .libs 目录（如 numpy.libs, scipy.libs）
                if item.name.endswith(".libs"):
                    os.add_dll_directory(str(item))
                # lib 子目录（如 torchvision/lib）
                lib_sub = item / "lib"
                if lib_sub.is_dir() and lib_sub != torch_lib:
                    os.add_dll_directory(str(lib_sub))
    except (OSError, PermissionError):
        pass


def ensure_dirs(app_root: Path) -> None:
    """确保运行时需要的目录存在。"""
    dirs = [
        "data/chroma_db",
        "data/knowledge",
        "data/logs",
        "data/chat_history",
        "model",
    ]
    for d in dirs:
        (app_root / d).mkdir(parents=True, exist_ok=True)


def copy_initial_knowledge(app_root: Path) -> None:
    """如果 data/knowledge 为空，从 knowledge/ 复制初始文档。"""
    src = app_root / "knowledge"
    dst = app_root / "data" / "knowledge"
    if src.exists() and src.is_dir():
        # 检查目标是否为空
        try:
            has_files = any(dst.iterdir())
        except (OSError, StopIteration):
            has_files = False
        if not has_files:
            import shutil
            print(f"正在复制初始知识库文档: {src} -> {dst}")
            shutil.copytree(src, dst, dirs_exist_ok=True)


def _write_llm_config(config_path: str, api_base: str, api_key: str, model: str) -> None:
    """写入 LLM 配置到 config.yaml（安装时由 NSIS 调用）。"""
    import yaml
    path = Path(config_path)
    if not path.exists():
        print(f"配置文件不存在: {path}")
        return
    with open(path, "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)
    if api_base:
        config["llm"]["api_base"] = api_base
    if api_key:
        config["llm"]["api_key"] = api_key
    if model:
        config["llm"]["model"] = model
    with open(path, "w", encoding="utf-8") as f:
        yaml.dump(config, f, default_flow_style=False, allow_unicode=True, sort_keys=False)
    print(f"LLM 配置已写入: {path}")


def main():
    """启动应用。"""
    # 处理 --write-config 模式（安装时由 NSIS 调用）
    if "--write-config" in sys.argv:
        try:
            idx = sys.argv.index("--write-config")
            config_path = sys.argv[idx + 1] if idx + 1 < len(sys.argv) else "config.yaml"
            api_base = sys.argv[idx + 2] if idx + 2 < len(sys.argv) else ""
            api_key = sys.argv[idx + 3] if idx + 3 < len(sys.argv) else ""
            model = sys.argv[idx + 4] if idx + 4 < len(sys.argv) else ""
            _write_llm_config(config_path, api_base, api_key, model)
            return
        except Exception as e:
            print(f"写配置失败: {e}")
            sys.exit(1)

    app_root = get_app_root()

    # ── PyInstaller 打包后修复运行环境 ──
    if getattr(sys, "frozen", False):
        # 显式将 _internal 加入 sys.path，确保所有 Python 库可被导入
        # PyInstaller bootloader 通常会做这件事，但混合模式（EXE + COLLECT）
        # 下可能遗漏，这里作为兜底保障
        internal_path = str(app_root / "_internal")
        if internal_path not in sys.path:
            sys.path.insert(0, internal_path)
            print(f"  [PATH] 已添加 _internal 到 sys.path: {internal_path}")
        # 同时添加 _internal/base_library.zip（PyInstaller 的 PYZ 归档）
        base_lib = str(app_root / "_internal" / "base_library.zip")
        if os.path.isfile(base_lib) and base_lib not in sys.path:
            sys.path.insert(0, base_lib)

    # 切换到应用根目录（确保相对路径正确）
    os.chdir(str(app_root))

    # PyInstaller 打包后修复 DLL 搜索路径（解决 torch c10.dll 及各类 DLL 加载失败）
    _patch_dll_search_path(app_root)

    # 检测本地模型（优先使用本地模型，避免首次启动联网下载）
    # 打包脚本会将模型复制到 model/text2vec-base-chinese/ 和 model/bge-reranker-base/
    model_dir = app_root / "model"
    emb_local = model_dir / "text2vec-base-chinese"
    reranker_local = model_dir / "bge-reranker-base"

    has_local_emb = emb_local.exists()
    has_local_reranker = reranker_local.exists()

    if has_local_emb:
        os.environ["EMBEDDING_LOCAL_PATH"] = str(emb_local)
        print(f"  [MODEL] 检测到本地 Embedding 模型: {emb_local}")
    else:
        print(f"  [MODEL] 未检测到本地 Embedding 模型，首次运行将自动下载")

    if has_local_reranker:
        os.environ["RERANKER_LOCAL_PATH"] = str(reranker_local)
        print(f"  [MODEL] 检测到本地 Reranker 模型: {reranker_local}")
    else:
        print(f"  [MODEL] 未检测到本地 Reranker 模型，首次运行将自动下载")

    # ── 环境变量 ──
    os.environ["MODEL_ROOT"] = str(model_dir)
    os.environ.setdefault("SENTENCE_TRANSFORMERS_HOME", str(model_dir))

    # 仅在缺少本地模型时才设置 HF 镜像（本地模型就绪时无需联网）
    if not (has_local_emb and has_local_reranker):
        os.environ.setdefault("HF_ENDPOINT", "https://hf-mirror.com")
    else:
        os.environ.pop("HF_ENDPOINT", None)  # 清除可能的残留，避免无谓联网尝试
        print(f"  [MODEL] 全部模型已本地就绪，禁用 HuggingFace 联网")

    # 确保运行时目录
    ensure_dirs(app_root)
    copy_initial_knowledge(app_root)

    # 打印启动信息
    from rag import __version__
    from rag.config import get_config
    cfg = get_config()
    copyright_line = f"Copyright © {datetime.now().year} {cfg.ui.company_name}. All rights reserved."
    print("=" * 60)
    print(f"  知识库智能问答系统  v{__version__}")
    print(f"  {copyright_line}")
    print(f"  应用目录: {app_root}")
    print(f"  模型目录: {app_root / 'model'}")
    print(f"  启动后请用浏览器访问: http://localhost:8501")
    print("=" * 60)

    # 启动 Streamlit
    from streamlit.web import cli as stcli

    app_file = str(app_root / "app.py")
    sys.argv = [
        "streamlit", "run", app_file,
        "--global.developmentMode", "false",
        "--server.port", "8501",
        "--server.address", "0.0.0.0",
        "--server.headless", "true",
        "--browser.gatherUsageStats", "false",
        "--server.enableCORS", "false",
        "--server.enableXsrfProtection", "false",
        # 禁用文件监控（打包后不需要热重载）
        "--server.fileWatcherType", "none",
    ]
    sys.exit(stcli.main())


if __name__ == "__main__":
    main()

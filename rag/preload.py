"""预加载模块 — 后台加载 RAGChain 状态管理。

独立模块不会被 Streamlit rerun 重置（Python 模块只导入一次），
因此后台线程写入的状态在任意次 rerun 后仍然可见。
"""

import threading
from rag.logging_config import get_logger

logger = get_logger(__name__)

# 预加载状态（可变字典，线程安全写入）
state: dict = {
    "chain": None,       # RAGChain 实例
    "error": None,       # 错误信息字符串
    "done": False,       # 是否完成（成功或失败）
    "started": False,    # 是否已启动线程
    "loading": False,    # 是否正在加载中
}


def start():
    """启动后台预加载线程（幂等，只启动一次）。"""
    if state["started"]:
        return
    state["started"] = True
    state["loading"] = True
    logger.info("后台预加载线程启动...")
    t = threading.Thread(target=_load, daemon=True)
    t.start()


def _load():
    """在后台线程中加载 RAGChain。"""
    try:
        logger.info("正在加载 RAGChain（包含 embedding 模型，约需 15 秒）...")
        from rag.chain import RAGChain
        chain = RAGChain.from_config()
        state["chain"] = chain
        state["error"] = None
        logger.info("RAGChain 加载完成 ✅")
    except Exception as e:
        state["error"] = str(e)
        state["chain"] = None
        logger.error("RAGChain 加载失败: %s", e)
    finally:
        state["done"] = True
        state["loading"] = False


def is_done() -> bool:
    """预加载是否已完成。"""
    return state["done"]


def get_chain():
    """获取已加载的 chain，未完成返回 None。"""
    return state["chain"]


def get_error() -> str:
    """获取错误信息。"""
    return state["error"] or "未知错误"


def reset():
    """重置状态，用于重新加载。"""
    state["chain"] = None
    state["error"] = None
    state["done"] = False
    state["started"] = False
    state["loading"] = False

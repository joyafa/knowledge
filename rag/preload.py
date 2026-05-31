"""预加载模块 — 后台加载 RAGChain 状态管理。

独立模块不会被 Streamlit rerun 重置（Python 模块只导入一次），
因此后台线程写入的状态在任意次 rerun 后仍然可见。
"""

import os
import sys
import threading
import traceback
from datetime import datetime
from pathlib import Path
from rag.logging_config import get_logger

logger = get_logger(__name__)

# 预加载状态（可变字典，线程安全写入）
state: dict = {
    "chain": None,         # RAGChain 实例
    "error": None,         # 错误信息字符串
    "error_traceback": "",  # 完整堆栈跟踪
    "error_log_file": "",   # 错误日志文件路径（写入磁盘，便于诊断）
    "done": False,         # 是否完成（成功或失败）
    "started": False,      # 是否已启动线程
    "loading": False,      # 是否正在加载中
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
    """在后台线程中加载 RAGChain 并预热模型。"""
    try:
        logger.info("正在加载 RAGChain（包含 embedding 模型，约需 15 秒）...")
        from rag.chain import RAGChain
        from rag.config import load_config
        chain = RAGChain.from_config()
        state["chain"] = chain
        state["error"] = None
        state["error_traceback"] = ""
        state["error_log_file"] = ""
        logger.info("RAGChain 加载完成 ✅")

        # 预热 Reranker 模型（避免首次查询时等待加载）
        try:
            config = load_config()
            RAGChain.warmup_reranker(config)
        except Exception as e:
            logger.warning("Reranker 预热跳过: %s", e)
    except Exception as e:
        # 确保错误信息不为空：优先使用异常消息，回退为异常类名
        err_msg = str(e).strip() if str(e).strip() else type(e).__name__
        full_tb = traceback.format_exc()
        state["error"] = err_msg
        state["error_traceback"] = full_tb
        state["chain"] = None
        logger.error("RAGChain 加载失败: %s\n%s", e, full_tb)
        # 写入磁盘文件，方便用户离线诊断
        _write_error_log(err_msg, full_tb)
    except BaseException as e:
        # 捕获 SystemExit / KeyboardInterrupt 等
        err_msg = str(e).strip() if str(e).strip() else type(e).__name__
        full_tb = traceback.format_exc()
        state["error"] = err_msg
        state["error_traceback"] = full_tb
        state["chain"] = None
        _write_error_log(err_msg, full_tb)
        raise
    finally:
        state["done"] = True
        state["loading"] = False


def _write_error_log(err_msg: str, full_tb: str):
    """将初始化错误写入磁盘文件。"""
    try:
        log_dir = Path("data/logs")
        log_dir.mkdir(parents=True, exist_ok=True)
        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        fpath = log_dir / f"init_error_{ts}.txt"
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(f"=== 系统初始化失败 {ts} ===\n")
            f.write(f"Python: {sys.version}\n")
            f.write(f"SysPath: {sys.path[:5]}\n")
            f.write(f"Frozen: {getattr(sys, 'frozen', False)}\n\n")
            f.write(f"错误信息: {err_msg}\n\n")
            f.write(f"完整堆栈:\n{full_tb}\n")
        state["error_log_file"] = str(fpath)
        logger.info("错误日志已写入: %s", fpath)
    except Exception:
        pass


def is_done() -> bool:
    """预加载是否已完成。"""
    return state["done"]


def get_chain():
    """获取已加载的 chain，未完成返回 None。"""
    return state["chain"]


def get_error() -> str:
    """获取错误信息（含异常类型和简短描述）。"""
    # 优先显示完整的 traceback（如果存在）
    tb = state.get("error_traceback", "")
    if tb:
        # 提取最后一行作为摘要
        lines = tb.strip().split("\n")
        last_line = lines[-1] if lines else ""
        return last_line.strip() or f"无法解析错误（traceback 存在但最后行为空）"
    msg = state.get("error")
    if msg:
        return msg
    # 既无 traceback 也无 error，但 done=True → 诊断信息
    if state.get("chain") is not None:
        return "预加载已完成但未被 UI 检测到（请刷新页面）"
    return "预加载线程已完成但未设置 chain（可能被静默终止）"


def get_error_detail() -> str:
    """获取完整的错误详情（含堆栈跟踪），供高级用户排查。"""
    tb = state.get("error_traceback", "")
    if tb:
        prefix = ""
        logf = state.get("error_log_file", "")
        if logf:
            prefix = f"（完整日志已写入: {logf}）\n\n"
        return prefix + tb
    logf = state.get("error_log_file", "")
    if logf:
        return f"完整日志已写入: {logf}\n\n{state.get('error') or '（无错误信息）'}"
    err = state.get("error")
    if err:
        return err
    if state.get("chain") is not None:
        return "预加载已成功完成，chain 实例已就绪。\n（可能是 UI 状态未及时刷新，请刷新页面重试）"
    return "预加载线程已完成但未捕获到任何异常。\n可能原因：线程被系统静默终止、内存不足、或子进程异常退出。"


def reset():
    """重置状态，用于重新加载。"""
    state["chain"] = None
    state["error"] = None
    state["error_traceback"] = ""
    state["error_log_file"] = ""
    state["done"] = False
    state["started"] = False
    state["loading"] = False

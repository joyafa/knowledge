"""
PyInstaller runtime hook for chromadb embedding functions.

问题：chromadb 在 chromadb/utils/embedding_functions/__init__.py 中使用
pkgutil.iter_modules() 扫描文件系统目录来动态发现子模块。PyInstaller 默认
将纯 Python 模块打包进 PYZ 归档（ZIP 格式），pkgutil.iter_modules 无法在
归档内进行目录扫描，导致所有 embedding function 子模块（包括关键的
ONNXMiniLM_L6_V2）未被注册到模块命名空间。

修复：在 chromadb 被导入之前，用 monkey-patch 拦截 pkgutil.iter_modules。
当检测到正在扫描 chromadb 的 embedding_functions 目录时，直接返回预置的
子模块列表，绕过文件系统扫描。
"""
import pkgutil

# ── chromadb embedding_functions/ 下全部 14 个子模块 ──
_CHROMADB_EF_MODULES = [
    "amazon_bedrock_embedding_function",
    "chroma_langchain_embedding_function",
    "cohere_embedding_function",
    "google_embedding_function",
    "huggingface_embedding_function",
    "instructor_embedding_function",
    "jina_embedding_function",
    "ollama_embedding_function",
    "onnx_mini_lm_l6_v2",
    "open_clip_embedding_function",
    "openai_embedding_function",
    "roboflow_embedding_function",
    "sentence_transformer_embedding_function",
    "text2vec_embedding_function",
]

_original_iter_modules = pkgutil.iter_modules


def _patched_iter_modules(path=None, prefix=""):
    """拦截 chromadb embedding_functions 目录扫描，返回硬编码模块列表。"""
    if path is not None:
        for p in path:
            p_str = str(p) if not isinstance(p, str) else p
            if "embedding_functions" in p_str and "chromadb" in p_str:
                for mod_name in _CHROMADB_EF_MODULES:
                    yield (None, mod_name, False)
                return
    yield from _original_iter_modules(path, prefix)


pkgutil.iter_modules = _patched_iter_modules

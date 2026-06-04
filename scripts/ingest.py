"""文档入库脚本。

扫描 knowledge/ 目录，加载文档文件，分块并向量化后存入 ChromaDB。
默认增量模式：仅处理新增/变更文件，跳过未修改文件。
使用 --full 可强制全量重建。
"""

import argparse
import os
import sys
from pathlib import Path

# 将项目根目录添加到 Python 路径
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

# 先检测本地模型路径，再决定是否需要 HF 镜像
from rag.config import detect_local_models
detect_local_models()

# 仅在未配置本地模型路径时才设置 HF 镜像（本地模型就绪时无需联网）
if not (os.environ.get("EMBEDDING_LOCAL_PATH") and os.environ.get("RERANKER_LOCAL_PATH")):
    os.environ.setdefault("HF_ENDPOINT", "https://hf-mirror.com")

from rag.loader import load_documents, SUPPORTED_EXTENSIONS
from rag.vectorstore import VectorStore, _compute_file_hash
from rag.config import get_config
from rag.logging_config import setup_logging, get_logger

logger = get_logger(__name__)


_HASH_CACHE_FILE = Path("./data/.ingest_hash_cache.json")


def _load_hash_cache() -> dict[str, dict]:
    """加载哈希缓存文件（{relative_path: {"mtime": float, "size": int, "hash": str}}）。"""
    if _HASH_CACHE_FILE.exists():
        try:
            import json
            return json.loads(_HASH_CACHE_FILE.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            pass
    return {}


def _save_hash_cache(cache: dict[str, dict]):
    """保存哈希缓存文件。"""
    _HASH_CACHE_FILE.parent.mkdir(parents=True, exist_ok=True)
    import json
    _HASH_CACHE_FILE.write_text(json.dumps(cache, ensure_ascii=False), encoding="utf-8")


def _scan_file_hashes(docs_dir: str) -> dict[str, str]:
    """扫描目录，返回 {relative_path: content_hash}（仅支持的文件类型）。

    增量优化：用 mtime+size 作为快速指纹，未变化的文件直接复用缓存的 MD5，避免重复读取。
    """
    docs_path = Path(docs_dir)
    if not docs_path.exists():
        return {}
    cache = _load_hash_cache()
    hashes = {}
    for doc_file in sorted(docs_path.rglob("*")):
        if not doc_file.is_file():
            continue
        if doc_file.suffix.lower() not in SUPPORTED_EXTENSIONS:
            continue
        if doc_file.name.lower() == "readme.md":
            continue
        rel = str(doc_file.relative_to(docs_path))
        stat = doc_file.stat()
        quick_key = f"{stat.st_mtime}:{stat.st_size}"
        # 快速指纹匹配 → 复用缓存的 MD5，跳过文件读取
        cached = cache.get(rel)
        if cached and cached.get("quick_key") == quick_key:
            hashes[rel] = cached["hash"]
        else:
            h = _compute_file_hash(str(doc_file))
            hashes[rel] = h
            cache[rel] = {"quick_key": quick_key, "hash": h}
    _save_hash_cache(cache)
    return hashes


def main():
    parser = argparse.ArgumentParser(description="知识库文档入库")
    parser.add_argument("--full", action="store_true",
                        help="全量重建（默认增量模式，仅处理变更文件）")
    args = parser.parse_args()

    setup_logging()

    config = get_config()
    knowledge_cfg = config.knowledge

    docs_dir = knowledge_cfg.docs_directory
    chunk_size = knowledge_cfg.chunk_size
    chunk_overlap = knowledge_cfg.chunk_overlap

    logger.info("正在扫描文档目录: %s", docs_dir)

    if args.full:
        # 全量模式：加载所有文件
        logger.info("模式: 全量重建")
        chunks = load_documents(docs_dir, chunk_size, chunk_overlap)
        if not chunks:
            logger.warning("未找到有效的文档。")
            return
        logger.info("共加载 %d 个文档块", len(chunks))

        vectorstore = VectorStore.from_config()
        count = vectorstore.add_documents(chunks)
        total = vectorstore.get_document_count()
        logger.info("入库完成！新增/更新 %d 个文档块，向量库共 %d 个文档块。", count, total)
        return

    # ── 增量模式 ──
    logger.info("模式: 增量更新（对比文件哈希）")

    # 1. 扫描当前磁盘文件哈希
    current_hashes = _scan_file_hashes(docs_dir)
    current_sources = set(current_hashes.keys())
    if not current_sources:
        logger.warning("未找到有效的文档。")
        return
    logger.info("磁盘文件: %d 个", len(current_sources))

    # 2. 获取向量库中已存在的文件哈希（一次 collection.get()，供哈希查询和孤儿清理复用）
    vectorstore = VectorStore.from_config()
    all_metadata = vectorstore._get_all_metadata()
    stored_hashes = vectorstore.get_file_hashes(all_metadata)
    logger.info("向量库已存文件: %d 个", len(stored_hashes))

    # 3. 对比：找出新增/变更文件
    new_files: set[str] = set()
    changed_files: set[str] = set()
    unchanged_files: set[str] = set()

    for src, h in current_hashes.items():
        if src not in stored_hashes:
            new_files.add(src)
        elif stored_hashes[src] != h:
            changed_files.add(src)
        else:
            unchanged_files.add(src)

    logger.info("文件比对结果:")
    logger.info("  新增: %d 个", len(new_files))
    logger.info("  变更: %d 个", len(changed_files))
    logger.info("  未变: %d 个", len(unchanged_files))

    # 4. 清理孤儿（磁盘已删除但向量库中仍残留）
    orphan_removed = vectorstore.cleanup_orphans(current_sources, all_metadata)

    # 5. 如果没有需要更新的文件
    changed_or_new = new_files | changed_files
    if not changed_or_new:
        if orphan_removed:
            logger.info("入库完成！仅清理了孤儿分块，所有文件均为最新。")
        else:
            logger.info("入库完成！没有文件发生变化，跳过向量化。")
        total = vectorstore.get_document_count()
        logger.info("向量库共 %d 个文档块。", total)
        return

    # 6. 仅加载变更/新增的文件
    for src in sorted(changed_or_new):
        logger.info("  %s %s", "[新增]" if src in new_files else "[变更]", src)

    chunks = load_documents(docs_dir, chunk_size, chunk_overlap,
                           file_filter=changed_or_new)
    if not chunks:
        logger.warning("变更文件中提取不到有效内容。")
        return
    logger.info("变更文件共产生 %d 个文档块", len(chunks))

    # 7. 删除旧分块 + 向量化新分块
    # 先删除变更文件的旧分块（新增文件无需删除）
    for src in changed_files:
        vectorstore.remove_document(src)

    # 构建 file_paths 映射供哈希存储
    docs_path = Path(docs_dir)
    file_paths = {src: str(docs_path / src) for src in changed_or_new}

    count = vectorstore.add_documents(chunks, file_paths=file_paths)

    total = vectorstore.get_document_count()
    logger.info("入库完成！新增/更新 %d 个文档块，向量库共 %d 个文档块。", count, total)


if __name__ == "__main__":
    main()

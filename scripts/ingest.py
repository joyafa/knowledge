"""文档入库脚本。

扫描 knowledge/ 目录，加载文档文件，分块并向量化后存入 ChromaDB。
支持增量更新（已入库的文档会被覆盖）。
"""

import os
import sys
from pathlib import Path

# 使用国内 HuggingFace 镜像
os.environ.setdefault("HF_ENDPOINT", "https://hf-mirror.com")

# 将项目根目录添加到 Python 路径
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from rag.loader import load_documents
from rag.vectorstore import VectorStore
from rag.config import get_config
from rag.logging_config import setup_logging, get_logger

logger = get_logger(__name__)


def main():
    setup_logging()

    config = get_config()
    knowledge_cfg = config.knowledge

    docs_dir = knowledge_cfg.docs_directory
    chunk_size = knowledge_cfg.chunk_size
    chunk_overlap = knowledge_cfg.chunk_overlap

    logger.info("正在扫描文档目录: %s", docs_dir)

    # 加载并分块
    chunks = load_documents(docs_dir, chunk_size, chunk_overlap)
    if not chunks:
        logger.warning("未找到有效的文档。请将 .md/.txt/.pdf 文件放入 knowledge/ 目录。")
        return

    logger.info("共加载 %d 个文档块", len(chunks))

    # 统计来源文件
    sources = set(chunk.metadata["source"] for chunk in chunks)
    logger.info("涉及 %d 个文件:", len(sources))
    for source in sorted(sources):
        logger.info("  - %s", source)

    # 向量化并存储
    logger.info("正在向量化并存入 ChromaDB...")
    vectorstore = VectorStore.from_config()
    count = vectorstore.add_documents(chunks)

    total = vectorstore.get_document_count()
    logger.info("入库完成！新增/更新 %d 个文档块，向量库共 %d 个文档块。", count, total)


if __name__ == "__main__":
    main()

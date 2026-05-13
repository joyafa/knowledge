"""清空向量库脚本。

删除 ChromaDB 中的所有文档数据。
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from rag.vectorstore import VectorStore
from rag.logging_config import setup_logging, get_logger

logger = get_logger(__name__)


def main():
    setup_logging()

    vectorstore = VectorStore.from_config()
    count = vectorstore.get_document_count()

    if count == 0:
        logger.info("向量库已经是空的，无需清空。")
        return

    confirm = input(f"确认清空向量库？（当前 {count} 个文档块）[y/N]: ")
    if confirm.strip().lower() != "y":
        logger.info("已取消。")
        return

    vectorstore.clear()
    logger.info("已清空向量库（删除了 %d 个文档块）。", count)


if __name__ == "__main__":
    main()

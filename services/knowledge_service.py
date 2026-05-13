"""知识库服务模块。

提供文档内容读取、元数据查询等服务函数。
"""

from pathlib import Path
from typing import Optional

from rag.logging_config import get_logger

logger = get_logger(__name__)

SUPPORTED_EXTENSIONS = {".md", ".txt", ".pdf"}


def read_full_content(docs_dir: str, relative_path: str) -> Optional[str]:
    """读取文档全文内容（用于预览）。

    Args:
        docs_dir: 文档根目录
        relative_path: 文档相对路径

    Returns:
        文档全文内容，失败返回 None
    """
    file_path = Path(docs_dir) / relative_path
    if not file_path.exists():
        return None

    try:
        ext = file_path.suffix.lower()
        if ext == ".pdf":
            try:
                import pymupdf
                doc = pymupdf.open(str(file_path))
                content = "\n\n".join(page.get_text() for page in doc)
                doc.close()
                return content
            except Exception:
                pass
        else:
            return file_path.read_text(encoding="utf-8")
    except Exception as e:
        logger.warning("读取文件失败 %s: %s", file_path, e)
        return None

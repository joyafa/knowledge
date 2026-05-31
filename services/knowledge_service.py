"""知识库服务模块。

提供文档内容读取、元数据查询等服务函数。
"""

from pathlib import Path
from typing import Optional

from rag.logging_config import get_logger

logger = get_logger(__name__)

# 编码探测顺序（中文 Windows 源码常见 GBK/GB2312 编码）
_TEXT_ENCODINGS = ["utf-8", "gbk", "gb2312", "gb18030", "latin-1"]


def _read_text_file(file_path: Path) -> str:
    """读取文本文件，自动探测编码。"""
    raw = file_path.read_bytes()
    for enc in _TEXT_ENCODINGS:
        try:
            return raw.decode(enc)
        except (UnicodeDecodeError, LookupError):
            continue
    return raw.decode("utf-8", errors="replace")


def read_full_content(docs_dir: str, relative_path: str) -> Optional[str]:
    """读取文档全文内容（用于预览）。

    Args:
        docs_dir: 文档根目录
        relative_path: 文档相对路径

    Returns:
        文档全文内容，失败返回 None
    """
    # 安全校验：防止路径遍历攻击（../../etc/passwd）
    base_dir = Path(docs_dir).resolve()
    file_path = (base_dir / relative_path).resolve()
    if not str(file_path).startswith(str(base_dir)):
        logger.warning("拒绝路径遍历请求: %s", relative_path)
        return None
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
            return _read_text_file(file_path)
    except Exception as e:
        logger.warning("读取文件失败 %s: %s", file_path, e)
        return None

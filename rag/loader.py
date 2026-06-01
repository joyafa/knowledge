"""文档加载与分块模块。

支持格式：Markdown (.md)、纯文本 (.txt)、PDF (.pdf)、
          C/C++ 源码 (.c, .cc, .cpp, .cxx, .h, .hpp, .hxx)
递归扫描 knowledge/ 目录，按语义切分，保留元数据。
"""

import os
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

from rag.config import load_config
from rag.logging_config import get_logger

logger = get_logger(__name__)


# 支持的文件扩展名
SUPPORTED_EXTENSIONS = {
    ".md", ".txt", ".pdf",
    ".c", ".cc", ".cpp", ".cxx", ".h", ".hpp", ".hxx", 
}


@dataclass
class DocumentChunk:
    """文档分块。"""
    content: str
    metadata: dict = field(default_factory=dict)


def _split_by_headers(text: str, max_chunk_size: int, overlap: int) -> list[str]:
    """按 Markdown 标题切分，超长段落再按语义边界切分。

    优先按 ## 二级标题切分，保留标题作为上下文。
    对代码块保持完整，不从中截断。
    """
    lines = text.split("\n")
    sections: list[str] = []
    current_section: list[str] = []
    in_code_block = False

    for line in lines:
        # 追踪代码块边界
        if line.strip().startswith("```"):
            in_code_block = not in_code_block

        # 不在代码块内时，按二级标题切分
        if not in_code_block and line.startswith("## ") and current_section:
            sections.append("\n".join(current_section))
            current_section = [line]
        else:
            current_section.append(line)

    if current_section:
        sections.append("\n".join(current_section))

    # 对超长 section 按段落再切分（保持代码块完整）
    chunks: list[str] = []
    for section in sections:
        if len(section) <= max_chunk_size:
            chunks.append(section)
        else:
            paragraphs = section.split("\n\n")
            current_chunk: list[str] = []
            current_len = 0
            in_block = False

            for para in paragraphs:
                para_len = len(para)
                # 检测代码块开始/结束
                if para.strip().startswith("```"):
                    in_block = not in_block

                if current_len + para_len > max_chunk_size and current_chunk and not in_block:
                    chunks.append("\n\n".join(current_chunk))
                    if overlap > 0 and current_chunk:
                        overlap_text = "\n\n".join(current_chunk)
                        overlap_part = overlap_text[-overlap:]
                        current_chunk = [overlap_part, para]
                        current_len = len(overlap_part) + para_len
                    else:
                        current_chunk = [para]
                        current_len = para_len
                else:
                    current_chunk.append(para)
                    current_len += para_len

            if current_chunk:
                chunks.append("\n\n".join(current_chunk))

    return chunks


def _extract_title(text: str) -> str:
    """从文档内容提取第一个标题。"""
    for line in text.split("\n"):
        line = line.strip()
        if line.startswith("# "):
            return line[2:].strip()
    return ""


def _load_pdf(file_path: Path) -> str:
    """提取 PDF 文件文本内容。"""
    try:
        import pymupdf
    except ImportError:
        try:
            import fitz as pymupdf
        except ImportError:
            raise ImportError(
                "读取 PDF 需要安装 pymupdf，请运行: pip install pymupdf"
            )

    doc = pymupdf.open(str(file_path))
    pages = []
    for page in doc:
        pages.append(page.get_text())
    doc.close()
    return "\n\n".join(pages)


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
    # 最终兜底：忽略无法解码的字节
    return raw.decode("utf-8", errors="replace")


def _load_file(file_path: Path) -> str:
    """根据文件类型加载文本内容。"""
    ext = file_path.suffix.lower()

    if ext == ".pdf":
        return _load_pdf(file_path)
    else:
        return _read_text_file(file_path)


def load_documents(
    docs_dir: str,
    chunk_size: int = 500,
    chunk_overlap: int = 50,
    file_filter: Optional[set] = None,
) -> list[DocumentChunk]:
    """扫描目录并加载所有支持的文档文件，返回分块列表。

    支持格式：.md、.txt、.pdf、C/C++ 源码（.c/.cc/.cpp/.cxx/.h/.hpp/.hxx）

    Args:
        docs_dir: 文档目录路径
        chunk_size: 分块最大字符数
        chunk_overlap: 分块重叠字符数
        file_filter: 可选的文件名集合，仅加载这些文件

    Returns:
        文档分块列表
    """
    docs_path = Path(docs_dir)
    if not docs_path.exists():
        raise FileNotFoundError(f"文档目录不存在: {docs_dir}")

    all_chunks: list[DocumentChunk] = []
    loaded_count = 0

    for doc_file in sorted(docs_path.rglob("*")):
        if not doc_file.is_file():
            continue
        if doc_file.suffix.lower() not in SUPPORTED_EXTENSIONS:
            continue
        if doc_file.name.lower() == "readme.md":
            continue
        if file_filter is not None and doc_file.name not in file_filter:
            continue

        try:
            text = _load_file(doc_file)
        except Exception as e:
            logger.warning("无法读取文件 %s: %s", doc_file, e)
            continue

        if not text.strip():
            continue

        # 跳过内容过短的文件（只有标题和时间戳的空壳文档）
        if len(text.strip()) < 100:
            logger.debug("跳过内容过短的文件: %s", doc_file)
            continue

        title = _extract_title(text)
        if not title:
            title = doc_file.stem
        relative_path = str(doc_file.relative_to(docs_path))
        chunks = _split_by_headers(text, chunk_size, chunk_overlap)

        for i, chunk in enumerate(chunks):
            if not chunk.strip():
                continue
            all_chunks.append(DocumentChunk(
                content=chunk.strip(),
                metadata={
                    "source": relative_path,
                    "title": title,
                    "chunk_index": i,
                    "file_type": doc_file.suffix.lower(),
                }
            ))
        loaded_count += 1

    logger.info("文档加载完成: %d 个文件 → %d 个文档块", loaded_count, len(all_chunks))
    return all_chunks


def get_knowledge_files_meta(docs_dir: str) -> list[dict]:
    """获取知识库文件元数据（不加载全文内容）。

    Returns:
        文件元数据列表：path, title, size, modified_time, file_type
    """
    docs_path = Path(docs_dir)
    if not docs_path.exists():
        return []

    files = []
    for doc_file in sorted(docs_path.rglob("*")):
        if not doc_file.is_file():
            continue
        if doc_file.suffix.lower() not in SUPPORTED_EXTENSIONS:
            continue
        if doc_file.name.lower() == "readme.md":
            continue

        # 只读前几行提取标题，不加载全文
        try:
            if doc_file.suffix.lower() == ".pdf":
                title = doc_file.stem
                size = doc_file.stat().st_size
            else:
                head = _read_text_file(doc_file)[:2000]
                title = _extract_title(head) or doc_file.stem
                size = doc_file.stat().st_size
        except Exception:
            title = doc_file.stem
            size = 0

        _icon_map = {
            "pdf": "📕", "txt": "📝", "md": "📘",
            "c": "⚙️", "cc": "⚙️", "cpp": "⚙️", "cxx": "⚙️",
            "h": "📐", "hpp": "📐", "hxx": "📐",
        }
        icon = _icon_map.get(doc_file.suffix.lower().lstrip("."), "📄")
        files.append({
            "path": str(doc_file.relative_to(docs_path)),
            "name": doc_file.name,
            "title": title,
            "size": size,
            "modified_time": doc_file.stat().st_mtime,
            "file_type": doc_file.suffix.lower().strip("."),
            "icon": icon,
        })

    return files


if __name__ == "__main__":
    config = load_config()
    knowledge_cfg = config["knowledge"]
    chunks = load_documents(
        knowledge_cfg["docs_directory"],
        knowledge_cfg["chunk_size"],
        knowledge_cfg["chunk_overlap"],
    )
    print(f"共加载 {len(chunks)} 个文档块")
    for chunk in chunks[:3]:
        print(f"\n--- {chunk.metadata['source']} (块 {chunk.metadata['chunk_index']}) ---")
        print(chunk.content[:200])

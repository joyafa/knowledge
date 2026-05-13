"""文档加载器测试。"""

import tempfile
from pathlib import Path

import pytest

from rag.loader import (
    _split_by_headers,
    _extract_title,
    DocumentChunk,
    get_knowledge_files_meta,
)


class TestSplitByHeaders:
    """分块逻辑测试。"""

    def test_simple_split(self):
        text = """## Section 1
content one
## Section 2
content two"""
        chunks = _split_by_headers(text, 500, 0)
        assert len(chunks) == 2
        assert "Section 1" in chunks[0]
        assert "Section 2" in chunks[1]

    def test_no_headers(self):
        text = "just some content without headers"
        chunks = _split_by_headers(text, 500, 0)
        assert len(chunks) == 1
        assert chunks[0] == text

    def test_chunk_overflow(self):
        text = "## Section\n" + "A" * 300 + "\n\n" + "B" * 300
        chunks = _split_by_headers(text, 400, 0)
        # 两段之间有空行，会被拆分成多个 chunk
        assert len(chunks) >= 2

    def test_overlap(self):
        text = "## Section\n" + "A" * 300 + "\n\n" + "B" * 300
        chunks = _split_by_headers(text, 400, 50)
        # 有 overlap 时应该在 chunk 边界有重叠内容
        assert len(chunks) >= 2

    def test_code_block_preserved(self):
        text = """## Code Example
Some text before code.

```
int main() {
    return 0;
}
```

## Next Section
More content."""
        chunks = _split_by_headers(text, 1000, 0)
        # 代码块不应该在中间被截断
        for chunk in chunks:
            if "```" in chunk:
                # 代码块标记应该成对出现
                count = chunk.count("```")
                assert count % 2 == 0


class TestExtractTitle:
    """标题提取测试。"""

    def test_extract_h1(self):
        text = "# My Title\n## Subtitle\ncontent"
        assert _extract_title(text) == "My Title"

    def test_no_title(self):
        text = "just some text\nno headers"
        assert _extract_title(text) == ""

    def test_multiple_h1(self):
        text = "# First\n# Second"
        assert _extract_title(text) == "First"


class TestGetKnowledgeFilesMeta:
    """文件元数据获取测试。"""

    def test_empty_dir(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            files = get_knowledge_files_meta(tmpdir)
            assert files == []

    def test_with_md_files(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            md_file = Path(tmpdir) / "test.md"
            md_file.write_text("# Test Title\ncontent here", encoding="utf-8")

            txt_file = Path(tmpdir) / "notes.txt"
            txt_file.write_text("plain notes", encoding="utf-8")

            # 不应该被包含的文件
            readme = Path(tmpdir) / "README.md"
            readme.write_text("# README", encoding="utf-8")

            files = get_knowledge_files_meta(tmpdir)
            file_names = {f["name"] for f in files}

            assert "test.md" in file_names
            assert "notes.txt" in file_names
            assert "README.md" not in file_names

    def test_title_extraction_from_meta(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            md_file = Path(tmpdir) / "api.md"
            md_file.write_text("# API Reference\ncontent", encoding="utf-8")

            files = get_knowledge_files_meta(tmpdir)
            assert len(files) == 1
            assert files[0]["title"] == "API Reference"
            assert files[0]["file_type"] == "md"
            assert "content" not in files[0]  # 不应包含全文


class TestDocumentChunk:
    """DocumentChunk 数据结构测试。"""

    def test_default_metadata(self):
        chunk = DocumentChunk(content="test")
        assert chunk.content == "test"
        assert chunk.metadata == {}

    def test_with_metadata(self):
        chunk = DocumentChunk(
            content="test content",
            metadata={"source": "doc.md", "chunk_index": 0},
        )
        assert chunk.metadata["source"] == "doc.md"
        assert chunk.metadata["chunk_index"] == 0

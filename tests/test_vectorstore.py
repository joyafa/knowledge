"""向量库服务测试。"""

import tempfile
import shutil
from pathlib import Path

import pytest

from rag.vectorstore import VectorStore
from rag.loader import DocumentChunk


class TestVectorStore:
    """向量库管理测试。"""

    def setup_method(self):
        self._tmpdir = tempfile.mkdtemp()
        self._persist_dir = Path(self._tmpdir) / "chroma_test"

    def teardown_method(self):
        shutil.rmtree(self._tmpdir, ignore_errors=True)

    def _create_store(self, collection_name="test_collection") -> VectorStore:
        return VectorStore(
            persist_directory=str(self._persist_dir),
            collection_name=collection_name,
            embedding_model="shibing624/text2vec-base-chinese",
        )

    def test_init_creates_directories(self):
        store = self._create_store()
        # 目录在首次访问 ChromaDB 客户端时才创建（延迟初始化）
        store._get_client()
        assert self._persist_dir.exists()

    def test_get_document_count_empty(self):
        store = self._create_store()
        assert store.get_document_count() == 0

    def test_add_and_count_documents(self):
        store = self._create_store()
        chunks = [
            DocumentChunk(content="测试文档内容一", metadata={"source": "test.md", "chunk_index": 0, "title": "Test"}),
            DocumentChunk(content="测试文档内容二", metadata={"source": "test.md", "chunk_index": 1, "title": "Test"}),
        ]
        count = store.add_documents(chunks)
        assert count == 2
        assert store.get_document_count() == 2

    def test_add_duplicate_documents(self):
        """重复添加同名文档应覆盖而非重复。"""
        store = self._create_store()
        chunks = [
            DocumentChunk(content="版本1", metadata={"source": "doc.md", "chunk_index": 0, "title": "Doc"}),
        ]
        store.add_documents(chunks)
        assert store.get_document_count() == 1

        # 再次添加同名文档
        chunks_v2 = [
            DocumentChunk(content="版本2", metadata={"source": "doc.md", "chunk_index": 0, "title": "Doc"}),
        ]
        store.add_documents(chunks_v2)
        assert store.get_document_count() == 1

    def test_get_stats(self):
        store = self._create_store()
        chunks = [
            DocumentChunk(content="文件1内容", metadata={"source": "file1.md", "chunk_index": 0, "title": "文件1"}),
            DocumentChunk(content="文件1内容续", metadata={"source": "file1.md", "chunk_index": 1, "title": "文件1"}),
            DocumentChunk(content="文件2内容", metadata={"source": "file2.md", "chunk_index": 0, "title": "文件2"}),
        ]
        store.add_documents(chunks)

        stats = store.get_stats()
        assert stats["total_chunks"] == 3
        assert stats["total_files"] == 2
        assert stats["collection_name"] == "test_collection"

    def test_search_returns_results(self):
        store = self._create_store()
        chunks = [
            DocumentChunk(content="TcpConnection 类用于管理 TCP 连接", metadata={"source": "tcp.md", "chunk_index": 0, "title": "TCP"}),
            DocumentChunk(content="EventLoop 是事件循环的核心", metadata={"source": "event.md", "chunk_index": 0, "title": "Event"}),
        ]
        store.add_documents(chunks)

        results = store.search("TcpConnection", top_k=2)
        assert len(results) > 0
        # 最相关的结果应包含 TcpConnection
        assert "TcpConnection" in results[0]["content"]

    def test_search_empty_collection(self):
        store = self._create_store()
        results = store.search("任何查询")
        assert results == []

    def test_remove_document(self):
        store = self._create_store()
        chunks = [
            DocumentChunk(content="要删除的内容", metadata={"source": "remove_me.md", "chunk_index": 0, "title": "Remove"}),
            DocumentChunk(content="保留的内容", metadata={"source": "keep.md", "chunk_index": 0, "title": "Keep"}),
        ]
        store.add_documents(chunks)
        assert store.get_document_count() == 2

        removed = store.remove_document("remove_me.md")
        assert removed == 1
        assert store.get_document_count() == 1

    def test_list_and_switch_collections(self):
        store = self._create_store("coll_a")
        chunks_a = [DocumentChunk(content="集合A文档", metadata={"source": "a.md", "chunk_index": 0, "title": "A"})]
        store.add_documents(chunks_a)

        store.switch_collection("coll_b")
        chunks_b = [DocumentChunk(content="集合B文档", metadata={"source": "b.md", "chunk_index": 0, "title": "B"})]
        store.add_documents(chunks_b)

        collections = store.list_collections()
        assert "coll_a" in collections
        assert "coll_b" in collections

    def test_clear_collection(self):
        store = self._create_store()
        chunks = [DocumentChunk(content="测试", metadata={"source": "test.md", "chunk_index": 0, "title": "Test"})]
        store.add_documents(chunks)
        assert store.get_document_count() == 1

        store.clear()
        assert store.get_document_count() == 0

    def test_get_all_documents(self):
        store = self._create_store()
        chunks = [
            DocumentChunk(content="Doc1", metadata={"source": "file1.md", "chunk_index": 0, "title": "F1"}),
            DocumentChunk(content="Doc2", metadata={"source": "file2.md", "chunk_index": 0, "title": "F2"}),
        ]
        store.add_documents(chunks)

        docs = store.get_all_documents()
        assert len(docs) == 2
        assert docs[0]["content"] == "Doc1"
        assert docs[1]["content"] == "Doc2"
        assert "metadata" in docs[0]

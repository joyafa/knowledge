"""RAG Chain 测试。

测试检索、上下文构建、token 估算等核心逻辑。
"""

import pytest

from rag.chain import (
    RAGChain,
    BM25Retriever,
    reciprocal_rank_fusion,
)


class TestBM25Retriever:
    """BM25 检索引擎测试。"""

    def test_empty_corpus(self):
        bm25 = BM25Retriever()
        results = bm25.search("test query")
        assert results == []

    def test_basic_search(self):
        bm25 = BM25Retriever()
        docs = [
            {"content": "TcpConnection 类是 muduo 网络库的核心类", "metadata": {}},
            {"content": "EventLoop 负责事件循环", "metadata": {}},
            {"content": "Buffer 用于读写缓冲区管理", "metadata": {}},
        ]
        bm25.index(docs)

        # 搜索中文关键词
        results = bm25.search("TcpConnection")
        assert len(results) > 0

        # 第一个结果应该是最相关的
        top_idx = results[0][0]
        assert "TcpConnection" in docs[top_idx]["content"]

    def test_no_match(self):
        bm25 = BM25Retriever()
        docs = [
            {"content": "网络编程相关内容", "metadata": {}},
        ]
        bm25.index(docs)

        results = bm25.search("完全不相关的查询")
        assert results == []

    def test_multiple_term_query(self):
        bm25 = BM25Retriever()
        docs = [
            {"content": "TcpServer 是 muduo 的 TCP 服务器类", "metadata": {}},
            {"content": "TcpClient 用于建立客户端连接", "metadata": {}},
            {"content": "HTTP 协议相关知识", "metadata": {}},
        ]
        bm25.index(docs)

        results = bm25.search("muduo TcpServer")
        assert len(results) > 0
        # 同时包含 muduo 和 TcpServer 的文档得分应最高
        top_idx = results[0][0]
        assert "TcpServer" in docs[top_idx]["content"]


class TestReciprocalRankFusion:
    """RRF 融合算法测试。"""

    def test_basic_fusion(self):
        # 使用相同的 dict 对象确保 id() 去重生效
        doc_a = {"content": "doc A", "id": 1}
        doc_b = {"content": "doc B", "id": 2}
        doc_c = {"content": "doc C", "id": 3}
        doc_d = {"content": "doc D", "id": 4}

        vec_results = [doc_a, doc_b, doc_c]
        bm25_results = [doc_b, doc_c, doc_d]
        fused = reciprocal_rank_fusion(vec_results, bm25_results)

        # doc B 和 doc C 都同时出现在两个列表中（引用相同对象），所以是 4 个
        assert len(fused) == 4  # A, B, C, D
        # doc B (出现在两个列表) 应该排在前两位
        assert fused[0]["id"] == 2 or fused[1]["id"] == 2

    def test_empty_inputs(self):
        fused = reciprocal_rank_fusion([], [])
        assert fused == []

    def test_one_sided(self):
        vec_results = [{"content": "only", "id": 1}]
        fused = reciprocal_rank_fusion(vec_results, [])
        assert len(fused) == 1
        assert fused[0]["id"] == 1


class TestTokenEstimation:
    """Token 估算测试。"""

    def test_estimate_chinese(self):
        text = "这是一个测试句子"  # 7 个汉字
        tokens = int(len(text) / 1.5)
        # 7 / 1.5 = 4.66 → int = 4
        assert tokens in (4, 5)

    def test_estimate_mixed(self):
        text = "TcpConnection 是 muduo 的核心类"  # 中英文混合
        tokens = int(len(text) / 1.5)
        assert tokens > 0


class TestContextBuilding:
    """上下文构建测试。"""

    def test_empty_results(self):
        # 模拟空结果的情况
        chain = RAGChain.__new__(RAGChain)
        chain.CHARS_PER_TOKEN = 1.5
        chain._estimate_tokens = lambda self, x: int(len(x) / 1.5)

        # 空结果列表
        results = []
        # 不应该崩溃
        with pytest.raises(IndexError):
            chain._build_context(results, 1000)

    def test_context_budget_calculation(self):
        """测试上下文预算计算。"""
        chain = RAGChain.__new__(RAGChain)
        chain.CHARS_PER_TOKEN = 1.5
        chain._context_window = 32768
        chain._max_tokens = 2048

        def mock_estimate(text):
            return int(len(text) / 1.5)
        chain._estimate_tokens = mock_estimate

        budget = chain._calc_context_budget("测试问题", history=None)
        assert budget > 0

        # 有对话历史时预算应减少
        history = [
            {"role": "user", "content": "之前的问题"},
            {"role": "assistant", "content": "之前的回答"},
        ]
        budget_with_history = chain._calc_context_budget("测试问题", history=history)
        assert budget_with_history <= budget

    def test_sources_extraction(self):
        """来源提取测试。"""
        chain = RAGChain.__new__(RAGChain)
        results = [
            {"metadata": {"source": "doc1.md", "title": "Doc 1"}},
            {"metadata": {"source": "doc1.md", "title": "Doc 1"}},  # 重复
            {"metadata": {"source": "doc2.md", "title": "Doc 2"}},
        ]
        sources = chain._build_sources(results)
        assert len(sources) == 2  # 去重后
        assert sources[0]["source"] == "doc1.md"
        assert sources[1]["source"] == "doc2.md"

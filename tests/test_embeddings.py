"""Embedding 函数测试。"""

import pytest

from rag.embeddings import ChineseEmbeddingFunction


class TestChineseEmbeddingFunction:
    """中文 Embedding 函数测试。"""

    def test_init_default(self):
        emb_fn = ChineseEmbeddingFunction()
        assert emb_fn._model_name == "shibing624/text2vec-base-chinese"
        assert emb_fn._model is None  # 延迟加载

    def test_init_with_local_path(self):
        emb_fn = ChineseEmbeddingFunction(
            model_name="shibing624/text2vec-base-chinese",
            local_path="/path/to/local/model",
        )
        assert emb_fn._model_name == "/path/to/local/model"

    def test_lazy_loading(self):
        """模型应延迟加载，首次调用 __call__ 时才实例化。"""
        emb_fn = ChineseEmbeddingFunction()
        assert emb_fn._model is None

        # 不实际加载模型，只验证接口
        # 实际加载需要联网下载 400MB 模型，不适合单元测试

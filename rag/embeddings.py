"""向量化模块。

封装 sentence-transformers 中文 embedding 模型为 ChromaDB 兼容的 embedding function。
"""

import os
from pathlib import Path
from typing import Optional

from chromadb.api.types import EmbeddingFunction, Documents

from rag.logging_config import get_logger

logger = get_logger(__name__)


class ChineseEmbeddingFunction(EmbeddingFunction):
    """基于 sentence-transformers 的中文 embedding 函数。

    支持两种加载方式：
    - 在线：传入 HuggingFace 模型名（如 shibing624/text2vec-base-chinese）
    - 离线：传入本地模型目录路径
    """

    def __init__(self, model_name: str = "shibing624/text2vec-base-chinese", local_path: str = ""):
        self._model_name = local_path if local_path else model_name
        self._model: Optional[object] = None

    def _get_model(self):
        """延迟加载模型，带进度提示。支持离线本地加载。"""
        if self._model is None:
            from sentence_transformers import SentenceTransformer
            logger.info("正在加载 Embedding 模型: %s", self._model_name)
            if self._model_name and Path(self._model_name).exists():
                # 本地路径：离线加载，禁止联网
                logger.info("（从本地路径离线加载）")
                self._model = SentenceTransformer(self._model_name, local_files_only=True)
            else:
                logger.info("（首次运行需下载模型约 400MB，请耐心等待...）")
                self._model = SentenceTransformer(self._model_name)
            logger.info("Embedding 模型加载完成。")
        return self._model

    def __call__(self, input: Documents) -> list[list[float]]:
        """将文档列表转换为向量列表。"""
        model = self._get_model()
        logger.debug("正在向量化 %d 个文档块...", len(input))
        embeddings = model.encode(input, show_progress_bar=True)
        logger.debug("向量化完成，输出维度: %s", embeddings.shape)
        return embeddings.tolist()

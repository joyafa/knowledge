"""向量化模块。

封装 sentence-transformers 中文 embedding 模型为 ChromaDB 兼容的 embedding function。
输出向量经过 L2 归一化，使得平方 L2 距离在 [0, 4] 区间，便于设定合理阈值。
"""

import os
from pathlib import Path
from typing import Optional

import numpy as np
from chromadb.api.types import EmbeddingFunction, Documents

from rag.logging_config import get_logger

logger = get_logger(__name__)


def _patch_sentence_transformers():
    """修复 sentence_transformers 对包元数据 Home-page 为 None 时的崩溃。

    sentence_transformers.util.check_package_availability 通过
    importlib.metadata.metadata() 获取包元数据，但某些包（如 datasets）的
    Home-page 字段可能为 None，导致 `owner in meta["Home-page"]` 抛出：
        TypeError: argument of type 'NoneType' is not iterable

    此补丁包装 importlib.metadata.metadata()，确保返回的元数据中
    Home-page 等关键字段不会为 None。
    """
    import importlib.metadata
    _original_metadata = importlib.metadata.metadata

    def _safe_metadata(package_name):
        meta = _original_metadata(package_name)
        # 确保关键字段不会是 None，避免 sentence_transformers 崩溃
        for key in ("Home-page", "Author", "Author-email", "Summary"):
            if meta.get(key) is None:
                meta[key] = ""
        return meta

    importlib.metadata.metadata = _safe_metadata


# 在导入 SentenceTransformer 之前应用补丁
_patch_sentence_transformers()


class ChineseEmbeddingFunction(EmbeddingFunction):
    """基于 sentence-transformers 的中文 embedding 函数。

    支持两种加载方式：
    - 在线：传入 HuggingFace 模型名（如 shibing624/text2vec-base-chinese）
    - 离线：传入本地模型目录路径

    输出向量经 L2 归一化，位于单位球面上。
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
        """将文档列表转换为 L2 归一化的向量列表。

        归一化后向量位于单位球面上，平方 L2 距离 ∈ [0, 4]，
        可使用合理的距离阈值（~1.5）过滤低相关度结果。
        """
        model = self._get_model()
        logger.debug("正在向量化 %d 个文档块...", len(input))
        embeddings = model.encode(input, show_progress_bar=True, normalize_embeddings=True)
        logger.debug("向量化完成（已 L2 归一化），输出维度: %s", embeddings.shape)
        return embeddings.tolist()

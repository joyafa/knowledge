"""健康检查 API 模块。

提供 /health 端点用于监控和就绪探针。
"""

import time
from typing import Any

from rag import __version__
from rag.logging_config import get_logger

logger = get_logger(__name__)


def check_llm_connectivity(config) -> dict[str, Any]:
    """检查 LLM API 连通性。"""
    try:
        from openai import OpenAI
        client = OpenAI(
            base_url=config.llm.api_base,
            api_key=config.llm.api_key,
        )
        start = time.time()
        # 仅查询模型列表验证连通性
        client.models.list()
        latency = (time.time() - start) * 1000
        return {"status": "healthy", "latency_ms": round(latency, 1)}
    except Exception as e:
        return {"status": "unhealthy", "error": str(e)}


def check_vectorstore(config) -> dict[str, Any]:
    """检查向量库状态。"""
    try:
        from rag.vectorstore import VectorStore
        vs = VectorStore.from_config()
        count = vs.get_document_count()
        return {"status": "healthy", "document_count": count}
    except Exception as e:
        return {"status": "unhealthy", "error": str(e)}


def check_embedding(config) -> dict[str, Any]:
    """检查 Embedding 模型状态。"""
    try:
        from rag.embeddings import ChineseEmbeddingFunction
        emb_fn = ChineseEmbeddingFunction(
            config.embedding.model,
            config.embedding.local_path,
        )
        emb_fn._get_model()
        return {"status": "healthy", "model": config.embedding.model}
    except Exception as e:
        return {"status": "unhealthy", "error": str(e)}


def get_health_status() -> dict[str, Any]:
    """获取完整健康检查状态。"""
    from rag.config import get_config
    config = get_config()

    llm_status = check_llm_connectivity(config)
    vs_status = check_vectorstore(config)
    emb_status = check_embedding(config)

    all_healthy = all(
        s["status"] == "healthy"
        for s in [llm_status, vs_status, emb_status]
    )

    return {
        "status": "healthy" if all_healthy else "degraded",
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "components": {
            "llm": llm_status,
            "vectorstore": vs_status,
            "embedding": emb_status,
        },
        "version": __version__,
    }

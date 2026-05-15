"""ChromaDB 向量库管理模块。

提供向量库的初始化、文档添加、相似度检索和持久化功能。
支持全局单例缓存，避免重复加载 embedding 模型。
"""

from pathlib import Path
from typing import Optional

import chromadb

from rag.config import load_config
from rag.embeddings import ChineseEmbeddingFunction
from rag.loader import DocumentChunk
from rag.logging_config import get_logger

logger = get_logger(__name__)

# 全局缓存：避免每次创建新实例时重新加载 embedding 模型
_cached_vectorstore: Optional["VectorStore"] = None
_cached_config_key: Optional[str] = None


class VectorStore:
    """ChromaDB 向量库管理器。"""

    def __init__(
        self,
        persist_directory: str,
        collection_name: str,
        embedding_model: str = "shibing624/text2vec-base-chinese",
        embedding_local_path: str = "",
    ):
        self._persist_directory = persist_directory
        self._collection_name = collection_name
        self._embedding_fn = ChineseEmbeddingFunction(embedding_model, embedding_local_path)
        self._client: Optional[chromadb.ClientAPI] = None
        self._collection = None

    def _get_client(self) -> chromadb.ClientAPI:
        """获取 ChromaDB 客户端（延迟初始化）。"""
        if self._client is None:
            Path(self._persist_directory).mkdir(parents=True, exist_ok=True)
            self._client = chromadb.PersistentClient(path=self._persist_directory)
        return self._client

    def _get_collection(self):
        """获取或创建集合（内部使用，外部请用 get_collection）。"""
        if self._collection is None:
            client = self._get_client()
            self._collection = client.get_or_create_collection(
                name=self._collection_name,
                embedding_function=self._embedding_fn,
            )
        return self._collection

    def get_collection(self):
        """获取 ChromaDB 集合实例（公开接口）。"""
        return self._get_collection()

    def get_all_documents(self) -> list[dict]:
        """获取向量库中所有文档块。

        Returns:
            [{"content": str, "metadata": dict}, ...]
        """
        collection = self._get_collection()
        all_data = collection.get()
        documents = []
        if all_data["documents"] and all_data["metadatas"]:
            for i in range(len(all_data["documents"])):
                documents.append({
                    "content": all_data["documents"][i],
                    "metadata": all_data["metadatas"][i] if all_data["metadatas"] else {},
                })
        return documents

    def list_collections(self) -> list[str]:
        """列出所有集合名称（支持多知识库）。"""
        client = self._get_client()
        return [c.name for c in client.list_collections()]

    def switch_collection(self, collection_name: str):
        """切换到指定集合。"""
        self._collection_name = collection_name
        self._collection = None
        logger.info("切换到集合: %s", collection_name)

    def add_documents(self, chunks: list[DocumentChunk]) -> int:
        """将文档分块添加到向量库。"""
        if not chunks:
            return 0

        collection = self._get_collection()
        ids = []
        documents = []
        metadatas = []

        for i, chunk in enumerate(chunks):
            chunk_id = f"{chunk.metadata['source']}_{chunk.metadata['chunk_index']}"
            ids.append(chunk_id)
            documents.append(chunk.content)
            metadatas.append(chunk.metadata)

        # 先删除已存在的同名文档（支持增量更新）
        existing = collection.get(ids=ids)
        if existing["ids"]:
            collection.delete(ids=existing["ids"])

        collection.add(ids=ids, documents=documents, metadatas=metadatas)
        logger.info("向量库入库: %d 个文档块", len(ids))
        return len(ids)

    def remove_document(self, source: str) -> int:
        """按来源路径删除文档的所有分块。"""
        collection = self._get_collection()
        results = collection.get(where={"source": source})
        if results["ids"]:
            collection.delete(ids=results["ids"])
            logger.info("已删除文档: %s (%d 个分块)", source, len(results["ids"]))
            return len(results["ids"])
        return 0

    def search(self, query: str, top_k: int = 5, metadata_filter: Optional[dict] = None) -> list[dict]:
        """相似度检索（支持元数据过滤）。"""
        collection = self._get_collection()
        kwargs = {"query_texts": [query], "n_results": top_k}
        if metadata_filter:
            kwargs["where"] = metadata_filter
        results = collection.query(**kwargs)

        if not results["documents"] or not results["documents"][0]:
            return []

        search_results = []
        for i in range(len(results["documents"][0])):
            search_results.append({
                "content": results["documents"][0][i],
                "metadata": results["metadatas"][0][i],
                "distance": results["distances"][0][i],
            })
        return search_results

    def get_document_count(self) -> int:
        """获取向量库中的文档数量。"""
        collection = self._get_collection()
        return collection.count()

    def get_stats(self) -> dict:
        """获取向量库统计信息。"""
        collection = self._get_collection()
        count = collection.count()
        # 获取不同来源文件数
        try:
            all_data = collection.get()
            sources = set()
            if all_data["metadatas"]:
                for meta in all_data["metadatas"]:
                    if meta and "source" in meta:
                        sources.add(meta["source"])
            file_count = len(sources)
        except Exception:
            file_count = 0

        return {
            "collection_name": self._collection_name,
            "total_chunks": count,
            "total_files": file_count,
        }

    def clear(self):
        """清空向量库。"""
        client = self._get_client()
        try:
            client.delete_collection(self._collection_name)
        except Exception:
            pass
        self._collection = None
        logger.info("向量库已清空: %s", self._collection_name)

    @classmethod
    def from_config(cls, config_path: str = "config.yaml") -> "VectorStore":
        """从配置文件创建 VectorStore 实例（全局单例缓存）。

        相同配置只创建一个实例，embedding 模型只加载一次。
        """
        global _cached_vectorstore, _cached_config_key

        from rag.config import get_config as get_app_config
        config = get_app_config(config_path)
        vs_cfg = config.vectorstore
        emb_cfg = config.embedding

        config_key = f"{vs_cfg.persist_directory}|{vs_cfg.collection_name}|{emb_cfg.model}|{emb_cfg.local_path}"

        if _cached_vectorstore is not None and _cached_config_key == config_key:
            return _cached_vectorstore

        instance = cls(
            persist_directory=vs_cfg.persist_directory,
            collection_name=vs_cfg.collection_name,
            embedding_model=emb_cfg.model,
            embedding_local_path=emb_cfg.local_path,
        )

        _cached_vectorstore = instance
        _cached_config_key = config_key
        return instance

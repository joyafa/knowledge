"""RAG 检索链模块。

检索相关文档块 → 重排序 → 构建 RAG prompt → 调用 LLM 生成回答。
支持多轮对话、混合检索（向量+BM25）、Cross-Encoder Reranker。
"""

import time
from typing import Generator, Optional

import yaml
from openai import OpenAI

from rag.vectorstore import VectorStore
from rag.logging_config import get_logger, audit_log

logger = get_logger(__name__)


def load_config(config_path: str = "config.yaml") -> dict:
    """加载配置文件（兼容旧接口）。"""
    from rag.config import get_config as get_app_config
    config = get_app_config(config_path)
    return {
        "knowledge": {
            "docs_directory": config.knowledge.docs_directory,
            "chunk_size": config.knowledge.chunk_size,
            "chunk_overlap": config.knowledge.chunk_overlap,
        },
        "embedding": {
            "model": config.embedding.model,
            "local_path": config.embedding.local_path,
        },
        "vectorstore": {
            "persist_directory": config.vectorstore.persist_directory,
            "collection_name": config.vectorstore.collection_name,
            "top_k": config.vectorstore.top_k,
            "distance_threshold": config.vectorstore.distance_threshold,
        },
        "llm": {
            "api_base": config.llm.api_base,
            "api_key": config.llm.api_key,
            "model": config.llm.model,
            "temperature": config.llm.temperature,
            "max_tokens": config.llm.max_tokens,
            "context_window": config.llm.context_window,
        },
    }


SYSTEM_PROMPT = """你是一个团队内部的 API 知识库助手。你必须严格遵守以下规则：

## 核心规则
1. **只能**根据下方提供的「知识库内容」回答问题，禁止使用你自身的知识储备
2. 如果知识库内容不足以回答问题，必须明确回复："抱歉，知识库中暂无相关内容，无法回答该问题。"
3. 绝对不要编造、推测或补充任何知识库中没有的信息

## 回答格式
- 回答时引用具体的来源文档路径
- 使用简体中文回答
- 如果包含代码，使用正确的 markdown 代码块格式（```cpp 等）

## 知识库内容
{context}"""


# ── 简单 BM25 关键词检索 ──

class BM25Retriever:
    """简易 BM25 关键词检索引擎。

    对 Corpus 中文档块进行索引，支持关键词搜索。
    使用经典 BM25 公式：得分 = IDF × TF × (k1+1) / (TF + k1×(1-b+b×doc_len/avg_doc_len))
    """

    def __init__(self, k1: float = 1.5, b: float = 0.75):
        self.k1 = k1
        self.b = b
        self._corpus: list[dict] = []
        self._doc_freq: dict[str, int] = {}
        self._avg_doc_len: float = 0
        self._built = False

    def index(self, documents: list[dict]):
        """构建 BM25 索引。

        Args:
            documents: [{"content": str, "metadata": dict}, ...]
        """
        self._corpus = documents
        self._doc_freq = {}
        total_len = 0

        for doc in documents:
            terms = self._tokenize(doc["content"])
            unique_terms = set(terms)
            for term in unique_terms:
                self._doc_freq[term] = self._doc_freq.get(term, 0) + 1
            total_len += len(terms)

        self._avg_doc_len = total_len / len(documents) if documents else 0
        self._built = True

    def _tokenize(self, text: str) -> list[str]:
        """简易中文分词。"""
        import re
        # 提取中文字符、英文单词、数字
        tokens = re.findall(r'[\u4e00-\u9fff]+|[a-zA-Z_]\w*|\d+', text.lower())
        return tokens

    def search(self, query: str, top_k: int = 10) -> list[tuple[int, float]]:
        """关键词检索，返回 [(doc_index, score), ...] 按分数降序排列。"""
        if not self._built:
            return []

        query_terms = self._tokenize(query)
        if not query_terms:
            return []

        N = len(self._corpus)
        scores = []

        for idx, doc in enumerate(self._corpus):
            doc_terms = self._tokenize(doc["content"])
            doc_len = len(doc_terms)
            if doc_len == 0:
                continue

            term_freqs = {}
            for t in doc_terms:
                term_freqs[t] = term_freqs.get(t, 0) + 1

            score = 0.0
            for term in query_terms:
                tf = term_freqs.get(term, 0)
                if tf == 0:
                    continue
                df = self._doc_freq.get(term, 0)
                if df == 0:
                    continue
                idf = max(0, ((N - df + 0.5) / (df + 0.5)))
                numerator = tf * (self.k1 + 1)
                denominator = tf + self.k1 * (1 - self.b + self.b * doc_len / self._avg_doc_len)
                score += idf * (numerator / denominator)

            if score > 0:
                scores.append((idx, score))

        scores.sort(key=lambda x: x[1], reverse=True)
        return scores[:top_k]


# ── Reciprocal Rank Fusion ──

def reciprocal_rank_fusion(
    vector_results: list[dict],
    bm25_results: list[dict],
    k: int = 60,
) -> list[dict]:
    """RRF 融合向量检索和 BM25 检索结果。

    RRF_score(d) = Σ 1/(k + rank_i(d))
    """
    scores: dict[int, float] = {}
    doc_map: dict[int, dict] = {}

    # 向量检索排名
    for rank, doc in enumerate(vector_results):
        doc_id = id(doc)
        doc_map[doc_id] = doc
        scores[doc_id] = scores.get(doc_id, 0) + 1.0 / (k + rank + 1)

    # BM25 检索排名
    for rank, doc in enumerate(bm25_results):
        doc_id = id(doc)
        if doc_id not in doc_map:
            doc_map[doc_id] = doc
        scores[doc_id] = scores.get(doc_id, 0) + 1.0 / (k + rank + 1)

    # 按 RRF 分数排序
    sorted_ids = sorted(scores.keys(), key=lambda x: scores[x], reverse=True)
    return [doc_map[doc_id] for doc_id in sorted_ids]


class RAGChain:
    """RAG 检索增强生成链。

    支持：
    - 多轮对话（自动注入对话历史）
    - 混合检索（向量 + BM25 + RRF 融合）
    - Cross-Encoder Reranker（可选）
    - 查询改写（可选）
    """

    CHARS_PER_TOKEN = 1.5

    def __init__(self, vectorstore: VectorStore, config: dict):
        self._vectorstore = vectorstore
        self._config = config
        self._llm_cfg = config["llm"]
        self._vs_cfg = config["vectorstore"]
        self._context_window = self._llm_cfg.get("context_window", 8192)
        self._max_tokens = self._llm_cfg.get("max_tokens", 2048)
        self._client = OpenAI(
            base_url=self._llm_cfg["api_base"],
            api_key=self._llm_cfg["api_key"],
        )
        # BM25 检索器（延迟初始化）
        self._bm25: Optional[BM25Retriever] = None
        # 最近一次检索的原始结果（用于 BM25 索引复用）
        self._last_doc_count: int = 0

    def _ensure_bm25_ready(self):
        """确保 BM25 检索器与向量库同步。"""
        current_count = self._vectorstore.get_document_count()
        if self._bm25 is not None and current_count == self._last_doc_count:
            return

        logger.info("重建 BM25 索引 (%d 个文档块)...", current_count)
        collection = self._vectorstore._get_collection()
        # 获取所有文档块
        try:
            all_data = collection.get()
            documents = []
            if all_data["documents"] and all_data["metadatas"]:
                for i in range(len(all_data["documents"])):
                    documents.append({
                        "content": all_data["documents"][i],
                        "metadata": all_data["metadatas"][i] if all_data["metadatas"] else {},
                    })
            self._bm25 = BM25Retriever()
            self._bm25.index(documents)
            self._last_doc_count = current_count
            logger.info("BM25 索引构建完成")
        except Exception as e:
            logger.warning("BM25 索引构建失败: %s", e)
            self._bm25 = None

    def _estimate_tokens(self, text: str) -> int:
        """粗略估算文本的 token 数。"""
        return int(len(text) / self.CHARS_PER_TOKEN)

    def _rewrite_query(self, query: str, history: list[dict] = None) -> str:
        """查询改写：将对话上下文中的指代消解为独立查询。

        例如："TcpConnection 怎么用？" → "那它的 send 函数呢？"
        改写为 → "TcpConnection 的 send 函数怎么用？"
        """
        if not history or len(history) < 2:
            return query

        # 使用轻量规则：如果查询很短（<10字）且有历史，拼接最后一个用户问题
        if len(query) < 10 and history:
            last_user_msg = ""
            for msg in reversed(history):
                if msg.get("role") == "user":
                    last_user_msg = msg.get("content", "")
                    break
            if last_user_msg:
                combined = f"{last_user_msg} {query}"
                logger.debug("查询改写: %s → %s", query, combined)
                return combined

        return query

    def _retrieve(self, query: str, top_k: int = None, enable_hybrid: bool = True) -> list[dict]:
        """混合检索：向量检索 + BM25 关键词检索 + RRF 融合。

        Args:
            query: 查询文本
            top_k: 返回结果数
            enable_hybrid: 是否启用混合检索

        Returns:
            检索结果列表
        """
        if top_k is None:
            top_k = self._vs_cfg.get("top_k", 5)
        threshold = self._vs_cfg.get("distance_threshold", 600)

        # 向量检索
        embedding_fn = self._vectorstore._embedding_fn
        query_embedding = embedding_fn([query])
        collection = self._vectorstore._get_collection()
        results = collection.query(query_embeddings=query_embedding, n_results=max(top_k * 2, 10))

        if not results["documents"] or not results["documents"][0]:
            return []

        vector_results = []
        for i in range(len(results["documents"][0])):
            vector_results.append({
                "content": results["documents"][0][i],
                "metadata": results["metadatas"][0][i],
                "distance": results["distances"][0][i],
            })

        # 过滤低相关度
        filtered = [r for r in vector_results if r["distance"] < threshold]

        # BM25 检索（当向量结果不足时作为补充）
        bm25_results = []
        if enable_hybrid:
            try:
                self._ensure_bm25_ready()
                if self._bm25:
                    bm25_indices = self._bm25.search(query, top_k=top_k * 2)
                    all_docs_for_bm25 = []
                    collection_data = collection.get()
                    if collection_data["documents"]:
                        for i in range(len(collection_data["documents"])):
                            all_docs_for_bm25.append({
                                "content": collection_data["documents"][i],
                                "metadata": collection_data["metadatas"][i] if collection_data["metadatas"] else {},
                            })
                    for idx, score in bm25_indices:
                        if idx < len(all_docs_for_bm25):
                            bm25_results.append({
                                "content": all_docs_for_bm25[idx]["content"],
                                "metadata": all_docs_for_bm25[idx]["metadata"],
                                "bm25_score": score,
                            })
            except Exception as e:
                logger.debug("BM25 检索跳过: %s", e)

        # 融合结果
        if filtered and bm25_results:
            return reciprocal_rank_fusion(filtered, bm25_results)[:top_k]
        elif filtered:
            return filtered[:top_k]
        elif bm25_results:
            logger.info("向量检索无结果，使用 BM25 兜底（%d 条）", len(bm25_results))
            return bm25_results[:top_k]
        else:
            return []

    def _rerank(self, query: str, results: list[dict]) -> list[dict]:
        """Cross-Encoder Reranker 二次精排。

        使用本地轻量 reranker 模型对检索结果重排序。
        """
        if len(results) <= 1:
            return results

        try:
            from sentence_transformers import CrossEncoder
            model_name = "BAAI/bge-reranker-base"
            logger.debug("正在加载 Reranker 模型: %s", model_name)
            reranker = CrossEncoder(model_name)
            pairs = [[query, r["content"]] for r in results]
            scores = reranker.predict(pairs)
            for i, score in enumerate(scores):
                results[i]["rerank_score"] = float(score)
            results.sort(key=lambda x: x.get("rerank_score", 0), reverse=True)
            logger.debug("Reranker 重排序完成")
        except Exception as e:
            logger.debug("Reranker 不可用，跳过: %s", e)

        return results

    def _build_context(self, search_results: list[dict], budget_tokens: int) -> str:
        """将检索结果拼接为上下文字符串，自动裁剪以适配上下文窗口。"""
        context_parts = []
        used_tokens = 0

        for i, result in enumerate(search_results, 1):
            source = result["metadata"].get("source", "未知来源")
            title = result["metadata"].get("title", "")
            header = f"[文档{i}] 来源: {source}" + (f" | 标题: {title}" if title else "")
            content = result["content"]
            part = f"{header}\n{content}"

            part_tokens = self._estimate_tokens(part)
            if used_tokens + part_tokens > budget_tokens:
                remaining = budget_tokens - used_tokens
                if remaining > 50:
                    char_budget = int(remaining * self.CHARS_PER_TOKEN) - len(header)
                    if char_budget > 0:
                        truncated = content[:char_budget] + "\n...（内容已截断）"
                        context_parts.append(f"{header}\n{truncated}")
                break

            context_parts.append(part)
            used_tokens += part_tokens

        if not context_parts:
            return search_results[0]["content"][:int(budget_tokens * self.CHARS_PER_TOKEN)]

        return "\n\n---\n\n".join(context_parts)

    def _build_sources(self, search_results: list[dict]) -> list[dict]:
        """提取来源信息。"""
        seen = set()
        sources = []
        for result in search_results:
            source = result["metadata"].get("source", "")
            if source and source not in seen:
                seen.add(source)
                sources.append({
                    "source": source,
                    "title": result["metadata"].get("title", ""),
                })
        return sources

    def _calc_context_budget(self, question: str, history: list[dict] = None) -> int:
        """计算上下文可用的 token 预算。"""
        template_overhead = self._estimate_tokens(SYSTEM_PROMPT.format(context=""))
        question_tokens = self._estimate_tokens(question)

        # 对话历史占用的 token
        history_tokens = 0
        if history:
            for msg in history[-6:]:  # 最近6轮
                history_tokens += self._estimate_tokens(msg.get("content", ""))

        budget = self._context_window - self._max_tokens - template_overhead - question_tokens - history_tokens - 100
        return max(budget, 200)

    def _build_messages(self, context: str, question: str, history: list[dict] = None) -> list[dict]:
        """构建 LLM 请求消息（支持多轮对话历史注入）。"""
        messages = [
            {"role": "system", "content": SYSTEM_PROMPT.format(context=context)},
        ]

        # 注入最近几轮对话历史
        if history:
            recent_history = history[-6:]  # 最近 6 轮
            for msg in recent_history:
                role = msg.get("role", "user")
                content = msg.get("content", "")
                if role in ("user", "assistant"):
                    messages.append({"role": role, "content": content[:2000]})

        messages.append({"role": "user", "content": question})
        return messages

    def query_stream_with_status(
        self,
        question: str,
        history: list[dict] = None,
        enable_hybrid: bool = True,
        enable_rerank: bool = True,
        enable_rewrite: bool = True,
        username: str = "anonymous",
    ) -> Generator[dict, None, None]:
        """执行 RAG 查询，分阶段返回状态和内容。

        Args:
            question: 用户问题
            history: 对话历史列表 [{"role": "user/assistant", "content": str}, ...]
            enable_hybrid: 是否启用混合检索
            enable_rerank: 是否启用 Reranker
            enable_rewrite: 是否启用查询改写
            username: 用户名（用于审计日志）

        Yields:
            {"status": "searching"}                    — 正在检索
            {"status": "generating", "chunk": str}     — 正在生成
            {"status": "done", "sources": list}        — 完成
            {"status": "error", "message": str}        — 出错
        """
        start_time = time.time()
        yield {"status": "searching"}

        # 查询改写
        if enable_rewrite and history:
            question = self._rewrite_query(question, history)

        try:
            search_results = self._retrieve(question, enable_hybrid=enable_hybrid)
        except Exception as e:
            err_msg = f"检索失败: {str(e)}"
            audit_log(username, "query", details=err_msg, query=question,
                      duration_ms=(time.time() - start_time) * 1000)
            yield {"status": "error", "message": err_msg}
            return

        if not search_results:
            duration_ms = (time.time() - start_time) * 1000
            audit_log(username, "query", details="无匹配结果", query=question,
                      result_count=0, duration_ms=duration_ms)
            yield {"status": "done", "sources": []}
            return

        # Reranker 二次精排
        if enable_rerank:
            search_results = self._rerank(question, search_results)

        budget = self._calc_context_budget(question, history)
        context = self._build_context(search_results, budget)
        sources = self._build_sources(search_results)
        messages = self._build_messages(context, question, history)

        logger.info("查询: %s → %d 个文档块", question[:50], len(search_results))

        yield {"status": "generating", "chunk": ""}

        # 流式调用 LLM
        try:
            stream = self._client.chat.completions.create(
                model=self._llm_cfg["model"],
                messages=messages,
                temperature=self._llm_cfg.get("temperature", 0.3),
                max_tokens=self._max_tokens,
                stream=True,
            )
            has_content = False
            full_answer = ""
            for chunk in stream:
                if chunk.choices and chunk.choices[0].delta.content:
                    has_content = True
                    token = chunk.choices[0].delta.content
                    full_answer += token
                    yield {"status": "generating", "chunk": token}
            if not has_content:
                raise RuntimeError("流式响应为空")
        except Exception as stream_err:
            logger.warning("流式调用失败，尝试非流式: %s", str(stream_err)[:200])
            try:
                resp = self._client.chat.completions.create(
                    model=self._llm_cfg["model"],
                    messages=messages,
                    temperature=self._llm_cfg.get("temperature", 0.3),
                    max_tokens=self._max_tokens,
                )
                full_answer = resp.choices[0].message.content
                if full_answer:
                    yield {"status": "generating", "chunk": full_answer}
                else:
                    err_msg = "模型返回了空内容"
                    audit_log(username, "query", details=err_msg, query=question,
                              result_count=len(search_results),
                              duration_ms=(time.time() - start_time) * 1000)
                    yield {"status": "error", "message": err_msg}
                    return
            except Exception as e2:
                err_detail = str(e2)
                # 提取 HTTP 状态码和 API 地址，帮助用户诊断
                api_url = self._llm_cfg.get("api_base", "未知")
                model = self._llm_cfg.get("model", "未知")
                err_msg = f"LLM 调用失败\n\n> API: `{api_url}`\n> 模型: `{model}`\n> 错误: {err_detail}"
                audit_log(username, "query", details=err_msg, query=question,
                          result_count=len(search_results),
                          duration_ms=(time.time() - start_time) * 1000)
                yield {"status": "error", "message": err_msg}
                return

        duration_ms = (time.time() - start_time) * 1000
        audit_log(
            username, "query",
            details=f"检索 {len(search_results)} 个文档块，生成 {len(full_answer)} 字回答",
            query=question,
            answer_preview=full_answer[:200] if full_answer else "",
            result_count=len(search_results),
            duration_ms=duration_ms,
        )

        yield {"status": "done", "sources": sources}

    @classmethod
    def from_config(cls, config_path: str = "config.yaml") -> "RAGChain":
        """从配置文件创建 RAGChain 实例。"""
        config = load_config(config_path)
        vectorstore = VectorStore.from_config(config_path)
        return cls(vectorstore=vectorstore, config=config)

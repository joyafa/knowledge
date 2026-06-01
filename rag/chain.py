"""RAG 检索链模块。

检索相关文档块 → 重排序 → 构建 RAG prompt → 调用 LLM 生成回答。
支持多轮对话、混合检索（向量+BM25）、Cross-Encoder Reranker。
"""

import hashlib
import re
import time
from pathlib import Path
from typing import Generator, Optional

import jieba
from openai import OpenAI

from rag.config import load_config
from rag.vectorstore import VectorStore
from rag.logging_config import get_logger, audit_log

logger = get_logger(__name__)


SYSTEM_PROMPT = """你是一个知识库问答机器人。你的回答**必须且只能**基于下方「知识库内容」。

---

## 🚨 刚性格式要求（不遵守 = 回答无效）

你的回答**必须**以以下两种格式之一开头，否则你的回答将被系统丢弃：

**格式 A — 可以回答时：**
【知识库回答】
（在这里写你的回答，必须引用下方知识库中的具体文档来源）

**格式 B — 无法回答时：**
【拒绝回答】
抱歉，知识库中暂无相关内容，无法回答该问题。

---

## 重要规则

- 如果知识库内容与用户问题主题相关 → 用格式 A，从知识库内容中提取信息组织答案
- 如果知识库内容与用户问题主题完全无关 → 用格式 B，只输出那一句话
- **绝对禁止**输出格式 A/B 之外的任何内容
- **绝对禁止**使用你自身的知识储备，你只是一个知识库内容的复述者
- 知识库内容是 API 参考文档，从中提取接口、参数、代码即可

---

## 知识库内容
{context}"""

# ── 简单 BM25 关键词检索 ──

class BM25Retriever:
    """简易 BM25 关键词检索引擎。

    对 Corpus 中文档块进行索引，支持关键词搜索。
    使用经典 BM25 公式：得分 = IDF × TF × (k1+1) / (TF + k1×(1-b+b×doc_len/avg_doc_len))
    """

    # 分词器版本——改分词逻辑后递增此值，强制重建索引
    TOKENIZER_VERSION = 3

    def __init__(self, k1: float = 1.5, b: float = 0.75):
        self.k1 = k1
        self.b = b
        self._corpus: list[dict] = []
        self._doc_freq: dict[str, int] = {}
        self._avg_doc_len: float = 0
        self._built = False
        # 预计算缓存：每个文档的 token 列表和词频
        self._doc_tokens: list[list[str]] = []
        self._doc_term_freqs: list[dict[str, int]] = []

    def index(self, documents: list[dict]):
        """构建 BM25 索引。

        预计算每个文档的 token 列表和词频，避免搜索时重复分词。

        Args:
            documents: [{"content": str, "metadata": dict}, ...]
        """
        self._corpus = documents
        self._doc_freq = {}
        self._doc_tokens = []
        self._doc_term_freqs = []
        total_len = 0

        for doc in documents:
            terms = self._tokenize(doc["content"])
            self._doc_tokens.append(terms)

            # 预计算词频
            term_freqs: dict[str, int] = {}
            for t in terms:
                term_freqs[t] = term_freqs.get(t, 0) + 1
            self._doc_term_freqs.append(term_freqs)

            unique_terms = set(terms)
            for term in unique_terms:
                self._doc_freq[term] = self._doc_freq.get(term, 0) + 1
            total_len += len(terms)

        self._avg_doc_len = total_len / len(documents) if documents else 0
        self._built = True

    def _tokenize(self, text: str) -> list[str]:
        """中文分词（jieba）+ 英文/数字提取 + camelCase 拆分。"""
        tokens = []
        for word in jieba.lcut(text):
            word = word.strip().lower()
            if not word:
                continue
            # 包含中文 → 直接作为 token
            if re.search(r'[一-鿿]', word):
                tokens.append(word)
            else:
                # 纯英文/数字/混合 → 拆分单词和数字
                sub_tokens = re.findall(r'[a-zA-Z_]\w*|\d+', word)
                tokens.extend(sub_tokens)
                # camelCase / PascalCase 拆分（TcpConnection → tcp, connection）
                for tok in sub_tokens:
                    parts = re.sub(r'([a-z])([A-Z])', r'\1 \2', tok).lower().split()
                    if len(parts) > 1:
                        tokens.extend(parts)
        return tokens

    def search(self, query: str, top_k: int = 10) -> list[tuple[int, float]]:
        """关键词检索，返回 [(doc_index, score), ...] 按分数降序排列。

        复用 index() 阶段预计算的 token 列表和词频，避免重复分词。
        """
        if not self._built:
            return []

        query_terms = self._tokenize(query)
        if not query_terms:
            return []

        N = len(self._corpus)
        scores = []

        for idx in range(len(self._corpus)):
            doc_len = len(self._doc_tokens[idx])
            if doc_len == 0:
                continue

            term_freqs = self._doc_term_freqs[idx]

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

def _doc_hash(doc: dict) -> str:
    """计算文档内容哈希，用于跨检索源去重。"""
    return hashlib.md5(doc.get("content", "").encode()).hexdigest()


def reciprocal_rank_fusion(
    vector_results: list[dict],
    bm25_results: list[dict],
    k: int = 10,
) -> list[dict]:
    """RRF 融合向量检索和 BM25 检索结果。

    RRF_score(d) = Σ 1/(k + rank_i(d))
    使用内容哈希去重，避免不同检索源返回的相同文档被重复计算。
    """
    scores: dict[str, float] = {}
    doc_map: dict[str, dict] = {}

    # 向量检索排名
    for rank, doc in enumerate(vector_results):
        doc_key = _doc_hash(doc)
        doc_map[doc_key] = doc
        scores[doc_key] = scores.get(doc_key, 0) + 1.0 / (k + rank + 1)

    # BM25 检索排名
    for rank, doc in enumerate(bm25_results):
        doc_key = _doc_hash(doc)
        if doc_key not in doc_map:
            doc_map[doc_key] = doc
        scores[doc_key] = scores.get(doc_key, 0) + 1.0 / (k + rank + 1)

    # 按 RRF 分数排序
    sorted_keys = sorted(scores.keys(), key=lambda x: scores[x], reverse=True)
    return [doc_map[key] for key in sorted_keys]


class RAGChain:
    """RAG 检索增强生成链。

    支持：
    - 多轮对话（自动注入对话历史）
    - 混合检索（向量 + BM25 + RRF 融合）
    - Cross-Encoder Reranker（可选，类级别缓存）
    - 查询改写（可选）
    """

    CHARS_PER_TOKEN = 1.5

    # 类级别缓存：避免每次查询都重新加载 Reranker 模型
    _reranker_model: Optional[object] = None
    _reranker_model_name: Optional[str] = None
    _reranker_load_failed: bool = False  # 加载失败标记，避免重复尝试

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
        # 记录 BM25 索引构建时的分词器版本
        self._bm25_tokenizer_version: int = 0

    def _ensure_bm25_ready(self):
        """确保 BM25 检索器与向量库同步。

        文档数变化或分词器版本升级时自动重建索引。
        """
        current_count = self._vectorstore.get_document_count()
        need_rebuild = (
            self._bm25 is None
            or current_count != self._last_doc_count
            or self._bm25_tokenizer_version != BM25Retriever.TOKENIZER_VERSION
        )
        if not need_rebuild:
            return

        logger.info("重建 BM25 索引 (%d 个文档块)...", current_count)
        try:
            documents = self._vectorstore.get_all_documents()
            self._bm25 = BM25Retriever()
            self._bm25.index(documents)
            self._last_doc_count = current_count
            self._bm25_tokenizer_version = BM25Retriever.TOKENIZER_VERSION
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
        threshold = self._vs_cfg.get("distance_threshold", 10000)

        # 向量检索（扩大候选集，给 BM25 单边高分文档更多融合机会）
        embedding_fn = self._vectorstore._embedding_fn
        query_embedding = embedding_fn([query])
        collection = self._vectorstore.get_collection()
        results = collection.query(query_embeddings=query_embedding, n_results=max(top_k * 3, 30))

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
                    # 直接复用 BM25 索引中已缓存的文档（避免每次查询全量加载 ChromaDB）
                    bm25_corpus = self._bm25._corpus
                    for idx, score in bm25_indices:
                        if idx < len(bm25_corpus):
                            bm25_results.append({
                                "content": bm25_corpus[idx]["content"],
                                "metadata": bm25_corpus[idx]["metadata"],
                                "bm25_score": score,
                            })
            except Exception as e:
                logger.debug("BM25 检索跳过: %s", e)

        # 融合结果（优先用 threshold 过滤后的向量结果，否则用原始候选）
        candidates = filtered if filtered else vector_results
        if candidates and bm25_results:
            if not filtered:
                logger.info("向量结果全被 threshold 过滤，用原始候选与 BM25 融合（%d+%d 条）",
                            len(vector_results), len(bm25_results))
            fused = reciprocal_rank_fusion(candidates, bm25_results)[:top_k]
            # 融合后不足 top_k，用 BM25 不在 fused 中的结果补齐
            if len(fused) < top_k:
                fused_hashes = {_doc_hash(d) for d in fused}
                for doc in bm25_results:
                    if len(fused) >= top_k:
                        break
                    if _doc_hash(doc) not in fused_hashes:
                        fused.append(doc)
            return fused
        elif candidates:
            if not filtered:
                logger.info("BM25 无结果，使用原始向量候选（distance: %.2f-%.2f）",
                            vector_results[0]["distance"], vector_results[-1]["distance"])
            return candidates[:top_k]
        elif bm25_results:
            logger.info("向量检索无结果，使用 BM25 兜底（%d 条）", len(bm25_results))
            return bm25_results[:top_k]
        else:
            return []

    def _rerank(self, query: str, results: list[dict]) -> list[dict]:
        """Cross-Encoder Reranker 二次精排。

        使用本地轻量 reranker 模型对检索结果重排序。
        模型在类级别缓存，避免每次查询重新加载。
        支持从配置的 local_path 离线加载，否则从 HuggingFace 在线下载。
        可通过配置 reranker.enabled=false 禁用，大幅加速响应。
        """
        reranker_cfg = self._config.get("reranker", {})
        if not reranker_cfg.get("enabled", True):
            return results

        if len(results) <= 1:
            return results

        # 只对前 top_n 个候选文档进行精排（减少 Cross-Encoder 计算量）
        top_n = reranker_cfg.get("top_n", 10)
        candidates = results[:top_n]
        rest = results[top_n:]

        try:
            reranker_model_name = reranker_cfg.get("model", "BAAI/bge-reranker-base")
            reranker_local_path = reranker_cfg.get("local_path", "")

            # 有本地路径且存在则离线加载，否则用 HuggingFace 模型名在线加载
            use_local = bool(reranker_local_path and Path(reranker_local_path).exists())
            resolved = reranker_local_path if use_local else reranker_model_name

            # 上次加载已失败且非本地路径 → 直接跳过（避免反复超时）
            if RAGChain._reranker_load_failed and not use_local:
                if RAGChain._reranker_model_name == resolved:
                    return results
                # 模型名变了，重置失败标记再试一次
                RAGChain._reranker_load_failed = False

            # 类级别缓存：只在首次或路径变化时加载
            if (RAGChain._reranker_model is None or
                    RAGChain._reranker_model_name != resolved):
                from sentence_transformers import CrossEncoder
                logger.debug("正在加载 Reranker 模型: %s", resolved)
                if use_local:
                    logger.debug("（从本地路径离线加载）")
                RAGChain._reranker_model = CrossEncoder(resolved, local_files_only=use_local)
                RAGChain._reranker_model_name = resolved
                logger.debug("Reranker 模型加载完成（已缓存）")

            pairs = [[query, r["content"]] for r in candidates]
            scores = RAGChain._reranker_model.predict(pairs)
            for i, score in enumerate(scores):
                candidates[i]["rerank_score"] = float(score)
            candidates.sort(key=lambda x: x.get("rerank_score", 0), reverse=True)
            logger.debug("Reranker 重排序完成 (%d 个候选)", len(candidates))
        except Exception as e:
            logger.debug("Reranker 不可用，跳过: %s", e)
            if not use_local:
                RAGChain._reranker_load_failed = True

        # 精排后的候选 + 未参与精排的剩余文档（保持原序）
        return candidates + rest

    def _build_context(self, search_results: list[dict], budget_tokens: int, low_confidence: bool = False) -> str:
        """将检索结果拼接为上下文字符串，自动裁剪以适配上下文窗口。

        Args:
            search_results: 检索结果列表
            budget_tokens: token 预算
            low_confidence: 是否为低置信度匹配（最佳结果距离 > 0.5）
        """
        context_parts = []

        # 低置信度时插入提示（仅做语气降级，不强制拒绝）
        if low_confidence:
            context_parts.append(
                "⚠️ 【系统提示】以下知识库内容是从关键词匹配获得的，可能与用户问题不完全对应。"
                "请仔细判断内容是否与问题相关：如果能找到有用信息就用格式 A 回答；"
                "如果确实完全无关再用格式 B。"
            )

        used_tokens = self._estimate_tokens("\n\n---\n\n".join(context_parts)) if context_parts else 0

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
            import traceback as _tb
            err_detail = f"检索失败: {str(e)}\n{_tb.format_exc()}"
            logger.error(err_detail)
            audit_log(username, "query", details=err_detail, query=question,
                      duration_ms=(time.time() - start_time) * 1000)
            yield {"status": "error", "message": f"检索失败: {str(e)}"}
            return

        if not search_results:
            # 知识库无匹配 → 直接返回提示，不再调用 LLM
            logger.info("查询: %s → 知识库无匹配", question[:50])
            duration_ms = (time.time() - start_time) * 1000
            audit_log(username, "query",
                      details="知识库无匹配",
                      query=question,
                      answer_preview="",
                      result_count=0,
                      duration_ms=duration_ms)
            yield {"status": "done", "sources": []}
            return

        # Reranker 二次精排
        if enable_rerank:
            search_results = self._rerank(question, search_results)

        budget = self._calc_context_budget(question, history)
        # 低置信度检测：
        # 仅当检索结果完全没有向量匹配（全部来自 BM25 且无 distance）时才标记低置信度。
        # Reranker 已做过精排，能留到这里的 result 都是相关的。
        top_distance = search_results[0].get("distance", -1) if search_results else -1
        has_vector_match = any(r.get("distance", -1) >= 0 for r in search_results)
        # 没有任何向量匹配结果 → 纯 BM25 兜底，可能不精确
        low_confidence = not has_vector_match and len(search_results) <= 2
        context = self._build_context(search_results, budget, low_confidence=low_confidence)
        sources = self._build_sources(search_results)
        messages = self._build_messages(context, question, history)

        logger.info("查询: %s → %d 个文档块 (top_distance=%.3f, has_vector=%s, low_conf=%s)",
                    question[:50], len(search_results), top_distance, has_vector_match, low_confidence)

        yield {"status": "generating", "chunk": ""}

        # 流式调用 LLM，带重试和降级
        full_answer = ""
        try:
            for token in self._call_llm_stream(messages):
                full_answer += token
                yield {"status": "generating", "chunk": token}
        except Exception as stream_err:
            logger.warning("流式调用失败，尝试非流式: %s", str(stream_err)[:200])
            try:
                full_answer = self._call_llm_nonstream(messages)
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
                err_msg = f"LLM 调用失败\n\n> 模型: `{self._llm_cfg.get('model', '未知')}`\n> 错误: {err_detail}"
                audit_log(username, "query", details=err_msg, query=question,
                          result_count=len(search_results),
                          duration_ms=(time.time() - start_time) * 1000)
                yield {"status": "error", "message": err_msg}
                return

        # 后处理：检测 LLM 是否遵守格式要求或引用了知识库来源
        format_ok = full_answer.startswith("【知识库回答】") or full_answer.startswith("【拒绝回答】")
        has_source = False
        if not format_ok:
            # 检查是否至少引用了一个知识库中的文档来源
            for src in sources:
                src_name = src.get("source", "")
                if src_name and src_name in full_answer:
                    has_source = True
                    break
            # 也检查常见的文件引用模式
            if re.search(r'(来源|source)[：:]\s*\S+\.(md|cc|h|txt)', full_answer):
                has_source = True

        if not format_ok and not has_source:
            logger.warning("LLM 回答未引用知识库来源，替换为拒绝回答")
            full_answer = "抱歉，知识库中暂无相关内容，无法回答该问题。"

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

    def _call_llm_stream(self, messages: list[dict], max_retries: int = 3) -> Generator[str, None, None]:
        """流式调用 LLM，带指数退避重试。

        Args:
            messages: 消息列表
            max_retries: 最大重试次数

        Yields:
            生成的 token 片段

        Raises:
            RuntimeError: 所有重试均失败
        """
        last_error = None
        for attempt in range(max_retries):
            try:
                stream = self._client.chat.completions.create(
                    model=self._llm_cfg["model"],
                    messages=messages,
                    temperature=self._llm_cfg.get("temperature", 0.3),
                    max_tokens=self._max_tokens,
                    stream=True,
                )
                has_content = False
                for chunk in stream:
                    if chunk.choices and chunk.choices[0].delta.content:
                        has_content = True
                        yield chunk.choices[0].delta.content
                if not has_content:
                    raise RuntimeError("流式响应为空")
                return  # 成功，退出
            except Exception as e:
                last_error = e
                if attempt < max_retries - 1:
                    wait = 2 ** attempt
                    logger.warning(
                        "LLM 流式调用失败 (尝试 %d/%d)，%d 秒后重试: %s",
                        attempt + 1, max_retries, wait, str(e)[:100]
                    )
                    time.sleep(wait)
        raise RuntimeError(f"LLM 调用失败（已重试 {max_retries} 次）: {last_error}")

    def _call_llm_nonstream(self, messages: list[dict], max_retries: int = 3) -> str:
        """非流式调用 LLM，带指数退避重试。

        Returns:
            LLM 返回的文本内容

        Raises:
            RuntimeError: 所有重试均失败
        """
        last_error = None
        for attempt in range(max_retries):
            try:
                resp = self._client.chat.completions.create(
                    model=self._llm_cfg["model"],
                    messages=messages,
                    temperature=self._llm_cfg.get("temperature", 0.3),
                    max_tokens=self._max_tokens,
                )
                content = resp.choices[0].message.content
                if content:
                    return content
                raise RuntimeError("模型返回了空内容")
            except Exception as e:
                last_error = e
                if attempt < max_retries - 1:
                    wait = 2 ** attempt
                    logger.warning(
                        "LLM 非流式调用失败 (尝试 %d/%d)，%d 秒后重试: %s",
                        attempt + 1, max_retries, wait, str(e)[:100]
                    )
                    time.sleep(wait)
        raise RuntimeError(f"LLM 调用失败（已重试 {max_retries} 次）: {last_error}")

    @classmethod
    def from_config(cls, config_path: str = "config.yaml") -> "RAGChain":
        """从配置文件创建 RAGChain 实例。"""
        config = load_config(config_path)
        vectorstore = VectorStore.from_config(config_path)
        return cls(vectorstore=vectorstore, config=config)

    @classmethod
    def warmup_reranker(cls, config: dict):
        """预热 Reranker 模型（后台线程调用，避免首次查询等待）。

        仅在配置启用 reranker 时加载模型到类级别缓存。
        """
        reranker_cfg = config.get("reranker", {})
        if not reranker_cfg.get("enabled", True):
            logger.info("Reranker 已禁用，跳过预热")
            return
        try:
            model_name = reranker_cfg.get("model", "BAAI/bge-reranker-base")
            local_path = reranker_cfg.get("local_path", "")
            use_local = bool(local_path and Path(local_path).exists())
            resolved = local_path if use_local else model_name
            if cls._reranker_model is not None and cls._reranker_model_name == resolved:
                logger.info("Reranker 模型已缓存，跳过预热")
                return
            if cls._reranker_load_failed and not use_local:
                logger.info("Reranker 上次加载失败，跳过预热")
                return
            from sentence_transformers import CrossEncoder
            logger.info("预热 Reranker 模型: %s", resolved)
            cls._reranker_model = CrossEncoder(resolved, local_files_only=use_local)
            cls._reranker_model_name = resolved
            cls._reranker_load_failed = False
            logger.info("Reranker 模型预热完成")
        except Exception as e:
            logger.warning("Reranker 预热失败（将在首次查询时重试）: %s", e)
            if not use_local:
                cls._reranker_load_failed = True

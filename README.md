# Project Instructions

This file provides context for AI assistants working on this project.

## Project Type

企业级 RAG 知识库智能问答系统（Python + Streamlit + ChromaDB）

## Build / Test Commands

```bash
# 安装依赖
pip install -r requirements.txt
pip install -r requirements-dev.txt  # 开发依赖（测试工具等）

# 运行测试
pytest tests/ -v

# 文档入库（新增/更新知识库文档后执行）
python scripts/ingest.py

# 清空向量库
python scripts/clear_db.py

# 启动 Web 界面
streamlit run app.py

# 打包离线安装包
python scripts/prepare_offline.py
```

## Architecture

```
app.py               → Streamlit 主应用入口
rag/                 → RAG 检索引擎
  chain.py           → 检索链：混合检索 + RRF 融合 + Reranker + LLM 生成
  config.py          → Pydantic 配置管理
  embeddings.py      → sentence-transformers 向量化
  vectorstore.py     → ChromaDB 向量库管理
  loader.py          → 文档加载与分块
  preload.py         → 后台预加载（Streamlit 兼容）
  health.py          → 健康检查
  logging_config.py  → 结构化日志
ui/                  → Streamlit 界面组件
  chat.py            → 对话面板
  login.py           → 登录页面
  sidebar.py         → 侧边栏导航
  theme.py           → 双主题样式
services/            → 业务服务层
  analytics.py       → 仪表盘统计
  history.py         → 聊天记录持久化
  knowledge_service.py → 文档预览服务
  rate_limiter.py    → 速率限制
scripts/             → 运维脚本
tests/               → 单元测试
```

## Guidelines

- Follow existing code style and patterns
- Write tests for new functionality
- Keep changes focused and atomic
- Document public APIs
- 用户可见文本使用简体中文，代码标识符使用英文
- 配置通过 config.yaml 管理，不硬编码

## Important Notes

- 版本号统一管理于 rag/__init__.py 的 __version__
- Reranker 模型在 RAGChain 类级别缓存，避免重复加载
- VectorStore 使用全局单例缓存，embedding 模型只加载一次
- 速率限制定期清理不活跃用户（10分钟/次），防止内存泄漏
- LLM 调用带指数退避重试（最多 3 次），流式失败自动降级为非流式
- Docker 镜像使用多阶段构建 + 非 root 用户运行

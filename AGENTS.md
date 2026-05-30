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

# 启动 Web 界面（开发模式）
python run_app.py

# 打包 Windows 安装包（快速调试，不含模型）
python scripts/build_installer.py --platform windows --skip-models

# 打包 Windows 完整安装包（含模型，需先运行一次 dev 模式下载模型到 model/）
python scripts/build_installer.py --platform windows

# 准备 Linux 安装包 staging（在 Windows 上执行，再拷贝到 Linux 用 fpm 打包）
python scripts/prepare_linux_staging.py
```

## Architecture

```
run_app.py           → 统一启动入口（dev 和 PyInstaller 打包模式兼容）
app.py               → Streamlit 主应用入口
rag/                 → RAG 检索引擎
  chain.py           → 检索链：混合检索 + RRF 融合 + Reranker + LLM 生成
  config.py          → Pydantic 配置管理（支持 ${ENV_VAR} 和 ${ENV_VAR:-default} 替换）
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
scripts/             → 运维脚本 + 打包构建
  build_installer.py → 统一构建入口
  build_windows.py   → Windows PyInstaller + NSIS 打包
  build_linux.py     → Linux fpm 打包（需在 Linux 上运行）
  prepare_linux_staging.py → Linux staging 准备（可在 Windows 上运行）
  ingest.py          → 文档入库
  clear_db.py        → 清空向量库
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

- **入口脚本**: `run_app.py` 为统一启动入口，自动处理环境变量、目录创建、模型检测
- 版本号统一管理于 rag/__init__.py 的 __version__
- Reranker 模型在 RAGChain 类级别缓存，避免重复加载
- VectorStore 使用全局单例缓存，embedding 模型只加载一次
- 速率限制定期清理不活跃用户（10分钟/次），防止内存泄漏
- LLM 调用带指数退避重试（最多 3 次），流式失败自动降级为非流式
- Docker 镜像使用多阶段构建 + 非 root 用户运行

## Model Path Resolution（模型路径解析）

启动时 `run_app.py` 自动按以下顺序解析模型路径：

1. 设置 `MODEL_ROOT=app_root/model`、`SENTENCE_TRANSFORMERS_HOME=app_root/model`
2. 检测 `model/text2vec-base-chinese/` 是否存在 → 设置 `EMBEDDING_LOCAL_PATH`
3. 检测 `model/bge-reranker-base/` 是否存在 → 设置 `RERANKER_LOCAL_PATH`
4. `config.yaml` 通过 `${EMBEDDING_LOCAL_PATH:-}` / `${RERANKER_LOCAL_PATH:-}` 引用
5. 存在则离线加载（`local_files_only=True`），不存在则从 HuggingFace 下载

## Windows 打包注意事项

- PyInstaller 将 `rag/`、`ui/`、`services/` 编译进 PYZ 归档，安装目录不暴露源码
- 仅 `app.py`、`config.yaml`、`logo.png`、`knowledge/`、`data/` 作为数据文件保留
- ChromaDB 所有命名空间包需通过 `_s.py` 全量扫描后加入 `hiddenimports`
- 修改依赖后必须重新扫描：`python _s.py` 对比 PYZ-00.toc

## Linux 打包注意事项

- Linux 无 PyInstaller 编译，保留源码目录（`rag/`、`ui/`、`services/`、`scripts/`）
- 使用 `build_linux.py`（在 Linux 上完整构建）或 `prepare_linux_staging.py`（跨平台准备）
- `launch.sh` 统一通过 `run_app.py` 启动，与 Windows 版本保持一致
- `postinst.sh` 不硬编码 `local_path`，由运行时自动检测

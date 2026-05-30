# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 项目简介

团队内部 API 智能助手（私有知识库 + RAG Chat）。成员可以用自然语言查询 API 用法、参数含义、代码示例，系统从 Markdown/PDF/TXT 知识库中检索相关内容并结合 LLM 生成回答。

## 技术栈

- **Python 3.10+**
- **Streamlit** — Web 界面（赛博朋克主题）
- **ChromaDB** — 向量数据库（持久化存储在 `./chroma_db`）
- **sentence-transformers** — 本地中文 embedding（text2vec-base-chinese）
- **OpenAI 兼容 API** — LLM 调用（支持切换到本地 vLLM）
- **httpx** — HTTP 客户端
- **pymupdf** — PDF 文本提取

## 常用命令

```bash
# 安装依赖
pip install -r requirements.txt

# 文档入库（新增/更新知识库文档后执行）
python scripts/ingest.py

# 清空向量库
python scripts/clear_db.py

# 启动 Web 界面（开发模式，run_app.py 为统一入口）
python run_app.py

# 打包 Windows 安装包（快速调试，不含模型）
python scripts/build_installer.py --platform windows --skip-models

# 打包 Windows 完整安装包（含模型，需先运行 dev 模式下载模型）
python scripts/build_installer.py --platform windows

# 准备 Linux 安装包 staging（Windows 上执行，拷贝到 Linux 用 fpm 打包）
python scripts/prepare_linux_staging.py
```

## 架构

```
run_app.py           → 统一启动入口（处理环境变量、目录创建、模型检测，兼容 dev/PyInstaller）
app.py               → Streamlit 主应用（双栏布局 + 赛博朋克主题 + 用户登录）
rag/
  config.py          → Pydantic 配置管理（支持 ${ENV_VAR:-default} 环境变量替换）
  loader.py          → 文档加载与分块（支持 .md / .txt / .pdf，按标题层级切分）
  embeddings.py      → 向量化（sentence-transformers → ChromaDB embedding function）
  vectorstore.py     → ChromaDB 向量库管理（全局单例缓存，增删查）
  chain.py           → RAG 检索链（混合检索 + RRF 融合 + Reranker + LLM 生成）
  preload.py         → 后台预加载（daemon thread，避免 Streamlit rerun 阻塞）
scripts/
  build_installer.py → 统一构建入口（--platform windows|linux|both，--skip-models 快速调试）
  build_windows.py   → Windows PyInstaller + NSIS 打包
  build_linux.py     → Linux fpm 打包（需在 Linux 上运行）
  prepare_linux_staging.py → Linux staging 准备（跨平台）
  ingest.py          → 文档入库
  clear_db.py        → 清空向量库
config.yaml          → 全局配置（模型、向量库、分块参数、检索阈值）
knowledge/           → 知识库文档目录（.md / .txt / .pdf）
data/                → 运行时数据（chroma_db、knowledge、logs、chat_history）
model/               → AI 模型缓存（SENTENCE_TRANSFORMERS_HOME 指向此处）
```

## 核心设计

### RAG 查询流程

1. 用户提问 → embedding 模型向量化查询
2. ChromaDB 向量检索 top-k 文档块
3. 按距离阈值过滤低相关度结果（`distance_threshold: 400`）
4. 自动裁剪上下文以适配模型窗口（`context_window`）
5. 拼接系统 prompt + 检索上下文 + 用户问题
6. 流式调用 LLM，失败时自动降级为非流式

### 性能优化

- **VectorStore 全局单例缓存**：相同配置只创建一个实例，embedding 模型只加载一次
- **检索时复用 embedding 模型**：直接用 `query_embeddings` 查询，跳过 ChromaDB 二次实例化
- **检索耗时**：~25ms（优化前 7.4s）

### 多用户隔离

- 登录时输入用户名，聊天记录存储在 `chat_history/{用户名}/{日期}.json`
- 每个用户只能看到自己的历史记录
- 支持"清除当前会话"（同时清空文件和页面）

### 相关度控制

- 向量检索按 L2 距离过滤，阈值 400（实测：相关问题 220-310，无关问题 400+）
- 无相关内容时不调用 LLM，直接返回"知识库中暂无匹配内容"
- Prompt 严格约束模型只能基于知识库内容回答

### 离线部署

- `scripts/build_installer.py` 统一构建入口，支持 `--skip-models` 快速调试开关
- Windows：PyInstaller 编译 exe + NSIS 打包安装包，源码编译进 PYZ 不暴露
- Linux：源码 + Python standalone + fpm 打包 .deb/.rpm，`prepare_linux_staging.py` 可在 Windows 上准备
- 模型缓存统一到 `model/` 目录，`run_app.py` 启动时自动检测本地模型并设置 `EMBEDDING_LOCAL_PATH`
- `config.yaml` 的 `local_path` 使用 `${EMBEDDING_LOCAL_PATH:-}` 环境变量引用，不硬编码

## 配置切换

模型切换只需修改 `config.yaml` 中的 `llm` 部分：

```yaml
# 切换到本地 vLLM 示例
llm:
  api_base: "http://localhost:8000/v1"
  api_key: "EMPTY"
  model: "Qwen2.5-7B-Instruct"
```

## 代码规范

- 所有用户可见文本（错误提示、日志、注释）使用简体中文
- 变量名、函数名、类名使用英文
- 配置通过 `config.yaml` 管理，不硬编码

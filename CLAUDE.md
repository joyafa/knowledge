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

# 启动 Web 界面
streamlit run app.py

# 打包离线安装包（在有网机器上运行）
python scripts/prepare_offline.py
```

## 架构

```
app.py               → Streamlit 主应用（双栏布局 + 赛博朋克主题 + 用户登录）
rag/
  loader.py          → 文档加载与分块（支持 .md / .txt / .pdf，按标题层级切分）
  embeddings.py      → 向量化（sentence-transformers → ChromaDB embedding function）
  vectorstore.py     → ChromaDB 向量库管理（全局单例缓存，增删查）
  chain.py           → RAG 检索链（复用 embedding 模型检索 + prompt 裁剪 + LLM 生成）
scripts/
  ingest.py          → 文档入库脚本
  clear_db.py        → 清空向量库
  prepare_offline.py → 离线打包脚本（生成 Windows + Linux 安装包）
config.yaml          → 全局配置（模型、向量库、分块参数、检索阈值）
knowledge/           → 知识库文档目录（.md / .txt / .pdf）
chat_history/        → 聊天记录（按用户名/日期隔离存储）
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

- `scripts/prepare_offline.py` 打包 wheels + embedding 模型 + 项目代码
- Windows 双击 `install_offline.bat`，Linux 运行 `install_offline.sh`
- 自动配置本地 embedding 模型路径

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

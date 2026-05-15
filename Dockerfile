# 知识库智能助手 Docker 镜像（多阶段构建）
# 阶段 1: 构建依赖
FROM python:3.11-slim AS builder

LABEL maintainer="knowledge-team"
LABEL description="企业级 RAG 知识库智能问答系统"

WORKDIR /app

# 安装构建依赖
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    g++ \
    curl \
    && rm -rf /var/lib/apt/lists/*

# 设置国内镜像（可选，构建时通过 --build-arg 控制）
ARG USE_MIRROR=false
ENV HF_ENDPOINT="https://hf-mirror.com"

# 复制依赖文件并安装
COPY requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt

# ── 阶段 2: 运行时镜像 ──
FROM python:3.11-slim

WORKDIR /app

# 安装运行时系统依赖
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    && rm -rf /var/lib/apt/lists/*

# 创建非 root 用户
RUN groupadd -r knowledge && useradd -r -g knowledge -d /app -s /bin/bash knowledge

# 设置国内镜像
ENV HF_ENDPOINT="https://hf-mirror.com"

# 从构建阶段复制已安装的 Python 包
COPY --from=builder /root/.local /usr/local

# 复制项目代码
COPY --chown=knowledge:knowledge . .

# 创建必要目录并设置权限
RUN mkdir -p logs/audit chat_history chroma_db && \
    chown -R knowledge:knowledge /app

# 切换到非 root 用户
USER knowledge

# 暴露端口
EXPOSE 8501

# 健康检查
HEALTHCHECK --interval=30s --timeout=10s --start-period=60s --retries=3 \
    CMD curl -f http://localhost:8501/_stcore/health || exit 1

# 启动命令
CMD ["streamlit", "run", "app.py", \
     "--server.port=8501", \
     "--server.address=0.0.0.0", \
     "--server.headless=true", \
     "--server.enableCORS=false", \
     "--server.enableXsrfProtection=false"]

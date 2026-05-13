# 知识库智能助手 Docker 镜像
FROM python:3.11-slim

LABEL maintainer="knowledge-team"
LABEL description="企业级 RAG 知识库智能问答系统"

# 设置工作目录
WORKDIR /app

# 安装系统依赖
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    && rm -rf /var/lib/apt/lists/*

# 设置国内镜像（可选，构建时通过 --build-arg 控制）
ARG USE_MIRROR=false
ENV HF_ENDPOINT="https://hf-mirror.com"

# 复制依赖文件
COPY requirements.txt .

# 安装 Python 依赖
RUN pip install --no-cache-dir -r requirements.txt

# 复制项目代码
COPY . .

# 创建必要目录
RUN mkdir -p logs/audit chat_history chroma_db

# 暴露 Streamlit 端口
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

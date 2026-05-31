"""配置管理模块。

使用 Pydantic 进行配置校验，支持环境变量替换和单例访问。
"""

import os
import re
from pathlib import Path
from typing import Optional

import yaml
from pydantic import BaseModel, Field, field_validator


# ── 环境变量替换 ──

_ENV_VAR_PATTERN = re.compile(r"\$\{(\w+)(?::-([^}]*))?\}")


def _resolve_env_vars(value: str) -> str:
    """替换字符串中的 ${VAR_NAME} 或 ${VAR_NAME:-default} 为环境变量值。"""
    def _replace(match):
        var_name = match.group(1)
        default_val = match.group(2)
        env_val = os.environ.get(var_name)
        if env_val:
            return env_val
        if default_val is not None:
            return default_val
        return match.group(0)
    return _ENV_VAR_PATTERN.sub(_replace, value)


def _resolve_dict(obj):
    """递归替换字典中所有字符串值的环境变量。"""
    if isinstance(obj, dict):
        return {k: _resolve_dict(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [_resolve_dict(item) for item in obj]
    elif isinstance(obj, str):
        return _resolve_env_vars(obj)
    return obj


# ── 本地模型检测 ──

def detect_local_models(model_root: str = None) -> None:
    """检测本地模型并设置 EMBEDDING_LOCAL_PATH / RERANKER_LOCAL_PATH 环境变量。

    支持两种布局：
      1) 扁平目录：model/text2vec-base-chinese/、model/bge-reranker-base/
      2) HuggingFace 缓存：model/models--*--*/snapshots/<hash>/

    应在 app 启动早期调用，确保 config.yaml 中的 ${VAR:-} 占位符能正确解析。
    幂等调用：已有环境变量时不覆盖。
    """
    import logging
    _logger = logging.getLogger(__name__)

    if model_root is None:
        model_root = os.environ.get("MODEL_ROOT", "model")
    root = Path(model_root).resolve()

    def _find_snapshot(cache_name: str, flat_name: str) -> str:
        # 1) 扁平目录
        flat = root / flat_name
        if flat.is_dir():
            cfg = flat / "config.json"
            if cfg.exists():
                return str(flat)

        # 2) HF 缓存结构
        hf_cache = root / cache_name
        snapshots_dir = hf_cache / "snapshots"
        if snapshots_dir.is_dir():
            snapshot_dirs = sorted(
                [d for d in snapshots_dir.iterdir() if d.is_dir()],
                key=lambda d: d.stat().st_mtime, reverse=True,
            )
            for snap in snapshot_dirs:
                cfg = snap / "config.json"
                has_weights = any(
                    (snap / f).exists()
                    for f in ("pytorch_model.bin", "model.safetensors", "tf_model.h5")
                )
                if cfg.exists() and has_weights:
                    return str(snap)

        return ""

    # Embedding 模型
    if not os.environ.get("EMBEDDING_LOCAL_PATH"):
        emb_path = _find_snapshot(
            "models--shibing624--text2vec-base-chinese", "text2vec-base-chinese"
        )
        if emb_path:
            os.environ["EMBEDDING_LOCAL_PATH"] = emb_path
            _logger.debug("检测到本地 Embedding 模型: %s", emb_path)

    # Reranker 模型
    if not os.environ.get("RERANKER_LOCAL_PATH"):
        reranker_path = _find_snapshot(
            "models--BAAI--bge-reranker-base", "bge-reranker-base"
        )
        if reranker_path:
            os.environ["RERANKER_LOCAL_PATH"] = reranker_path
            _logger.debug("检测到本地 Reranker 模型: %s", reranker_path)


# ── Pydantic 模型 ──

class LLMConfig(BaseModel):
    """LLM 配置。"""
    api_base: str = "https://open.bigmodel.cn/api/paas/v4"
    api_key: str = "EMPTY"
    model: str = "glm-4-flash"
    temperature: float = Field(default=0.3, ge=0.0, le=2.0)
    max_tokens: int = Field(default=2048, ge=1, le=128000)
    context_window: int = Field(default=32768, ge=1024, le=256000)


class EmbeddingConfig(BaseModel):
    """Embedding 模型配置。"""
    model: str = "shibing624/text2vec-base-chinese"
    local_path: str = ""


class RerankerConfig(BaseModel):
    """Cross-Encoder Reranker 模型配置。"""
    model: str = "BAAI/bge-reranker-base"
    local_path: str = ""
    enabled: bool = True
    top_n: int = Field(default=10, ge=1, le=50)


class VectorStoreConfig(BaseModel):
    """向量库配置。"""
    persist_directory: str = "./chroma_db"
    collection_name: str = "knowledge_base"
    top_k: int = Field(default=5, ge=1, le=100)
    distance_threshold: float = Field(default=400.0, ge=0.0)


class KnowledgeConfig(BaseModel):
    """知识库配置。"""
    docs_directory: str = "./knowledge"
    chunk_size: int = Field(default=500, ge=50, le=10000)
    chunk_overlap: int = Field(default=50, ge=0, le=1000)

    @field_validator("chunk_overlap")
    @classmethod
    def overlap_less_than_chunk_size(cls, v, info):
        if "chunk_size" in info.data and v >= info.data["chunk_size"]:
            raise ValueError("chunk_overlap 必须小于 chunk_size")
        return v


class RateLimitConfig(BaseModel):
    """速率限制配置。"""
    enabled: bool = True
    max_requests_per_minute: int = Field(default=30, ge=1)
    max_input_length: int = Field(default=2000, ge=100, le=10000)


class UIConfig(BaseModel):
    """UI 配置。"""
    title: str = "智能知识库终端"
    subtitle: str = "知识库检索 · 接口查询 · 参数说明 · 代码示例"
    company_name: str = ""
    company_url: str = ""
    logo_text: str = "◈"
    default_theme: str = Field(default="dark", pattern="^(dark|light)$")


class AuthConfig(BaseModel):
    """用户认证配置。"""
    enabled: bool = True
    users_file: str = "./data/users.json"
    min_password_length: int = Field(default=8, ge=4, le=64)
    admin_users: list[str] = []


class AppConfig(BaseModel):
    """应用全局配置。"""
    # 应用版本号
    version: str = "0.18.18"
    # 本地模型根目录（离线部署时设置环境变量 MODEL_ROOT）
    model_root: str = "model"
    llm: LLMConfig = Field(default_factory=LLMConfig)
    embedding: EmbeddingConfig = Field(default_factory=EmbeddingConfig)
    reranker: RerankerConfig = Field(default_factory=RerankerConfig)
    vectorstore: VectorStoreConfig = Field(default_factory=VectorStoreConfig)
    knowledge: KnowledgeConfig = Field(default_factory=KnowledgeConfig)
    rate_limit: RateLimitConfig = Field(default_factory=RateLimitConfig)
    ui: UIConfig = Field(default_factory=UIConfig)
    auth: AuthConfig = Field(default_factory=AuthConfig)
    # 多轮对话配置
    max_conversation_turns: int = Field(default=10, ge=0, le=50)
    # 审计日志
    audit_enabled: bool = True
    # 管理员用户名列表
    admin_users: list[str] = []

    @classmethod
    def from_yaml(cls, config_path: str = "config.yaml") -> "AppConfig":
        """从 YAML 文件加载配置，自动替换环境变量。"""
        path = Path(config_path)
        if not path.exists():
            raise FileNotFoundError(f"配置文件不存在: {config_path}")

        with open(path, "r", encoding="utf-8") as f:
            raw = yaml.safe_load(f) or {}

        # 递归替换环境变量
        resolved = _resolve_dict(raw)

        return cls(**resolved)


# ── 全局单例 ──

_config_instance: Optional[AppConfig] = None


def get_config(config_path: str = "config.yaml") -> AppConfig:
    """获取全局配置单例。"""
    global _config_instance
    if _config_instance is None:
        _config_instance = AppConfig.from_yaml(config_path)
    return _config_instance


def reload_config(config_path: str = "config.yaml") -> AppConfig:
    """强制重新加载配置（用于运行时切换）。"""
    global _config_instance
    _config_instance = AppConfig.from_yaml(config_path)
    return _config_instance


def load_config(config_path: str = "config.yaml") -> dict:
    """加载配置并转为字典（兼容需要 dict 的旧接口）。

    推荐新代码直接使用 get_config() 返回的 Pydantic 对象。
    """
    config = get_config(config_path)
    return config.model_dump()

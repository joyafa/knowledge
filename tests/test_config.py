"""配置模块测试。"""

import os
import tempfile
from pathlib import Path

import pytest
import yaml

from rag.config import (
    AppConfig,
    LLMConfig,
    VectorStoreConfig,
    KnowledgeConfig,
    _resolve_env_vars,
    _resolve_dict,
    get_config,
)


class TestEnvVarResolution:
    """环境变量替换测试。"""

    def test_simple_env_var(self):
        os.environ["TEST_VAR"] = "hello"
        result = _resolve_env_vars("prefix_${TEST_VAR}_suffix")
        assert result == "prefix_hello_suffix"

    def test_env_var_with_default(self):
        result = _resolve_env_vars("${NONEXISTENT:-default_value}")
        assert result == "default_value"

    def test_env_var_no_default_missing(self):
        result = _resolve_env_vars("${NONEXISTENT}")
        assert result == "${NONEXISTENT}"  # 保留原文

    def test_resolve_dict(self):
        os.environ["API_KEY"] = "secret123"
        data = {
            "llm": {
                "api_key": "${API_KEY}",
                "model": "test-model",
            },
            "items": ["${API_KEY}", "static"],
        }
        resolved = _resolve_dict(data)
        assert resolved["llm"]["api_key"] == "secret123"
        assert resolved["items"][0] == "secret123"
        assert resolved["items"][1] == "static"


class TestPydanticModels:
    """Pydantic 配置模型测试。"""

    def test_llm_config_defaults(self):
        config = LLMConfig()
        assert config.temperature == 0.3
        assert config.max_tokens == 2048

    def test_llm_config_validation(self):
        with pytest.raises(Exception):
            LLMConfig(temperature=3.0)  # 超出 [0, 2] 范围

    def test_vectorstore_config_validation(self):
        with pytest.raises(Exception):
            VectorStoreConfig(top_k=0)  # 必须 >= 1

    def test_knowledge_config_validation(self):
        with pytest.raises(Exception):
            KnowledgeConfig(chunk_size=100, chunk_overlap=200)  # overlap >= chunk_size

    def test_full_config_from_yaml(self):
        yaml_content = {
            "llm": {
                "api_base": "http://localhost:8000/v1",
                "api_key": "test-key",
                "model": "test-model",
            },
            "embedding": {
                "model": "test-emb",
                "local_path": "",
            },
            "vectorstore": {
                "persist_directory": "./test_db",
                "collection_name": "test",
            },
            "knowledge": {
                "docs_directory": "./test_docs",
            },
            "ui": {},
        }
        config = AppConfig(**yaml_content)
        assert config.llm.model == "test-model"
        assert config.embedding.model == "test-emb"
        assert config.ui.title == "智能知识库终端"  # 默认值


class TestConfigFromYamlFile:
    """从文件加载配置测试。"""

    def test_load_from_file(self):
        with tempfile.NamedTemporaryFile(mode="w", suffix=".yaml", delete=False) as f:
            yaml.dump({
                "llm": {"model": "file-model"},
                "embedding": {"model": "file-emb"},
                "vectorstore": {},
                "knowledge": {},
            }, f)
            temp_path = f.name

        try:
            config = AppConfig.from_yaml(temp_path)
            assert config.llm.model == "file-model"
            assert config.embedding.model == "file-emb"
        finally:
            os.unlink(temp_path)

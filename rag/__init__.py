"""RAG 知识库检索引擎。"""


def _get_version() -> str:
    """从 config.yaml 读取版本号，读取失败时回退到硬编码默认值。"""
    try:
        import yaml
        from pathlib import Path
        config_path = Path(__file__).resolve().parent.parent / "config.yaml"
        if config_path.exists():
            with open(config_path, "r", encoding="utf-8") as f:
                config = yaml.safe_load(f) or {}
            return config.get("version", "0.8.17")
    except Exception:
        pass
    return "0.8.17"


__version__ = _get_version()

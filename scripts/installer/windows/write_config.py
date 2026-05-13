"""安装时写入 LLM 配置到 config.yaml。

由 NSIS 安装向导调用：
  python write_config.py <config_path> <api_base> <api_key> <model>
"""

import sys
from pathlib import Path


def update_config(config_path: str, api_base: str, api_key: str, model: str):
    """更新 config.yaml 中的 LLM 配置。"""
    path = Path(config_path)
    if not path.exists():
        print(f"配置文件不存在: {path}")
        return

    import yaml

    with open(path, "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)

    if api_base:
        config["llm"]["api_base"] = api_base
    if api_key:
        config["llm"]["api_key"] = api_key
    if model:
        config["llm"]["model"] = model

    with open(path, "w", encoding="utf-8") as f:
        yaml.dump(config, f, default_flow_style=False, allow_unicode=True, sort_keys=False)

    print(f"配置已更新: {path}")


if __name__ == "__main__":
    if len(sys.argv) < 5:
        print("用法: python write_config.py <config_path> <api_base> <api_key> <model>")
        sys.exit(1)
    update_config(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])

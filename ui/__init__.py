"""UI 包 — Streamlit 界面组件。"""

import base64
from pathlib import Path

# 项目根目录（logo.png 所在位置）
_PROJECT_ROOT = Path(__file__).resolve().parent.parent
_LOGO_PATH = _PROJECT_ROOT / "logo.png"


def get_logo_base64() -> str:
    """获取 logo 图片的 base64 编码字符串（data URI 格式）。

    Returns:
        "data:image/png;base64,..." 或空字符串（文件不存在时）。
    """
    if not _LOGO_PATH.exists():
        return ""
    with open(_LOGO_PATH, "rb") as f:
        b64 = base64.b64encode(f.read()).decode()
    return f"data:image/png;base64,{b64}"


def render_logo_img(width: int = 64, extra_style: str = "") -> str:
    """生成 logo <img> 标签的 HTML 字符串。

    Args:
        width: 图片宽度（像素）
        extra_style: 额外的 CSS 样式

    Returns:
        <img> 标签字符串，文件不存在时返回 fallback 文字 "◈"
    """
    data_uri = get_logo_base64()
    if not data_uri:
        return "◈"
    return (
        f'<img src="{data_uri}" width="{width}" '
        f'style="display:inline-block;vertical-align:middle;{extra_style}" '
        f'alt="logo" />'
    )

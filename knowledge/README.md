# 知识库文档目录

将你的 Markdown 知识库文档放在这里。

## 使用方式

1. 将 `.md` 文件放入此目录（支持子目录）
2. 运行 `python scripts/ingest.py` 入库
3. 启动 `streamlit run app.py` 开始使用

## 文档格式建议

```markdown
# API 名称

## 功能概述
简要描述这个 API 的用途。

## 参数说明
| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| xxx    | string | 是   | xxx  |

## 代码示例
​```python
# 示例代码
​```
```

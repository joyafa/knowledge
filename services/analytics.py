"""分析仪表盘服务。

从审计日志中提取统计数据：查询量、热门文档、API 用量等。
"""

import json
from datetime import datetime, timedelta
from pathlib import Path
from typing import Optional

from rag.logging_config import AUDIT_DIR, get_logger

logger = get_logger(__name__)


def get_dashboard_stats(days: int = 7) -> dict:
    """获取仪表盘统计数据。

    Args:
        days: 统计最近几天的数据

    Returns:
        统计字典
    """
    stats = {
        "total_queries": 0,
        "unique_users": set(),
        "avg_result_count": 0,
        "no_result_count": 0,
        "total_feedback_positive": 0,
        "total_feedback_negative": 0,
        "daily_queries": {},
        "top_queries": [],
        "avg_latency_ms": 0,
    }

    query_counts: dict[str, int] = {}
    result_counts: list[int] = []
    latencies: list[float] = []

    cutoff_date = datetime.now() - timedelta(days=days)

    if not AUDIT_DIR.exists():
        return _finalize_stats(stats, query_counts, result_counts, latencies)

    for log_file in sorted(AUDIT_DIR.glob("*.jsonl"), reverse=True):
        # 解析日期
        try:
            file_date = datetime.strptime(log_file.stem, "%Y-%m-%d")
            if file_date < cutoff_date:
                continue
        except ValueError:
            continue

        try:
            with open(log_file, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    try:
                        entry = json.loads(line)
                    except json.JSONDecodeError:
                        continue

                    action = entry.get("action", "")

                    if action == "query":
                        stats["total_queries"] += 1
                        username = entry.get("username", "unknown")
                        stats["unique_users"].add(username)

                        result_count = entry.get("result_count", 0)
                        result_counts.append(result_count)
                        if result_count == 0:
                            stats["no_result_count"] += 1

                        duration = entry.get("duration_ms", 0)
                        if duration > 0:
                            latencies.append(duration)

                        # 日统计
                        date_key = entry.get("timestamp", "")[:10]
                        if date_key:
                            stats["daily_queries"][date_key] = stats["daily_queries"].get(date_key, 0) + 1

                        # 查询频次
                        query = entry.get("query", "")
                        if query:
                            query_counts[query] = query_counts.get(query, 0) + 1

                    elif action == "feedback":
                        fb = entry.get("details", "")
                        if fb == "positive":
                            stats["total_feedback_positive"] += 1
                        elif fb == "negative":
                            stats["total_feedback_negative"] += 1
        except Exception as e:
            logger.warning("读取审计日志失败 %s: %s", log_file, e)

    return _finalize_stats(stats, query_counts, result_counts, latencies)


def _finalize_stats(stats: dict, query_counts: dict, result_counts: list, latencies: list) -> dict:
    """计算汇总统计。"""
    stats["unique_users"] = len(stats["unique_users"])

    # 平均结果数
    stats["avg_result_count"] = round(sum(result_counts) / len(result_counts), 1) if result_counts else 0

    # 平均延迟
    stats["avg_latency_ms"] = round(sum(latencies) / len(latencies), 1) if latencies else 0

    # Top 查询
    sorted_queries = sorted(query_counts.items(), key=lambda x: x[1], reverse=True)
    stats["top_queries"] = [{"query": q[:80], "count": c} for q, c in sorted_queries[:10]]

    # 日查询序列
    stats["daily_queries"] = dict(sorted(stats["daily_queries"].items()))

    return stats


def get_today_summary() -> dict:
    """获取今日摘要。"""
    return get_dashboard_stats(days=1)

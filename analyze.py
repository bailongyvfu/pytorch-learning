from __future__ import annotations

import json
import argparse
from pathlib import Path
from typing import Optional


# import json
# import argparse
# from pathlib import Path

# def load_data(filepath):
#     path = Path(filepath)
#     if not path.exists():
#         raise FileNotFoundError(f"文件不存在: {filepath}")
#     with open(path, "r", encoding="utf-8") as f:
#         return json.load(f)

# def compute_stats(students):
#     scores = [s["score"] for s in students]
#     return {
#         "count": len(scores),
#         "mean": sum(scores) / len(scores),
#         "max": max(scores),
#         "min": min(scores),
#         "top_student": max(students, key=lambda s: s["score"])["name"]
#     }
data={}
import time
import functools

def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"{func.__name__} 耗时 {elapsed:.4f} 秒")
        return result
    return wrapper

import functools
import time

def retry(max_attempts=3, delay=1.0):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"第 {attempt} 次失败: {e}")
                    if attempt == max_attempts:
                        raise
                    time.sleep(delay)
        return wrapper
    return decorator

@retry(max_attempts=3, delay=0.5)
def unstable_request():
    import random
    if random.random() < 0.7:
        raise ConnectionError("网络波动")
    return "成功"


@retry(max_attempts=3, delay=0.1)
@timer
def load_data(filepath: str) -> Optional[dict]:
    path = Path(filepath)
    if not path.exists():
        raise FileNotFoundError(f"文件不存在: {filepath}")
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)    

@timer
def compute_stats(students: list[dict]) -> dict:
    scores = [s["score"] for s in students]
    return {
        
        "count": len(scores),
        "mean": sum(scores) / len(scores),
        "max": max(scores),
        "min": min(scores),
        "top_student": max(students, key=lambda s: s["score"])["name"]
    }

def main():
    parser = argparse.ArgumentParser(description="学生成绩统计工具")
    parser.add_argument("filepath", help="JSON文件路径")
    args = parser.parse_args()

    data = load_data(args.filepath)
    stats = compute_stats(data["students"])

    print(f"学生人数: {stats['count']}")
    print(f"平均分: {stats['mean']:.1f}")
    print(f"最高分: {stats['max']} ({stats['top_student']})")
    print(f"最低分: {stats['min']}")

if __name__ == "__main__":
    main()
#python analyze.py data.json
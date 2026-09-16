import json
import argparse
from pathlib import Path

def load_data(filepath):
    path = Path(filepath)
    if not path.exists():
        raise FileNotFoundError(f"文件不存在: {filepath}")
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def compute_stats(students):
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
def compute_stats(numbers):
    total = sum(numbers)
    mean = total / len(numbers)
    variance = sum((x - mean) ** 2 for x in numbers) / len(numbers)
    return {"total": total, "mean": mean, "variance": variance}

data = [12, 7, 19, 4, 23, 15]
result = compute_stats(data)
print(result)
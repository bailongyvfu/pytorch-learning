# from typing import Optional

# def compute_stats(students: list[dict]) -> dict:
#     ...

# def load_data(filepath: str) -> Optional[dict]:
#     ...

# def greet(name: str) -> str:
#     return "Hello, " + name

# greet(123)   # Pylance 会标红：参数类型不匹配

# def train(model, data, *, lr: float = 1e-3, epochs: int = 10, **kwargs):
#     print(f"lr={lr} ({type(lr).__name__}), epochs={epochs} ({type(epochs).__name__})")
#     print(f"kwargs={kwargs}")

# train("m", "d", lr=0.01, epochs=20, weight_decay=1e-4)
# train("m", "d", lr=1, epochs="20")   # 运行时不会报错，但 Pylance 会警告
# try:
#     train("m", "d", 0.01, 20)        # 这里会报 TypeError
# except TypeError as e:
#     print(f"TypeError: {e}")

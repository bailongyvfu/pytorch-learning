# def make_counter():
#     count = 0
#     def counter():
#         nonlocal count
#         count += 1
#         return count
#     return counter

# c = make_counter()
# print(c())  # 1
# print(c())  # 2
# print(c())  # 3

# def my_decorator(func):
#     def wrapper():
#         print("函数执行前")
#         func()
#         print("函数执行后")
#     return wrapper

# @my_decorator
# def say_hello():
#     print("Hello")

# say_hello()


# import functools

# def my_decorator(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         print(f"调用 {func.__name__}")
#         result = func(*args, **kwargs)
#         return result
#     return wrapper

# @my_decorator
# def say_hello():
#     print("Hello")

# say_hello()

# import functools

# def my_decorator(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         print(f"调用 {func.__name__}")
#         result = func(*args, **kwargs)
#         return result
#     return wrapper


# import time
# import functools

# def timer(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         start = time.perf_counter()
#         result = func(*args, **kwargs)
#         elapsed = time.perf_counter() - start
#         print(f"{func.__name__} 耗时 {elapsed:.4f} 秒")
#         return result
#     return wrapper

# @timer
# def slow_sum(n):
#     return sum(range(n))


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

print(unstable_request())

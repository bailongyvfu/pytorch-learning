# def append_log(msg, log=None):
#     if log is None:
#         log = []
#     log.append(msg)
#     return log

# q = append_log("start")
# print(append_log("start"))        # ['start']
# print(append_log("loading"))      # ['loading']
# print(append_log("done"))         # ['done']
# print(append_log("loading",q))   
# my_log = ["init"]
# append_log("start", my_log)
# print(my_log)  # ['init', 'start']

# def show(*args, **kwargs):
#     print(f"args = {args}")
#     print(f"kwargs = {kwargs}")

# show(1, 2, 3, name="Alice", age=30)
# # args = (1, 2, 3)
# # kwargs = {'name': 'Alice', 'age': 30}

def log_config(**kwargs):
    # kwargs 是字典，遍历字典的每一组键值对
    for key, value in kwargs.items():
        print(f"{key} = {value}")

# 测试调用
log_config(host="127.0.0.1", port=8080, debug=True)


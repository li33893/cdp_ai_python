"""

用法一：两个值比大小
直接传两个参数，返回较大的那个：
pythonprint(max(3, 7))    # 7
print(max(10, 2))   # 10

用法二：从一个可迭代对象里找最大值，带 key=
key= 接收一个函数，max() 会对每个元素调用这个函数，根据返回值来比大小，但最终返回的是原始元素，不是函数返回值。
words = ["cat", "elephant", "dog"]
print(max(words, key=len))   # "elephant"，按字符串长度比

posts = [
    {"id": "a1", "score": 15},
    {"id": "a2", "score": 42},
    {"id": "a3", "score": 7},
]
print(max(posts, key=lambda p: p["score"]))   # {"id": "a2", "score": 42}

"""

# 用法一：找到1， 27, 29， 100中的最大值
print(max(1, 27, 29, 100))

# 用法二：定义 records = [{"name": "Alice", "age": 29}, {"name": "Bob", "age": 34}, {"name": "Carol", "age": 21}]，用 max() 加 key= 找出年龄最大的那条记录并打印

records = [{"name": "Alice", "age": 29}, {"name": "Bob", "age": 34}, {"name": "Carol", "age": 21}]
print(max(records, key=lambda x:x["age"]))
"""

list comprehension 列表推导式
[装什么  for 变量 in 列表  if 条件]   
 
"""

# 从列表里挑出含有 "b" 的水果，装进新列表（列表推导式），把水果的大写装进新的列表里

fruits = ["apple", "banana", "cherry", "blueberry"]
result = []
for f in fruits:
    if "b" in f:
        result.append(f)

# 2. 用列表推导式可以压缩成一行
result = [f.upper() for f in fruits if "b" in f]

print(result)
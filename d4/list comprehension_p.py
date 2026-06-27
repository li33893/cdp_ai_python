# 从列表里挑出含有 "b" 的水果，装进新列表（），把水果的大写装进新的列表里

fruits = ["apple", "banana", "cherry", "blueberry"]

result = [fruit.upper() for fruit in fruits if "b" in fruit]

print(result)
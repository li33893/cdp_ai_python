"""
list 切片是从一个列表里"截取"出一段来，得到一个新列表。语法是 列表[start:end]，
取出的是从 start 位置开始、到 end 位置之前（不含 end）的元素。

fruits = ["apple", "banana", "cherry", "date", "elderberry"]

print(fruits[1:3])   # ["banana", "cherry"]，取下标1和2，不含3
print(fruits[:2])    # ["apple", "banana"]，从头到下标2之前
print(fruits[2:])    # ["cherry", "date", "elderberry"]，从下标2到结尾
print(fruits[-2:])   # ["date", "elderberry"]，倒数两个

"""

#  写一个列表 numbers = [10, 20, 30, 40, 50, 60, 70]，然后分别打印：前三个元素、最后两个元素、下标 2 到 5（不含 5）的元素
numbers = [10, 20, 30, 40, 50, 60, 70]

# 前三个元素
print(numbers[:3])

# 最后两个元素
print(numbers[-2:])

# 下标2到5（不含5）
print(numbers[2:5])
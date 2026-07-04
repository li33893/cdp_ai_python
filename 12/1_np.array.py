"""

np.array()

普通 Python 列表做 == 是什么结果？
a = [1, 2, 3]
b = [1, 0, 3]
print(a == b)
这里 a == b 是「整个列表和整个列表比」，结果是一个 False（因为两个列表不完全相同）。它不会逐个元素比。

numpy 数组不一样。
import numpy as np
a = np.array([1, 2, 3])
b = np.array([1, 0, 3])
print(a == b)
numpy 的 == 是「逐个元素比」。它会拿 a 的第0个和 b 的第0个比，a 的第1个和 b 的第1个比……每一对得到一个 True/False，最后拼成一个新数组：
[ True False  True]
这个由 True/False 组成的数组，就叫布尔数组。
一句话规则：numpy 数组之间用 ==，得到的是一个逐元素比较的布尔数组，不是单个 True/False。


"""


 
# 题1（预测题，先不要运行）
# 下面代码打印什么？先写下你的预测，再运行验证。
import numpy as np
x = np.array([5, 5, 5])
y = np.array([5, 6, 5])
print(x == y)

# [True, False, True]

# 题2（操作题）
# 用 numpy 写代码：有两个评分者的打分 [1, 1, 0, 1] 和 [1, 0, 0, 1]，打印出「他们每一位是否一致」的布尔数组。要求必须用 np.array()，不能用 for 循环。
a = np.array([1, 1, 0, 1])
b = np.array([1, 0, 0, 1])
print(a == b)
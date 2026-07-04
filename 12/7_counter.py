"""

Counter 

是干嘛的:数一个列表里,每个东西各出现了几次。
你手动数过「苹果几个、香蕉几个」。Counter 就是自动帮你数:

from collections import Counter

labels = ["ES", "CO", "ES", "TA", "ES", "CO"]
print(Counter(labels))

输出:
Counter({'ES': 3, 'CO': 2, 'TA': 1})
它扫一遍列表,数出:ES 出现 3 次、CO 2 次、TA 1 次,自动按次数从多到少排。
和你学过的 .value_counts() 是什么关系?

.value_counts() 用在 pandas 的列上(d10 学过)
Counter() 用在普通 Python 列表上

两个干的是同一件事(数频率),只是对象不同。项目里 human_labels 是个普通列表,所以用 Counter。

"""

# 题1(预测题,先不要运行)
from collections import Counter
x = ["a", "b", "a", "c", "a", "b"]
c = Counter(x)
print(c)
print(c["a"])
print(c["z"])

# 三行各打印什么?(注意最后一行查的是没出现过的 "z")
# [{'a':3...}]
# 3
# 0

# 题2(操作题)
# 有一串判断 codes = ["Habitual", "Episodic", "Habitual", "NM", "Habitual", "Episodic"]。用 Counter 数出每类各几次并打印。再单独打印出 "Habitual" 出现的次数。
codes      = ["Habitual", "Episodic", "Habitual", "NM", "Habitual", "Episodic"]
code_count = Counter(codes)
print(code_count)
print(code_count["Habitual"])
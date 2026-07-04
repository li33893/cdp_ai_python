# 题1(预测题,先不要运行)
from collections import Counter
x = ["a", "b", "a", "c", "a", "b"]
c = Counter(x)
print(c)
print(c["a"])
print(c["z"])

# 三行各打印什么?(注意最后一行查的是没出现过的 "z")


# 题2(操作题)
# 有一串判断 codes = ["Habitual", "Episodic", "Habitual", "NM", "Habitual", "Episodic"]。用 Counter 数出每类各几次并打印。再单独打印出 "Habitual" 出现的次数。

"""

布尔值在做加法时会被当成数字
 里 True 等于 1，False 等于 0。这不是 numpy 特有的，普通 Python 就这样：
print(True + True)   # 2
print(False + True)  # 1

np.sum() 对布尔数组求和 = 数 True 的个数
上一步你得到过 [ True False  True  True]。把它交给 np.sum()：
import numpy as np
arr = np.array([True, False, True, True])
print(np.sum(arr))   # 3
因为 True 算 1、False 算 0，加起来就是 1+0+1+1 = 3，正好是 True 的个数。
一句话规则：np.sum(布尔数组) 数的是 True 有几个。

这两步合起来，就是 agreement_check.py 里那行的完整含义：
p_o = np.sum(r1 == r2) / n
r1 == r2 先得到布尔数组（哪些位一致），np.sum(...) 数出一致的个数，再除以总数 n，就是一致率（observed agreement）。

"""

# 题1（预测题，先不要运行）
# 下面打印什么？

import numpy as np
arr = np.array([True, True, False, True, False])
print(np.sum(arr))
# 3

# 题2（操作题）
# 两个评分者：[1, 0, 1, 1, 0] 和 [1, 0, 0, 1, 1]。
# 用 numpy 算出他们的一致率（一致的位数 ÷ 总位数），打印出来。要求用上 np.array()、==、np.sum()，不能用 for 循环。

a = np.array([1, 0, 1, 1, 0])
b = np.array([1, 0, 0, 1, 1])

agreed    = np.sum(a == b)
disagreed = np.sum(a != b)

rate = agreed/(agreed+disagreed)

print(rate)
"""

讲两个 numpy 函数:np.sqrt() 和 np.trace()。这俩是新的,前面没出现过。

np.sqrt() —— 开平方
import numpy as np
print(np.sqrt(9))    # 3.0
print(np.sqrt(2))    # 1.4142135...
就是数学的 √。cohens_kappa/gwet 的方差计算里会用到,单独看很简单。

np.trace() —— 矩阵的迹
「迹」是二维矩阵主对角线上的元素之和(从左上到右下那条斜线)。
import numpy as np
m = np.array([[5, 1, 0],
              [2, 8, 1],
              [0, 3, 7]])
print(np.trace(m))   # 5 + 8 + 7 = 20
对角线是 5, 8, 7,加起来 20。
为什么重要:在混淆矩阵里,主对角线正好代表「两个评分者判断一致」的格子。所以 np.trace(混淆矩阵) 一步就能算出「一共有多少次一致」。
这就是 rickwood_validation.py 里 po = np.trace(cm) / n 的含义。

"""

# 题1(预测题,先不要运行)
import numpy as np
m = np.array([[1, 9, 9],
              [9, 2, 9],
              [9, 9, 3]])
print(np.trace(m))
# 打印什么?
# 6


# 题2(操作题)
# 自己用 np.array() 建一个 2×2 矩阵 [[10, 4], [7, 20]],用 np.trace() 打印它的迹。再用 np.sqrt() 打印这个迹的平方根。
matrix  = np.array([[10, 4], 
                   [7, 20]])

trace_m = np.trace(matrix)
sqrt_m  = np.sqrt(trace_m)

print(trace_m)
print(sqrt_m)
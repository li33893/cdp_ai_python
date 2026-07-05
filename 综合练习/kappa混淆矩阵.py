# 题1
# 两个评分者:a = [1, 0, 1, 1, 0],b = [1, 1, 1, 0, 0]。算出他们的一致率(判得一样的位数 ÷ 总位数),打印。不许用 for 循环。

import numpy as np

a = np.array([1, 0, 1, 1, 0])
b = np.array([1, 1, 1, 0, 0])

agreed = sum(a == b)
rate   = agreed/len(a)
print(f"一致率：{rate:.1%}")



# 题2
# codes = ["ES", "CO", "ES", "TA", "ES", "CO", "N"]。打印每类各出现几次,再单独打印 "ES" 出现的次数。
from collections import Counter

codes = ["ES", "CO", "ES", "TA", "ES", "CO", "N"]
show  = Counter(codes)
print(show)
print(show["ES"])


# 题3
# human = ["A", "B", "A", "C", "B"]
# llm   = ["A", "B", "C", "C", "B"]
# 打印这两串判断的 κ 值;
# 再打印一张混淆矩阵,类别顺序按 ["A","B","C"] 排。
from sklearn.metrics import cohen_kappa_score, confusion_matrix
import pandas as pd

human = ["A", "B", "A", "C", "B"]
llm   = ["A", "B", "C", "C", "B"]

kappa           = cohen_kappa_score(human, llm)
cm              = confusion_matrix(human, llm, labels=["A", "B", "C"])
df              = pd.DataFrame(cm, index=["A","B","C"], columns=["A","B","C"])
df.index.name   = "human"
df.columns.name = "llm"

print(kappa)
print(df)

# 题4(不用写代码)
# cm = [[6 2 0]
#       [1 5 1]
#       [0 2 4]]

# (a) 这张表对角线加起来是几?代表什么?
# 15。代表两个评分者结果一致的情况
# (b) 每一行分别加起来是多少?(三个数)
# 8 6 6
# (c) 每一列分别加起来是多少?(三个数)
# 7 9 5

# 题5
# 写一小段脚本:

# 从命令行接一个参数 --input,默认值 "data.csv"
# 从这个路径里取出不带扩展名的文件名(data.csv → data)
# 写一个函数 backoff(n),加上类型注解,返回 2 的 n 次方
# 打印文件名,和 backoff(3) 的结果

import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("--input", default="data.csv")
args   = parser.parse_args()


file = os.path.splitext(args.input)[0]

def backoff(n:int):
    return 2**n

bo = backoff(3)

print(file)
print(bo)



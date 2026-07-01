"""
01-tilde
pandas 里，一列布尔值不能用 not，要用 ~。原因是 not 是 Python 内置操作符，只能作用于单个值，不知道怎么处理一整列。
~ 是专门为数组/Series 设计的，会逐元素翻转。

import pandas as pd

df = pd.DataFrame({
    "name": ["Alice", "Bob", "Carol"],
    "active": [True, False, True]
})

mask = df["active"] == True
print(mask)
# 0     True
# 1    False
# 2     True

print(~mask)
# 0    False
# 1     True
# 2    False
括号很重要。如果要组合条件再取反：
python# 取反整个括号里的条件
~(df["active"] == True)

# 多个条件组合后取反
~((df["active"] == True) | (df["name"] == "Bob"))



02-isin()


作用:判断一列里的每个值,是否属于给定的一组值。比 == 好在——== 只能判断"等于某一个值",isin() 能一次判断"是否属于多个值中的任意一个"。
不用 isin() 的写法(想找 subreddit 是 depression 或 Anxiety 的帖子):

df[(df["subreddit"] == "depression") | (df["subreddit"] == "Anxiety")]

用 isin():

df[df["subreddit"].isin(["depression", "Anxiety"])]

"""

import pandas as pd

df = pd.DataFrame({
    "post_id": ["p1", "p2", "p3", "p4", "p5", "p6"],
    "subreddit": ["depression", "therapy", "Anxiety", "mentalhealth", "depression", "therapyGPT"],
    "risk_level": [1, 3, 1, 2, 3, 1],
})

# 完成以下三步,分别 print 结果:

# 用 isin() 筛选出 subreddit 不属于 ["depression", "therapy"] 的帖子(用 ~ + isin())
# 构造一个 mask:risk_level == 3,赋值给 high_risk_mask,取出高风险的帖子
# 用 ~high_risk_mask 取出非高风险的帖子(不要重新写条件)

not_in_de_or_an = df[~(df["subreddit"].isin(["depression", "Anxiety"]))]
print(not_in_de_or_an)

mask = df["risk_level"] == 3
print(df[mask])

ksam = df[~mask]
print(ksam)
"""
Boolean Indexing — 用条件筛选行
想象你有一张表，想只保留满足某个条件的行。boolean indexing 就是干这个的。

"""

import pandas as pd

data = {"name": ["Alice", "Bob", "Charlie"], "age": [25, 17, 30]}
df   = pd.DataFrame(data)

df[df["age"] >= 18]
# 结果：
# nameageAlice25Charlie30
# df["age"] >= 18 先生成一列 True/False，然后 df[...] 只保留 True 的行。

# 多个条件用 & 连接：
# df[df["age"] >= 18 & df["age"] <= 28]  # ❌ 会出错
# df[(df["age"] >= 18) & (df["age"] <= 28)]  # ✅ 每个条件要加括号
#注意两点：

# & 不是 and，在 DataFrame 里必须用 &
# 每个条件必须用 () 括起来，不括会报错


#____________  练习 _________________________

#  1. 理解题： 下面的代码会保留哪几行？
# data = {"name": ["Alice", "Bob", "Charlie", "Diana"],
#         "score": [90, 45, 70, 55]}
# df = pd.DataFrame(data)

# result = df[(df["score"] >= 60) & (df["score"] <= 80)]

# charlie


#  2. 操作题： 从下面的 df 里筛出名字长度大于3、且 age 大于等于18的行，打印结果：
# import pandas as pd

# data = {"name": ["Alice", "Bob", "Charlie", "Di"],
#         "age": [25, 17, 30, 20]}
# df = pd.DataFrame(data)

# result = df[(df["age"]>18) & (df["name"].apply(len)>3)]
# print(result)


#  3. 加强题：
import pandas as pd

data = {
    "product": ["apple", "banana", "kiwi", "strawberry", "fig"],
    "price": [1.5, 0.8, 3.2, 2.1, 4.0],
    "in_stock": [True, False, True, True, False]
}
df = pd.DataFrame(data)
# 筛出：有货（in_stock 为 True）、价格低于 3.0、且名字长度超过 4 个字母的行，打印结果。

result = df[(df["in_stock"] == True) & (df["price"]<3.0) & (df["product"].apply(len)>4)]
print(result)
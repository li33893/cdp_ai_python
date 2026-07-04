"""
！！！！现在这个版本已经没有了，pandas2.0以后不加copy也没事了
.copy() — 创建独立副本
筛完数据之后，你通常会把结果存进一个新变量：
result = df[df["age"] >= 18]
但这里有个陷阱：result 不是独立的，它只是 df 的一个"窗口"。改 result 可能会连带影响 df，pandas 还会弹出警告。
加 .copy() 就解决了：
result = df[df["age"] >= 18].copy()
现在 result 是完全独立的新表，改它不会动 df。

"""

# 把boolean_indexing.py加强题的筛选结果加上 .copy()，然后给结果加一列 label，每行都是字符串 "selected"，打印最终结果

import pandas as pd

data = {
    "product": ["apple", "banana", "kiwi", "strawberry", "fig"],
    "price": [1.5, 0.8, 3.2, 2.1, 4.0],
    "in_stock": [True, False, True, True, False]
}
df = pd.DataFrame(data)
# 筛出：有货（in_stock 为 True）、价格低于 3.0、且名字长度超过 4 个字母的行，打印结果。

result = df[(df["in_stock"] == True) & (df["price"]<3.0) & (df["product"].apply(len)>4)]

result["label"] = "selected"

print(result)
print(df)
"""

df.iterrows — 逐行遍历表格

你在 Day 2 学过 .apply()，那是对整列统一做同一个操作。
iterrows 不一样，它让你一行一行手动处理，每行可以做不同的事，可以加 if 判断，可以跳过某行，可以调用函数。

for i, row in df.iterrows():
    print(i, row["name"])
i 是行号，从 0 开始。row 是这一行的数据，用列名取值，比如 row["name"]、row["score"]。

"""

# 用之前的 sample.csv
# 用 iterrows 遍历每一行，打印出每个人的名字和分数，格式如下：
# Alice 82
# Bob 45
# Carol 91

import pandas as pd

df = pd.read_csv("sample.csv")

for i, row in df.iterrows():
    print(row["name"], row["score"])


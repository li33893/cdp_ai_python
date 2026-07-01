"""

01_.fillna() 和 .notna()
.fillna()
作用:把一列里的缺失值(NaN)替换成你指定的值。

df["score"] = df["score"].fillna(0)

所有 NaN 变成 0,其他值不变。

df["note"] = df["note"].fillna("无备注")

字符串列同理,缺失的地方填成指定文字。

02_.notna()
作用:判断每个值是不是"非空"(不是 NaN),返回布尔 Series——跟你之前学的 mask 是同一套逻辑。
df["score"].notna()
结果是一串 True/False:值存在的地方是 True,是 NaN 的地方是 False。
常见用法:配合 .loc 或 df[...] 筛选出"有值的行":
df[df["score"].notna()]
反过来,.isna() 是判断"是不是空",跟 .notna() 刚好相反(等价于 ~df["score"].notna())。

"""

import pandas as pd
import numpy as np

df = pd.DataFrame({
    "post_id": ["p1", "p2", "p3", "p4", "p5"],
    "score": [10, np.nan, 30, np.nan, 50],
    "note": [None, "重要", None, "待查", None],
})

# 用 .fillna() 把 score 列的缺失值填成 0,print 结果
df["score"] = df["score"].fillna(0)
print(df["score"])
# 用 .fillna() 把 note 列的缺失值填成 "无备注",print 结果
df["note"] = df["note"].fillna("无备注")
print(df["note"])
# 用 .notna() 筛选出 score 列原本(填之前)不是缺失值的那些行(直接对原始 df 操作,不要用第1步填完的结果)
# have_score = df[df["score"].notna()]
# print(have_score)
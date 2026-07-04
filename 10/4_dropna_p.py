"""

.dropna() 

用来删除含有缺失值（NaN）的行（或列）。

import pandas as pd

df = pd.DataFrame({
    "post_id": ["p1", "p2", "p3", "p4"],
    "human_relevant": [True, None, False, True]
})

cleaned = df.dropna()
print(cleaned)

默认情况下，只要一行里任何一列有 NaN，这一行就会被删掉。


subset= 参数：如果 DataFrame 有很多列，但你只关心某一列是否为空，用 subset= 指定：

df.dropna(subset=["human_relevant"])

意思是：只看 human_relevant 这一列，只要这一列不是 NaN 就保留，哪怕其他列有 NaN 也不管。

.notna() 是对一列判断，返回一整列 True/False，你再拿去做 df.loc[mask] 筛选
.dropna() 是直接对整个 DataFrame操作，不需要你自己构造 mask，一步到位删掉含 NaN 的行

所以 df.dropna(subset=["col"]) 其实等价于：
df.loc[df["col"].notna()]
但前者更简洁。

"""

import pandas as pd
import numpy as np

df = pd.DataFrame({
    "post_id": ["p1", "p2", "p3", "p4", "p5"],
    "human_relevant": [True, np.nan, False, True, np.nan],
    "title": ["帖子A", "帖子B", np.nan, "帖子D", "帖子E"]
})

# 用 .dropna()（不带参数）删除任何列有 NaN 的行，赋值给 result1，print 看有几行
# 用 .dropna(subset=["human_relevant"]) 只删除 human_relevant 是 NaN 的行，赋值给 result2，print 看有几行
# 对比 result1 和 result2 的行数差异，说说为什么不一样（提示：p3 那一行发生了什么）

result1 = df.dropna()
print(len(result1))

result2 = df.dropna(subset=["human_relevant"])
print(len(result2))


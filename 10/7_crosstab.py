"""

pd.crosstab 
用来做交叉统计表——统计两列数据组合出现的次数。比如"每个 subreddit 里，每种 risk_level 各有多少条"。

import pandas as pd

df = pd.DataFrame({
    "subreddit": ["depression", "depression", "Anxiety", "Anxiety", "depression"],
    "risk_level": [1, 2, 1, 1, 2]
})

ct = pd.crosstab(df["risk_level"], df["subreddit"])
print(ct)

输出：
subreddit   Anxiety  depression
risk_level
1                 2           1
2                 0           2

行是第一个参数（risk_level），列是第二个参数（subreddit），格子里的数字是"两者组合出现的次数"。

margins=True：加上这个会多一行/一列"合计"：
pd.crosstab(df["risk_level"], df["subreddit"], margins=True)

.reindex()：crosstab 生成的行列顺序是按字母/数字自动排的，不一定是你想要的顺序（比如你想让 risk_level 按 1,2,3 排，subreddit 按项目里固定的顺序排）。
.reindex() 让你手动指定行/列的顺序：

ct = ct.reindex(index=[1, 2, 3], columns=["depression", "Anxiety", "therapy"], fill_value=0)
fill_value=0：如果你指定的某个行/列在原表里根本不存在（比如某个 subreddit 数据里一条都没有），reindex 后会出现 NaN，用 fill_value=0 把这些 NaN 填成 0。
这在 descriptive_stats.py 里的实际用法：

ct = pd.crosstab(coded[col], coded['subreddit'], margins=True)
idx_order = [c for c in order if c in ct.index] + ['All']
col_order = subreddits + ['All']
ct = ct.reindex(index=idx_order, columns=col_order, fill_value=0)

先用 crosstab 算出交叉表，再用 reindex 把行列顺序调整成项目里预先定好的顺序（而不是字母顺序），保证输出表格好读。

"""

import pandas as pd

df = pd.DataFrame({
    "subreddit": ["depression", "Anxiety", "depression", "therapy", "Anxiety", "depression", "therapy"],
    "timeframe": ["Habitual", "Episodic", "Habitual", "NM", "Habitual", "Episodic", "Habitual"]
})
# 不告诉你先跑哪一步，你自己写：

# 生成一个交叉表 ct，行是 timeframe，列是 subreddit
# 不看输出，先猜一下：depression 这一列、Habitual 这一行，格子里应该是几？（自己数一下原始数据里 depression 且 timeframe=Habitual 的有几条）
# 跑代码验证你猜的对不对
# 用 .reindex() 把行顺序改成 ["Habitual", "Episodic", "NM"]，列顺序改成 ["therapy", "Anxiety", "depression"]（故意换个新顺序，不是练习里给的顺序），fill_value=0

ct = pd.crosstab(df["timeframe"], df["subreddit"])
# depression 这一列、Habitual 这一行，格子里应该是2
row_order    = ["Habitual", "Episodic", "NM"]
column_order = ["therapy", "Anxiety", "depression"]
ct           = ct.reindex(index = row_order, columns= column_order, fill_value=0)
print(ct)


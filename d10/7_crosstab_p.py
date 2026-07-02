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
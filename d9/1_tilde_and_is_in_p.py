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
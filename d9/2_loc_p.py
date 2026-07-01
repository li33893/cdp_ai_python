import pandas as pd

df = pd.DataFrame({
    "post_id": ["p1", "p2", "p3", "p4", "p5"],
    "subreddit": ["depression", "therapy", "Anxiety", "mentalhealth", "depression"],
    "risk_level": [1, 3, 1, 2, 3],
    "status": ["", "", "", "", ""]
})

# 用 .loc 只取出 risk_level 为 3 的帖子的 post_id 这一列,print 出来
# 用 .loc 把 risk_level 为 3 的行的 status 列,统一改成 "排除",然后打印整个 df 看看效果
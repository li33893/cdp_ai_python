
import pandas as pd

df = pd.DataFrame({
    "post_id": ["p1", "p2", "p3", "p4", "p5", "p6", "p7"],
    "subreddit": ["depression", "therapy", "depression", "Anxiety", "depression", "therapy", "mentalhealth"],
    "risk_level": [1, 2, 3, 1, 2, 3, 1],
})

# 统计每个 subreddit 出现的次数,print(默认降序)
# 统计每个 risk_level 出现的次数,并按升序(次数少的在前)排列,print
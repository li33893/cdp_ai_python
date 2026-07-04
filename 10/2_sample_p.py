import pandas as pd

df = pd.DataFrame({
    "post_id": [f"p{i}" for i in range(1, 21)],
    "subreddit": ["depression"]*8 + ["Anxiety"]*7 + ["therapy"]*5,
    "score": list(range(20, 0, -1))
})

# 用 random_state=42，从 df 里随机抽 6 行，赋值给 sample1
# 再用同样的 random_state=42，从 df 里随机抽 6 行，赋值给 sample2
# 用 .equals() 方法比较 sample1 和 sample2 是否完全一样（print(sample1.equals(sample2))），验证 random_state 的作用
# 再用 frac=0.2 抽一次（不设 random_state），赋值给 sample3，print 出来看有几行
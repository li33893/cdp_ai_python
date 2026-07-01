import pandas as pd

group_a = pd.DataFrame({
    "post_id": ["p1", "p2", "p3"],
    "subreddit": ["depression", "depression", "depression"],
    "score": [5, 8, 3]
})

group_b = pd.DataFrame({
    "post_id": ["p4", "p5"],
    "subreddit": ["Anxiety", "Anxiety"],
    "score": [10, 2]
})

group_c = pd.DataFrame({
    "post_id": ["p6", "p7", "p8"],
    "subreddit": ["therapy", "therapy", "therapy"],
    "score": [7, 1, 9]
})

# 把 group_a、group_b、group_c 用列表装起来，通过 pd.concat 合并成一个 DataFrame，赋值给 all_posts
# 合并后 index 要重置（用 .reset_index(drop=True)）
# print all_posts，观察 index 是不是变成了连续的 0,1,2,3...7

# 题目1（偏 d9，混合 d10）
import pandas as pd
import numpy as np

df = pd.DataFrame({
    "post_id": [f"p{i}" for i in range(1, 9)],
    "subreddit": ["depression", "Anxiety", "depression", "therapy", 
                  "Anxiety", "depression", "therapy", "Anxiety"],
    "llm_relevant": [True, False, True, True, True, np.nan, False, True],
    "risk_level": [1, 1, 3, 2, 1, 1, 2, 1],
})

# 用 .dropna(subset=[...]) 去掉 llm_relevant 是空值的行，赋值给 valid_df
# 从 valid_df 里筛出 llm_relevant == True 且 risk_level != 3 的帖子，赋值给 usable_df，.reset_index(drop=True)
# 用 .value_counts() 找出 usable_df 里出现次数最多的 subreddit 是哪个、几次
valid_df         = df.dropna(subset="llm_relevant")
high_risk        = ~(df["risk_level"] == 3)
usable_df        = valid_df[(valid_df["llm_relevant"] == True) & high_risk].reset_index(drop=True)
usable_max_sub   = usable_df["subreddit"].value_counts().index[0]
usable_max_count = usable_df["subreddit"].value_counts().iloc[0]
print(f"出现最多的社区：{usable_max_sub}\n次数：{usable_max_count}")


# 题目2（偏 d10 merge/concat）
llm_batch1 = pd.DataFrame({
    "post_id": ["p1", "p2", "p3"],
    "llm_excluded": [False, True, False],
    "llm_source": ["Primary", None, "NM"]
})

llm_batch2 = pd.DataFrame({
    "post_id": ["p4", "p5"],
    "llm_excluded": [False, False],
    "llm_source": ["Solo", "Parallel"]
})

human_labels = pd.DataFrame({
    "post_id": ["p1", "p3", "p4"],
    "human_source": ["Primary", "NM", "Exploration"]
})

# 用 pd.concat 把 llm_batch1 和 llm_batch2 合并成 all_llm（重置 index）
# 用 .merge()，how="inner"，按 post_id 把 all_llm 和 human_labels 合并成 compared（想一下为什么这里用 inner 不用 left）
# 计算 compared 里 llm_source 和 human_source 完全一致的比例，print 出来
all_llm  = pd.concat([llm_batch1, llm_batch2]).reset_index(drop=True)
compared = all_llm.merge(human_labels, on="post_id", how="inner")
all      =len(compared)
same     = len(compared[compared["human_source"] == compared["llm_source"]])
frac     = same/all
print(f"人机一致率：{frac}")


# 题目3（综合 d9+d10，字典 + crosstab）
posts_by_sub = {
    "depression": pd.DataFrame({
        "post_id": ["a1", "a2", "a3"],
        "risk_level": [1, 3, 1]
    }),
    "Anxiety": pd.DataFrame({
        "post_id": ["b1", "b2"],
        "risk_level": [2, 1]
    }),
    "therapy": pd.DataFrame({
        "post_id": ["c1", "c2", "c3"],
        "risk_level": [1, 1, 3]
    })
}

# 用 .items()（配合 for 循环，或者 .values() 也行）把字典里所有 DataFrame 取出来放进一个列表，用 pd.concat 合成 all_posts，重置 index。合并前要先给每个 DataFrame 加一列 subreddit（记录来自哪个 key），用 .copy()（d6学的，避免改到原表）
# 用 pd.crosstab，行是 risk_level，列是 subreddit，margins=True
# 用 .rename() 把 all_posts 里的 risk_level 列改名成 llm_risk_level
container = []

for sub_name, sub_df in posts_by_sub.items():
    sub_df_copy = sub_df.copy()
    sub_df_copy["subreddit"] = sub_name
    container.append(sub_df_copy)

all_posts = pd.concat(container).reset_index(drop=True)

ct        = pd.crosstab(all_posts["risk_level"], all_posts["subreddit"], margins=True)
all_posts = all_posts.rename(columns={"risk_level":"llm_risk_level"})


print(ct) 
print(all_posts)




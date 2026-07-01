"""

01_value_counts()

作用:统计一列里每个值出现了多少次,自动按次数从多到少排序。
df["subreddit"].value_counts()

假设 subreddit 列是:
depression, therapy, depression, Anxiety, depression, therapy

结果:
depression    3
therapy       2
Anxiety       1
Name: subreddit, dtype: int64


02_.sort_values()

作用:给 Series 或 DataFrame 按某种规则排序。
对一个普通 Series 排序(比如一列数字):

s = pd.Series([3, 1, 4, 1, 5])
s.sort_values()             # 默认升序:1, 1, 3, 4, 5
s.sort_values(ascending=False)   # 降序:5, 4, 3, 1, 1

对 DataFrame 排序,要指定按哪一列排:
df.sort_values("risk_level")                      # 按 risk_level 升序
df.sort_values("risk_level", ascending=False)      # 降序

.value_counts() 本身返回的结果已经是一个 Series(索引是类别名,值是次数),默认已经按次数降序排好了。如果想改成升序,直接在后面链式调用 .sort_values():

df["risk_level"].value_counts().sort_values(ascending=True)

ascending 这个参数你应该在别处见过(比如 sorted(key=) 之类),True 是从小到大,False 是从大到小。


"""

import pandas as pd

df = pd.DataFrame({
    "post_id": ["p1", "p2", "p3", "p4", "p5", "p6", "p7"],
    "subreddit": ["depression", "therapy", "depression", "Anxiety", "depression", "therapy", "mentalhealth"],
    "risk_level": [1, 2, 3, 1, 2, 3, 1],
})

# 统计每个 subreddit 出现的次数,print(默认降序)

print(df["subreddit"].value_counts().sort_values(ascending=False))

# 统计每个 risk_level 出现的次数,并按升序(次数少的在前)排列,print

print(df["risk_level"].value_counts().sort_values(ascending=True))
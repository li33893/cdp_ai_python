"""

.sample() 

用来从 DataFrame 里随机抽取一部分行。常见用途：抽样做人工核查、分层抽样、随机打乱数据。


三个常用参数：
df.sample(n=5)                        # 随机抽5行
df.sample(frac=0.3)                   # 随机抽30%的行
df.sample(n=5, random_state=42)       # 固定随机种子，结果可复现

为什么要 random_state？
不设置的话，每次跑代码抽到的行都不一样——对研究来说这是个大问题，因为你没法复现结果、没法让别人验证你的抽样。
设置了 random_state=42（这个数字可以是任何整数，42只是约定俗成的习惯用法），只要种子一样，每次抽到的行就完全一样。

你在项目里见过很多次 random_state=42（generate_sample、data_cleaning.py、spot_check_sample.py），现在你知道这是为了让抽样可复现。
n= 和 frac= 不能同时用，二选一：

n= 是抽固定数量的行
frac= 是抽固定比例的行

"""


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

sample1 = df.sample(n=6, random_state=42)
sample2 = df.sample(n=6, random_state=42)
print(sample1.equals(sample2))

sample3 = df.sample(frac=0.2)
print(len(sample3))
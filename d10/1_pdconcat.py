"""

pd.concat


pd.concat 用来把多个 DataFrame 上下拼接（或左右拼接）成一个。
最常见场景：你分批处理数据（比如按 subreddit 分组抽样），最后要把各组结果合并回一个大表。
import pandas as pd

df1 = pd.DataFrame({"name": ["Alice", "Bob"], "score": [10, 20]})
df2 = pd.DataFrame({"name": ["Carol", "Dave"], "score": [30, 40]})

combined = pd.concat([df1, df2])
print(combined)


输出：
    name  score
0  Alice     10
1    Bob     20
0  Carol     30
1   Dave     40

注意看 index：拼接后 index 是保留原来各自的，会重复（0,1,0,1）。这在实际使用中通常是个问题——你后面遍历或用 index 定位时会出错。
所以几乎总是要配合 .reset_index(drop=True)：

combined = pd.concat([df1, df2]).reset_index(drop=True)

"""

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

all_post = pd.concat([group_a, group_b, group_c]).reset_index(drop=True)
print(all_post)

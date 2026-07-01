"""

.drop_duplicates(subset=, keep=) 和 .reset_index(drop=True)

01_.drop_duplicates()

作用:删除重复的行。
df.drop_duplicates()

默认要求所有列的值都一样才算重复。但通常你只关心某一列或几列是否重复,这时候用 subset 指定:
df.drop_duplicates(subset=["post_id"])

只要 post_id 这一列的值重复,就判定为重复行(哪怕其他列不一样)。

keep 参数决定重复的时候留哪一条:
df.drop_duplicates(subset=["post_id"], keep="first")   # 保留第一条出现的
df.drop_duplicates(subset=["post_id"], keep="last")    # 保留最后一条出现的
df.drop_duplicates(subset=["post_id"], keep=False)     # 重复的全部删掉,一条都不留


02_.reset_index(drop=True)
删除或筛选行之后,DataFrame 的索引(最左边那一列行号)会留下"洞",比如剩下的行索引是 0, 2, 4,不连续了。
df.reset_index(drop=True)
把索引重新从 0 开始连续编号。drop=True 表示"扔掉旧索引,不要把它变成新的一列"(如果不写 drop=True,旧索引会被保留成普通列,通常这不是你想要的)。

"""

import pandas as pd

df = pd.DataFrame({
    "post_id": ["p1", "p1", "p2", "p3", "p3", "p4"],
    "body": ["text a", "text a copy", "text b", "text c", "text c", "text d"],
    "word_count": [50, 80, 60, 40, 90, 70],
})

# 按 word_count 降序排序
desc = df.sort_values("word_count", ascending=False)
# 对 post_id 去重,保留第一条(也就是排序后字数最大的那条)
max = desc.drop_duplicates(subset=["post_id"], keep="first")
# 重置索引(不保留旧索引)
reset = max.reset_index(drop=True)
# print 最终结果,观察一下:p1 和 p3 各自保留下来的是不是字数更大的那条?
print(max)
print(reset)
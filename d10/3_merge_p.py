"""

.merge() 

用来把两个 DataFrame 按某一列的值对应关系横向拼接起来。和 pd.concat（上下堆叠）不同，.merge() 是根据某一列的值去"配对"两张表的行，类似 Excel 的 VLOOKUP，或者数据库的 JOIN。

import pandas as pd

posts = pd.DataFrame({
    "post_id": ["p1", "p2", "p3"],
    "title": ["帖子A", "帖子B", "帖子C"]
})

human_labels = pd.DataFrame({
    "post_id": ["p1", "p2", "p3"],
    "human_relevant": [True, False, True]
})

merged = posts.merge(human_labels, on="post_id")

print(merged)

输出：
  post_id title  human_relevant
0      p1  帖子A            True
1      p2  帖子B           False
2      p3  帖子C            True

on="post_id" 告诉 pandas：以 post_id 这一列为准，把两张表对应行拼在一起。
how= 参数：如果两张表的 post_id 不完全一样怎么办？how= 决定保留哪些行：

how="inner"（默认）：只保留两边都有的 post_id
how="left"：以左边表为准，左边有的都保留，右边没匹配上的填 NaN
how="right"：以右边表为准
how="outer"：两边所有 post_id 都保留，没匹配上的填 NaN

merged = human_df.merge(llm_df, on="post_id")
把人工判断和 LLM 判断按 post_id 拼在一起，才能逐行比较两边的判断是否一致。

"""

import pandas as pd

llm_results = pd.DataFrame({
    "post_id": ["p1", "p2", "p3", "p4"],
    "llm_relevant": [True, False, True, True]
})

human_results = pd.DataFrame({
    "post_id": ["p1", "p2", "p3"],
    "human_relevant": [True, True, False]
})
# 注意：human_results 只有3条，llm_results 有4条（p4 人工没标注）。

# 用 how="inner" 合并两张表，赋值给 merged_inner，print 出来，观察有几行
# 用 how="left"（以 llm_results 为准）合并，赋值给 merged_left，print 出来，观察 p4 那一行 human_relevant 是什么值
# 说说你觉得项目里 agreement_check.py 为什么用默认的 inner（不是 left 或 outer）？（提示：结合它的用途——只想比较双方都判断过的帖子）

merged_inner = llm_results.merge(human_results, on="post_id", how="inner")
print(merged_inner)

merged_left = llm_results.merge(human_results, on="post_id", how="left")
print(merged_left)

# 因为inner会排除掉双方都是空的情况
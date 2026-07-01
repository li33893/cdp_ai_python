"""

.rename() 

用来修改列名（也能改行的 index，但最常用的是改列名）。

import pandas as pd

df = pd.DataFrame({
    "id": ["p1", "p2"],
    "rel": [True, False]
})

renamed = df.rename(columns={"id": "post_id", "rel": "is_relevant"})
print(renamed)

输出：
  post_id  is_relevant
0      p1         True
1      p2        False

columns= 接收一个字典：{旧名: 新名}，可以一次改多个。

为什么需要这个？ 最常见场景是：两张表有同名列，merge 的时候会冲突（pandas 会自动加后缀 _x/_y），所以合并前先改名区分开。或者：LLM 输出的列名和你项目里约定的列名不一样，需要统一。
你在 rickwood_coding.py 里见过这种模式（虽然写法不同，是用字典）：

这里把 LLM 原始输出的列名（excluded）都加上 llm_ 前缀，避免跟后面人工编码的同名列（excluded）搞混。
注意：.rename() 默认不会修改原 DataFrame，而是返回一个新的（除非你加 inplace=True，但项目里几乎不用这个参数，都是用赋值的方式，跟你学过的 .copy() 类似的思路——不直接改原数据）。

"""

import pandas as pd

llm_output = pd.DataFrame({
    "post_id": ["p1", "p2", "p3"],
    "excluded": [False, True, False],
    "reasoning": ["理由A", "理由B", "理由C"]
})

# 用 .rename() 把 excluded 改名为 llm_excluded，把 reasoning 改名为 llm_reasoning，赋值给 renamed_df
# print renamed_df 和原始的 llm_output，确认原始的 llm_output 列名没有被改变（验证 .rename() 不改原表）

renamed_df = llm_output.rename(columns={"reasoning":"llm_reasoning", "excluded": "llm_excluded"})
print(llm_output)
print(renamed_df)

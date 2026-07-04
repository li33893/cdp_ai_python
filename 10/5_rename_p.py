import pandas as pd

llm_output = pd.DataFrame({
    "post_id": ["p1", "p2", "p3"],
    "excluded": [False, True, False],
    "reasoning": ["理由A", "理由B", "理由C"]
})

# 用 .rename() 把 excluded 改名为 llm_excluded，把 reasoning 改名为 llm_reasoning，赋值给 renamed_df
# print renamed_df 和原始的 llm_output，确认原始的 llm_output 列名没有被改变（验证 .rename() 不改原表）
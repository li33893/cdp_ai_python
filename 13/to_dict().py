"""

pandas.DataFrame 有：

df.to_dict()

但重点是：要看你想转成什么结构。orient 不同，结果差很多。

假设：

import pandas as pd

df = pd.DataFrame({
    "name": ["A", "B"],
    "score": [90, 80]
})
默认：orient="dict"
df.to_dict()

结果：

{
    "name": {0: "A", 1: "B"},
    "score": {0: 90, 1: 80}
}

也就是：

列名 → {行索引 → 值}
最常用：orient="records"
df.to_dict(orient="records")

结果：

[
    {"name": "A", "score": 90},
    {"name": "B", "score": 80}
]

也就是每一行变成一个字典。要逐行发送给 API、LLM 或写 JSON 时，通常用这个。

其他常见形式
df.to_dict(orient="list")
{
    "name": ["A", "B"],
    "score": [90, 80]
}
df.to_dict(orient="index")
{
    0: {"name": "A", "score": 90},
    1: {"name": "B", "score": 80}
}

所以，能直接用在 DataFrame 上，但不是写 todict，而是：

df.to_dict()

中间有下划线。你大概率需要的是：

records = df.to_dict(orient="records")

"""
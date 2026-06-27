# 把boolean_indexing.py加强题的筛选结果加上 .copy()，然后给结果加一列 label，每行都是字符串 "selected"，打印最终结果

import pandas as pd

data = {
    "product": ["apple", "banana", "kiwi", "strawberry", "fig"],
    "price": [1.5, 0.8, 3.2, 2.1, 4.0],
    "in_stock": [True, False, True, True, False]
}
df = pd.DataFrame(data)
# 筛出：有货（in_stock 为 True）、价格低于 3.0、且名字长度超过 4 个字母的行，打印结果。


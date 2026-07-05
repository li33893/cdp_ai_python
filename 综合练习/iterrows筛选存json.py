
## 提示：先运行一下d7，导出sample.csv

# 用 sample.csv 做数据来源，完成下面的任务：

# 用 pd.read_csv 读入文件
# 用 iterrows 逐行遍历，跳过 score 低于 60 的行
# 对剩下的行，把名字和分数存进一个列表，每个元素是字典，格式：{"name": "Alice", "score": 82}
# 用 json.dump 把这个列表保存到 day7_result.json

# 结果 print 出来确认一下，格式随意。

import pandas as pd
import json

df = pd.read_csv("sample.csv")

data_filtered = []

for i, row in df.iterrows():
    if row["score"]<60:
        continue
    data_filtered.append({"name":row["name"], "score":row["score"]})



with open("day_7result.json", "w", encoding="utf-8-sig") as f:
    json.dump(data_filtered, f)

print(data_filtered)


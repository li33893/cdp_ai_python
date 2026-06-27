# data = '{"score": 0.8}'
# 用try/except：

# try里：用json.loads()解析data，打印score
# except里：打印f"解析失败：{e}"

import json

data = '{"score": 0.8}'

try:
    data_dic = json.loads(data)
    print(data_dic["score"])
except Exception as e:
    print(f"解析失败：{e}")

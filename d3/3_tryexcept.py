"""

    try里的代码如果任何一行出错，就直接跳到except，不会崩掉整个程序。
    as e是把错误信息存进变量e，可以打印出来看是什么错。


    细分 → 可以针对不同错误做不同处理（比如422缩小时间窗口重试）
    Exception → 懒人写法，所有错误一起处理，代码简单但没法针对性处理

"""

# data = '{"score": 0.8}'
# 用try/except：

# try里：用json.loads()解析data，打印score
# except里：打印f"解析失败：{e}"

import json

data = "not valid json"

try:
    data_j = json.loads(data)
    print(data_j["score"])
except Exception as e:
    print(f"解析失败：{e}")

# 合法的JSON必须符合特定格式：
# {"key": "value"}   ← 合法
# "not valid json"   ← 不合法，没有key:value结构
# json.loads()看到"not valid json"，不知道怎么解析，就报错了。
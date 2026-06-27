"""

import — 三种写法
第一种：导入整个库
import requests

requests.get("https://example.com")  # 用的时候要加库名
第二种：导入并取别名
import pandas as pd

pd.DataFrame()  # 用别名代替，省得每次写pandas
第三种：只导入库里的某一个东西
from datetime import datetime

datetime(2023, 1, 1)  # 直接用，不用加库名

三种写法没有对错，只是习惯和方便程度不同。pandas 因为名字长，大家都用 as pd。

"""

#  1. 理解题： 下面三行哪里有问题？
import json
# result = dumps({"name": "Alice"})

# from datetime import datetime
# result = datetime.datetime(2023, 1, 1)
# 第二行： json.dumps(...)

#  2. 操作题： 不需要写文件，直接回答：如果我想用 re.compile()，下面哪种 import 是对的？
# A
# import re
# re.compile(r"\d+")

# # B
# from re import compile
# compile(r"\d+")

# # C
# import re as r
# r.compile(r"\d+")

# 操作题：A、B、C 其实都对，三种写法都能跑。B 最简洁，A 最常见。

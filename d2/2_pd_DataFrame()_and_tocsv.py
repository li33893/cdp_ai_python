"""

    pd.DataFrame() 就是把数据变成一张表。

    你在 collect.py 里采到的每一条帖子，都是一个字典，长这样：
    {
        "post_id": "abc123",
        "subreddit": "mentalhealth",
        "title": "I tried ChatGPT for therapy",
    }
    采完所有帖子之后，all_raw 里装了几千个这样的字典。然后：
    pythondf = pd.DataFrame(all_raw)
    这一行就把这个列表变成了一张表，每个字典变成一行，字典的 key 变成列名。

    to_csv():把list变成csv文件




    用 os.path.dirname() 再套一层就能往上走，或者用 .. 拼路径：

    import os

    current_dir = os.path.dirname(os.path.abspath(__file__))

    # 上一级目录
    parent_dir = os.path.dirname(current_dir)

    # 上一级里的某个子文件夹，比如 output/
    output_path = os.path.join(parent_dir, "output", "sentences.csv")

    # 如果那个文件夹不存在，先创建它
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    df.to_csv(output_path, index=False, encoding="utf-8-sig")
    也可以用 .. 直接写，效果一样：


    output_path = os.path.join(current_dir, "..", "output", "sentences.csv")

"""


#  1. 下面这段代码会创建一个几行几列的表？列名是什么？

import pandas as pd
import requests

# data = [
#     {"text": "I tried ChatGPT", "kw_pass": True},
#     {"text": "Feeling anxious",  "kw_pass": False},
#     {"text": "GPT helped me",    "kw_pass": True},
# ]

# df = pd.DataFrame(data)

# 三行。列名是各自的key

#  2. 第一天你用 requests.get() 拿数据，今天把数据存成表。

# 请求这个 url 三次，每次换一个不同的 text 参数，把三次返回的 args.text 值收集起来，用 pd.DataFrame() 存成一张表，列名叫 sentence，打印出来。
# https://httpbin.org/get?text=I+use+AI+tools
# https://httpbin.org/get?text=Feeling+anxious+today
# https://httpbin.org/get?text=ChatGPT+helped+me

all_data = []

https = [
    "https://httpbin.org/get?text=I+use+AI+tools",
    "https://httpbin.org/get?text=Feeling+anxious+today",
    "https://httpbin.org/get?text=ChatGPT+helped+me"
]   

for http in https:
    single_data = requests.get(http).json()
    text = single_data["args"]["text"]

    all_data.append({"sentence":text})

all_data_frame = pd.DataFrame(all_data)

print(all_data_frame)

#  3. 把刚才那个三行的 DataFrame 保存成 sentences.csv，不要行号，编码用 utf-8-sig，然后去文件夹里找到它打开看看。

all_data_frame.to_csv("sentences.csv",index=False,encoding="utf-8-sig")


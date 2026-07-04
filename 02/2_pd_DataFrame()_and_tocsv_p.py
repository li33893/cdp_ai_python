#  1. 下面这段代码会创建一个几行几列的表？列名是什么？

import pandas as pd
import requests
import os


data = [
    {"text": "I tried ChatGPT", "kw_pass": True},
    {"text": "Feeling anxious",  "kw_pass": False},
    {"text": "GPT helped me",    "kw_pass": True},
]





#  2. 第一天你用 requests.get() 拿数据，今天把数据存成表。

# 请求这个 url 三次，每次换一个不同的 text 参数，把三次返回的 args.text 值收集起来，用 pd.DataFrame() 存成一张表，列名叫 sentence，打印出来。
# https://httpbin.org/get?text=I+use+AI+tools
# https://httpbin.org/get?text=Feeling+anxious+today
# https://httpbin.org/get?text=ChatGPT+helped+me

https = [
    "https://httpbin.org/get?text=I+use+AI+tools",
    "https://httpbin.org/get?text=Feeling+anxious+today",
    "https://httpbin.org/get?text=ChatGPT+helped+me"
]

all_data = []

for a_https in https:
    single_data = requests.get(a_https).json()
    body        = single_data["args"]["text"]
    all_data.append({"body":body})

#  3. 把刚才那个三行的 DataFrame 保存成 sentences.csv，不要行号，编码用 utf-8-sig，然后去文件夹里找到它打开看看。
df = pd.DataFrame(all_data)

current_dir = os.path.dirname("__file__")
path        = os.path.join(current_dir,"sentence.csv")

df.to_csv(path, index=False, encoding="utf-8")
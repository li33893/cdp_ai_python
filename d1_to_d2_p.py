# 题目1
# 请求这三个 url，如果请求失败用 try/except 捕获错误并打印，成功的话把返回的 args.text 存进列表，最后用 pd.DataFrame() 打印出来，列名叫 sentence。
# https://httpbin.org/get?text=I+use+AI+tools
# https://httpbin.org/get?text=Feeling+anxious+today
# https://httpbin.org/get?text=ChatGPT+helped+me

import requests
import pandas as pd
import time
import re
import os

url = [
    "https://httpbin.org/get?text=I+use+AI+tools",
    "https://httpbin.org/get?text=Feeling+anxious+today",
    "https://httpbin.org/get?text=ChatGPT+helped+me"
]

all_data = []

for a_url in url:
    try:
        resp    = requests.get(a_url)
        resp.raise_for_status()
        data    = resp.json()
        body    = data["args"]["text"]
        pattern = re.compile(r"\bAI\b", re.IGNORECASE)
        if bool(pattern.search(body)):
            all_data.append({"sentence":body})
        time.sleep(1)
    except requests.exceptions.HTTPError as e:
        print(f"请求失败：{e}")

body_df     = pd.DataFrame(all_data)
current_dir = os.path.dirname("__file__")
path        = os.path.join(current_dir, "d2", "filtered.csv")

body_df.to_csv(path, index=False, encoding="utf-8")

# 题目2
# 请求这三个 url，每次请求之间 time.sleep(1)，用 re.compile() 过滤，只保留包含独立单词 "AI" 的句子，存成 filtered.csv，不要行号。
# https://httpbin.org/get?text=I+use+AI+tools
# https://httpbin.org/get?text=Feeling+anxious+today
# https://httpbin.org/get?text=AI+helped+me




# 题目3
# 请求这个 url，用 raise_for_status() 检查是否成功，把返回的整个 args 字典存成 args.json，缩进2个空格，中文正常显示。
# https://httpbin.org/get?text=ChatGPT+and+AI+tools
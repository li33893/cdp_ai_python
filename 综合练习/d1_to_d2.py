"""

trial 1：data = requests.get(url).json()在try的外面
         把.json()落下或者是写错（少写了“（）”）

"""

# 题目1
# 请求这三个 url，如果请求失败用 try/except 捕获错误并打印，成功的话把返回的 args.text 存进列表，最后用 pd.DataFrame() 打印出来，列名叫 sentence。
# https://httpbin.org/get?text=I+use+AI+tools
# https://httpbin.org/get?text=Feeling+anxious+today
# https://httpbin.org/get?text=ChatGPT+helped+me

import requests
import pandas as pd
import time
import re
import json

all_data = []

https = [
    "https://httpbin.org/get?text=I+use+AI+tools",
    "https://httpbin.org/get?text=Feeling+anxious+today",
    "https://httpbin.org/get?text=ChatGPT+helped+me"
]

# for url in https:
#     try: 
#         data = requests.get(url).json()
#         text = data["args"]["text"]
#         all_data.append({"sentence":text})
#     except Exception as e:
#         print(f"{url}请求失败，失败代号{requests.status_codes}")

# all_data_frame = pd.DataFrame(all_data)

# all_data_frame.to_csv("sentence.csv",index=False,encoding="utf-8-sig")


# 题目2
# 请求这三个 url，每次请求之间 time.sleep(1)，用 re.compile() 过滤，只保留包含独立单词 "AI" 的句子，存成 filtered.csv，不要行号。
# https://httpbin.org/get?text=I+use+AI+tools
# https://httpbin.org/get?text=Feeling+anxious+today
# https://httpbin.org/get?text=AI+helped+me

# pattern = re.compile(r"\bAI\b", re.IGNORECASE)

# for url in https:
#     data = requests.get(url).json()
#     time.sleep(1)
#     text = data["args"]["text"]
#     if pattern.search(text):
#         all_data.append({"sentence":text})

# all_data_frame = pd.DataFrame(all_data)

# all_data_frame.to_csv("filtered.csv", index=False, encoding="utf-8-sig")


# 题目3
# 请求这个 url，用 raise_for_status() 检查是否成功，把返回的整个 args 字典存成 args.json，缩进2个空格，中文正常显示。
# https://httpbin.org/get?text=ChatGPT+and+AI+tools

resp = requests.get("https://httpbin.org/get?text=ChatGPT+and+AI+tools")

data = resp.json()

print(resp.raise_for_status())

with open("args.json", "w", encoding="utf-8") as args:
    json.dump(data["args"],args,ensure_ascii=False,indent=2)
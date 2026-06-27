#  1. 下面两段代码，哪个更适合用在要处理一万条帖子的脚本里，为什么？
# 版本A
# for text in posts:
#     re.search(r"\bai\b", text, re.IGNORECASE)

# # 版本B
# pattern = re.compile(r"\bai\b", re.IGNORECASE)
# for text in posts:
#     pattern.search(text)




#  2. 第一天你用 requests.get() 拿到了 JSON 数据，今天加上正则。

# 写一个脚本，请求这个 url：
# https://httpbin.org/get?text=I+use+AI+tools+every+day
# 把返回的 JSON 里 args 字段的 text 值取出来，用 re.compile() 判断它有没有包含独立的单词 "AI"，打印 True 或 False。

import requests
import re

resp    = requests.get("https://httpbin.org/get?text=I+use+AI+tools+every+day")
data    = resp.json()
body    = data["args"]["text"]
pattern = re.compile(r"\bAI\b", re.IGNORECASE)
flg     = bool(pattern.search(body))
print(flg)




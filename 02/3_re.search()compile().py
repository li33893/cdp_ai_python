"""

    Regular Expression 正则表达式

    是一种描述文本模式的语法，用来在字符串里找你想要的内容。
    re 是 Python 内置的正则库，不用安装。

    1. re.search()
    正则表达式是用来找文字模式的。

    2. re.compile()
    Python 读到 r"\bai\b" 这串字符的时候，它不是直接就懂的。它要先花一点时间"翻译"一下，搞清楚你在说什么模式。
    如果你有一万条帖子，keyword_filter() 被调用一万次，Python 就要翻译一万次同一个东西。
    re.compile() 就是说：你先翻译一次，翻译完存起来，后面直接用翻译好的结果，不用再翻译了。

"""

import re
import requests

# r"\bAI\b" 是你要找的模式，\b 的意思是单词边界，也就是前后不能是字母
# text 是你要搜索的字符串
# re.IGNORECASE 是说不区分大小写

text = "I use AI every day"
# result = re.search(r"\bAI\b", text, re.IGNORECASE)

pattern = re.compile(r"\bAI\b", re.IGNORECASE)



#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————

#  练习

#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————

#  1. 下面两段代码，哪个更适合用在要处理一万条帖子的脚本里，为什么？
# 版本A
# for text in posts:
#     re.search(r"\bai\b", text, re.IGNORECASE)

# # 版本B
# pattern = re.compile(r"\bai\b", re.IGNORECASE)
# for text in posts:
#     pattern.search(text)

# b.因为1再每search一遍的之前都要compile一遍，b会直接保存compile的pattern，每次循环的时候只search就好





#  2. 第一天你用 requests.get() 拿到了 JSON 数据，今天加上正则。

# 写一个脚本，请求这个 url：
# https://httpbin.org/get?text=I+use+AI+tools+every+day
# 把返回的 JSON 里 args 字段的 text 值取出来，用 re.compile() 判断它有没有包含独立的单词 "AI"，打印 True 或 False。


resp = requests.get("https://httpbin.org/get?text=I+use+AI+tools+every+day")

data = resp.json()

text = data["args"]["text"]

pattern = re.compile(r"\bai\b", re.IGNORECASE)

if pattern.search(text) is not None:
    print("True")
else:
    print("False")

#或者将if-else改成:
print(bool(pattern.search(text)))
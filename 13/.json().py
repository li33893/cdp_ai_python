# ================================================================
# resp.json()  vs  json.loads()  vs  .replace()
# ================================================================

# resp.json()
# ------------------------------------------------
# - resp 是 requests.post(...) 返回的 Response 对象,不是字符串,也不是 dict
# - .json() 是 requests 库专门给 Response 对象加的方法(语法糖)
# - 作用:把 HTTP 响应体(本质是一段 JSON 字符串)自动解析成 Python dict
# - 相当于帮你省了一步 json.loads(resp.text)
# - 只有 Response 对象才有这个方法,字符串(str)没有 .json(),
#   如果对字符串写 text.json() 会报错:AttributeError: 'str' object has no attribute 'json'
#
# 例子:
# resp = requests.post(BASE_URL, ...)
# data = resp.json()
# # data 现在是 dict,例如 {"content": [{"type": "text", "text": "..."}], "id": "...", ...}
# # 这一层解析的是 Anthropic API 固定的外层结构(协议壳),跟业务内容无关


# json.loads(字符串)
# ------------------------------------------------
# - json 是 Python 标准库模块,需要 import json
# - loads = "load string" 的意思,是一个函数,不是方法
# - 作用:把任意"内容是合法 JSON 的字符串"解析成 Python 对象(dict 或 list)
# - 输入必须是 str 类型,而且内容必须真的是合法 JSON,否则报错 json.JSONDecodeError
#
# 例子:
# text = '{"excluded": false, "confidence": 0.9}'
# print(type(text))          # <class 'str'>  —— 只是字符串,不能 text["excluded"]
#
# result = json.loads(text)
# print(type(result))        # <class 'dict'>
# print(result["excluded"])  # False —— 现在可以正常取值了
#
# 在这个项目里,json.loads() 解析的是"模型自己生成的那段文字"
# (第二层,业务内容,不是 API 协议壳)



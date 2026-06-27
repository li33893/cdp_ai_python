"""

    resp.json() → 用在requests的响应对象上，把HTTP返回的内容转成字典
    json.loads() → 用在普通字符串上，把任意JSON字符串转成字典

"""
import json

text = '{"relevant": true, "confidence": 0.9}'
result = json.loads(text)
print(result["relevant"])  # True

#  用json.loads()把s转成字典，然后分别打印出risk_level和reason
s = '{"risk_level": 2, "relevant": true, "reason": "user describes using ChatGPT for emotional support"}'
# risk_level = json.loads(s)["risk_level"]
# reason = json.loads(s)["reason"]

# print(risk_level)
# print(reason)

#优化：我的调用了两次json.laods，最好的办法是先存成变量，只解析一次
s_json = json.loads(s)
print(s_json["risk_level"])
print(s_json["reason"])
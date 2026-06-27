#  用json.loads()把s转成字典，然后分别打印出risk_level和reason
import json

s = '{"risk_level": 2, "relevant": true, "reason": "user describes using ChatGPT for emotional support"}'

s_dic = json.loads(s)
print(s_dic["risk_level"])
print(s_dic["reason"])
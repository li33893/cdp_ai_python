"""
    params 字典传参
"""


import requests

#写法一：url传参
# requests.get("https://jsonplaceholder.typicode.com/posts?userId=1&_limit=3")

# #写法二：params传参
# requests.get("https//jsonplaceholder.typicode.com/posts", params={"user_id":1, "_limit":3})


#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————

#  练习

#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————


#  1. 用params传参的方式，获取user_id=1的前3条数据（要求：打印拼接好的url）

params = {"userId": 1, "_limit": 3}
resp = requests.get("https://jsonplaceholder.typicode.com/posts", params=params)

print(resp.url)     # 看看requests帮你拼成了什么URL
print(resp.json())  # 返回了几条数据？


#  2. 把 _limit 改成 5，然后只打印每条数据的 title（用 for 循环）
params = {"user_id":1, "_limit":5}
resp = requests.get("https://jsonplaceholder.typicode.com/posts", params=params)
data=resp.json()
for user in data:
    print(user["title"])
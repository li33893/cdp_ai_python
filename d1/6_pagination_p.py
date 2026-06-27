  # 1. 用 while 循环自动翻页，把 jsonplaceholder.typicode.com/posts 的所有数据全部拿到，打印每次拿了几条，最后打印总计几条。每次请求后等0.5秒

# 犯过的错误：
# 1. https://没写
# 2. dumps少写了一个s

import json
import requests
import time

start    = 0
all_data = []

while True:
  params = {"_start":start,"_limit":10}
  resp = requests.get("https://jsonplaceholder.typicode.com/posts", params = params)
  data = resp.json()
  all_data.extend(data)

  print(f"{start}s: 拿到{len(data)}条")

  time.sleep(0.5)

  start += 10

  if len(data)<10:
    break

print(f"总计拿到{len(all_data)}条。")
print(f"所有帖子：{json.dumps(all_data, indent = 2)}")





"""

    Pagination

"""


  # 1. 用 while 循环自动翻页，把 jsonplaceholder.typicode.com/posts 的所有数据全部拿到，打印每次拿了几条，最后打印总计几条。每次请求后等0.5秒
import requests
import time
import json

all_data = []
start = 0

while True:
    params = {"_limit": 10, "_start": start}
    resp = requests.get("https://jsonplaceholder.typicode.com/posts", params=params)
    data = resp.json()
    
    print(f"_start={start}，拿到 {len(data)} 条")
    
    all_data.extend(data)
    start += 10
    time.sleep(0.5)    # 每次请求后等0.5秒
    
    if len(data) == 0 or len(data) < 10:
        break
    


print(f"\n总计拿到：{len(all_data)} 条")
print(json.dumps(all_data, indent=2))


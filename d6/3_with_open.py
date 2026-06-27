"""

with open — 写文件
with open("log.json", "w", encoding="utf-8") as f:
    json.dump(data, f)

"log.json" — 要写的文件名，不存在就创建，存在就覆盖
"w" — 写模式
encoding="utf-8" — 支持中文等非英文字符
as f — 把打开的文件装进变量 f
with 结束时自动关文件
json.dump(data, f) — 把 data 写进 f 这个文件里

"""

# 把下面的字典写进 result.json，然后打开文件确认内容对不对：
import json

data = {"name": "Alice", "score": 95, "passed": True}

with open("result.json", "w", encoding="utf-8") as f:
    json.dump(data, f)
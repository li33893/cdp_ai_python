"""

# 写文件
with open("test.txt", "w", encoding="utf-8") as f:
    f.write("第一行\n")
    f.write("第二行\n")

# 读文件
with open("test.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())

# 追加
with open("test.txt", "a", encoding="utf-8") as f:
    f.write("第三行\n")

JSONL 是每行一个 JSON 对象的格式


import json

# 写 JSONL
records = [{"id": 1, "text": "hello"}, {"id": 2, "text": "world"}]
with open("data.jsonl", "w", encoding="utf-8") as f:
    for record in records:
        f.write(json.dumps(record) + "\n")

# 读 JSONL
with open("data.jsonl", "r", encoding="utf-8") as f:
    for line in f:
        obj = json.loads(line.strip())
        print(obj)

"""

# 把 [{"post_id": "a1", "label": "ES"}, {"post_id": "a2", "label": "CO"}] 写成 JSONL 文件 coding.jsonl
# 再读回来，逐行打印每条记录的 post_id 和 label
import json

result = [{"post_id": "a1", "label": "ES"}, {"post_id": "a2", "label": "CO"}]

with open("coding.jsonl", "w", encoding="utf-8") as f:
    for record in result:
        f.write(json.dumps(record) + "\n")

with open("coding.jsonl", "r", encoding="utf-8") as f:
    for i, line in enumerate(f, start=1):
        post = json.loads(line.strip())
        print(f"{i},{post['post_id']} {post['label']}")
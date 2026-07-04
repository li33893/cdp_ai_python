import pandas as pd
import os
import re
import json


# 题目一
# 新建一个 posts.csv，内容：
# post_id,subreddit,text,score
# p1,mentalhealth,I use AI every day,42
# p2,depression,feeling sad today,8
# p3,Anxiety,ChatGPT helps me cope,15
# p4,therapy,not related,5
# 用 pd.read_csv 读入，用 df.iterrows 遍历，用 continue 跳过 text 里不含 "ai"（.lower()）的行，对剩下的行用三元表达式判断 
# score 大于 10 打印 "high" 否则 "low"，格式：p1: high

posts = {"post_id":["p1","p2","p3","p4"],
         "subreddit":["mentalhealth","depression","Anxiety","therapy"],
         "text":["I use AI every day","feeling sad today","ChatGPT helps me cope","not related"],
         "score":[42,8,15,5]}

current_dir = os.path.dirname(__file__)
path        = os.path.join(current_dir,"d7","posts.csv")

post_pd = pd.DataFrame(posts)
post_pd.to_csv(path, index=False, encoding="utf-8")

pattern = re.compile(r"\bAI\b", re.IGNORECASE)

read_csv = pd.read_csv(path)
print(read_csv)

filtered = []

for i, row in read_csv.iterrows():
    if pattern.search(row["text"]) == None: # 找不到时返回 None
        continue
    msg = "high" if row["score"]>10 else "low" 
    filtered.append({
        "post_id": row["post_id"],
        "text": row["text"],
        "score": int(row["score"])
    })
    print(f"{row['post_id']}: {msg}")


# 题目二
# 定义 records = [{"id": "p1", "label": "ES"}, {"id": "p2", "label": "XX"}, {"id": "p3", "label": "CO"}]，用 enumerate() 从 1 开始遍历，
# 对每条记录用 assert 检查 label 在 ["ES", "CO", "VE", "NM"] 里，
# 用多重 except 捕获 AssertionError 打印 "invalid: XX"，通过则打印 "1. p1 ES"
records = [{"id": "p1", "label": "ES"}, {"id": "p2", "label": "XX"}, {"id": "p3", "label": "CO"}]
for i, record in enumerate(records, start=1):
    try:
        assert record["label"] in ["ES", "CO", "VE", "NM"], "必须为'ES', 'CO', 'VE', 'NM'中的一个"
        print("通过测试")
    except AssertionError:
        print(f"invalid: {record["label"]}")

# 题目三
# 用题目一的 posts.csv，过滤含 "ai" 的行（列表推导式 + .get() fallback），把结果写成 JSONL，再读回来用 enumerate 打印
current_dir = os.path.dirname(__file__)
path        = os.path.join(current_dir, "d7", "results.jsonl")

with open (path, "w", encoding="utf-8") as f:
    for record in filtered:
        f.write(json.dumps(record) + "\n")

with open(path, "r", encoding="utf-8") as f:
    for i, row in enumerate(f, start=1):
        post = json.loads(row)
        print(f"{i}:{row}")
import re
import json
import time
import pandas as pd
import os

posts = [
    {"id": "a1", "subreddit": "mentalhealth", "title": "ChatGPT saved my night", "body": "I was alone and talked to it for hours", "score": None},
    {"id": "b2", "subreddit": "depression", "title": "Feeling lost", "body": "I asked Claude for advice and it actually helped", "score": 42},
    {"id": "c3", "subreddit": "Anxiety", "title": "AI is taking over", "body": "Just read an article about robots", "score": 15},
    {"id": "d4", "subreddit": "therapy", "title": "My therapist vs ChatGPT", "body": None, "score": 8},
    {"id": "e5", "subreddit": "mentalhealth", "title": "Long night", "body": "Used an AI chatbot when I couldn't sleep", "score": 5},
]

# 用列表推导式，筛出 body 不是 None 且包含 "chatgpt"、"claude"、或独立单词 "ai" 的帖子（用 re.search()，不区分大小写），存进 filtered
# 对 filtered 里每条帖子，用 f-string 打印："[subreddit] | [id] | score: [score或0]"，score用 .get() 兜底为 0，每条之间 time.sleep(0.1)
# 用 pd.DataFrame() 把 filtered 转成DataFrame，用 to_csv() 存成 review_output.csv
# 建一个嵌套字典 log，结构是 log[subreddit][id] = {"score": ...}，把 filtered 里每条帖子存进去，最后用 json.dump() 写进 review_log.json
# 整个处理流程用 try/except 包住，出错打印 "error: [错误信息]"

pattern = re.compile(r"\bAI\b|chatgpt|claude", re.IGNORECASE) #不能有多余的空格否则会漏掉chatgpt和claude

all_data = [
    post 
    for post in posts
    if post["body"] is not None and pattern.search(post["body"])
]
try:
    for single_data in all_data:
        print(f"subreddit: {single_data['subreddit']} | id: {single_data['id']} | score: {single_data.get('score', 0)}")

    pd_all_data = pd.DataFrame(all_data)

    current_dir = os.path.dirname(__file__)
    path       = os.path.join(current_dir, "d3", "review_output.csv")

    pd_all_data.to_csv(path, index=False, encoding="utf-8")

    log = {}

    for single_data_2 in all_data:
        sub_name   = single_data_2["subreddit"]
        post_id    = single_data_2["id"]
        post_score = single_data_2.get("score", 0)
        if single_data_2["subreddit"] not in log:
            log[sub_name]          = {}
        # log[sub_name]["id"]    = post_id 多余
        # if log[sub_name][post_id] not in log[sub_name]: 多余，每个id都是唯一的
        # log[sub_name][post_id] = {} 多余
        log[sub_name][post_id] = {"score":post_score} 
            
    json_path = os.path.join(current_dir, "d3", "review_log.json")

    with open (json_path, "w", encoding="utf-8") as open_log:
        json.dump(log, open_log, ensure_ascii=False, indent=2)
except Exception as e:
    print(f"erroe:{e}")








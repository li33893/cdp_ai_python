import re
import json
import time
import pandas as pd

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

try:
    re_kw_pattern = re.compile(r"\bai\b",re.IGNORECASE)
    filtered = [post for post in posts 
                    if post["body"] is not None  # body是None时，"chatgpt" in None会报TypeError而不是返回False，所以必须先挡掉 (0也是e，但是“”就会是false)
                    and ("chatgpt" in post["body"].lower() or 
                        "claude" in post["body"].lower() or 
                        re_kw_pattern.search(post["body"]) is not None
                    )
                ]
    for post in filtered:
        print(f'subreddit: {post["subreddit"]} | "id": {post["id"]} | "score": {post.get("score",0)}')
        time.sleep(0.1)

    data_frame = pd.DataFrame(filtered)

    data_frame.to_csv("review_output.csv", index=False, encoding="utf-8-sig")

    log = {}
    for post in filtered:
        sub = post["subreddit"]
        pid = post["id"]  # 不要用 id 做变量名，它是Python内置函数，会被覆盖掉。
        score = post["score"]

        if sub not in log:
            log[sub] = {}
        
        log[sub][pid] = {"score":score}
            

    with open("review_log.json", "w", encoding="utf-8") as openlog:
        json.dump(log, openlog, ensure_ascii=False, indent=2)
except Exception as e:
    print(f"error: {e}")

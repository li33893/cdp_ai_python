import requests
import pandas as pd
import json
import re
import time

SYSTEM_PROMPT = "You are a research assistant. Given a Reddit post, decide if the user describes a personal experience using an AI tool for emotional support. Respond ONLY with a JSON object, no markdown, no code blocks: {\"relevant\": true or false, \"reason\": \"one sentence\"}"
post_text     = "Is this post relevant to AI mental health?"
API_KEY       = ""

posts = [
    {"id": "001", "title": "ChatGPT saved me", "body": "I was feeling so alone last night and I opened ChatGPT and just started talking. It actually helped me calm down."},
    {"id": "002", "title": "Feeling anxious today", "body": "I don't know why but I can't stop shaking. Everything feels wrong."},
    {"id": "003", "title": "AI tools for therapy", "body": "Has anyone used AI-powered tools for mental health support? I've been using one for a month."},
]

all_data = []
pattern  = re.compile(r"\bAI\b|ai-", re.IGNORECASE)

# 用re.compile()过滤，只保留title+body合并后包含\bai\b或ai-的帖子
# 每篇之间time.sleep(0.5)
# 过滤后的帖子用f-string打印：Post {id}: {title}
# 对每篇过滤后的帖子构造payload，用requests.post()发给Claude API，timeout=60
# 用try/except解析返回的JSON，成功打印relevant和reason，失败打印f"解析失败：{type(e).__name__}：{e}"
# 把所有结果存成DataFrame，列名id、title、relevant、reason，保存成results.csv

for post in posts:
    content = f"{post["title"]}\n{post["body"]}"
    if bool(pattern.search(content)):
        print(f"Post {post["id"]}: {post["title"]}")

        payload       = {
            "model" : "claude-sonnet-4-6",
            "max_tokens" : 100,
            "system" : SYSTEM_PROMPT,
            "messages" : [
                {"role" : "user", "content" : f"{content}\n{post_text}"}
        ]
        }

        resp = requests.post(
            "https://api.anthropic.com/v1/messages",
            headers = {
                "Content-Type": "application/json",
                "x-api-key": API_KEY,
                "anthropic-version": "2023-06-01"
            },
            json    = payload,
            timeout = 60
        )

        try: 
            resp.raise_for_status()
            result = json.loads(resp.json()["content"][0]["text"])
            all_data.append({"id": post["id"], "title": post["title"], "relevant": result["relevant"], "reason": result["reason"]})
            print(f"relevant: {result["relevant"]}\nreason: {result["reason"]}")
        except Exception as e:
            print(f"解析失败：{type(e).__name__}：{e}")
            print(resp.text)

    time.sleep(0.5)

pd.DataFrame(all_data).to_csv("results.csv", index=False, encoding="utf-8-sig")
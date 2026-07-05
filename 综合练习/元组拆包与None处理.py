"""
常犯错误： 总是忽略了None的操作
"""

# 题1：
# records = [("abc123", "mentalhealth"), ("xyz999", "depression"), ("def456", "Anxiety")]
# 元组拆包遍历，打印每条：abc123 来自 r/mentalhealth
records = [("abc123", "mentalhealth"), ("xyz999", "depression"), ("def456", "Anxiety")]
# i = 0
# for element in records:
#     pid, subreddit = records[i]
#     i+=1
#     print(f"{pid}来自r/{subreddit}")

# 优化：
for element in records:
    pid, subreddit = element
    print(f"{pid}来自r/{subreddit}")


# 题2：
texts = ["I talked to ChatGPT today", "Feeling sad", "Claude really helped me", "I don't know"]
# 过滤掉不足5词的，剩下的检查有没有 "chatgpt" 或 "claude"，打印结果。
for text in texts:
    count = len(text.split())
    if count>=5:
        if "chatgpt" in text.lower() or "claude" in text.lower():
            print(text)

# 题3：
posts = [
    ("abc123", "mentalhealth", "  I talked to ChatGPT and it really helped me feel better  "),
    ("xyz999", "depression", None),
    ("def456", "Anxiety", "  Feeling very sad today  "),
    ("ghi789", "therapy", "  Claude helped me process my trauma and anxiety  "),
]
# 元组拆包遍历，跳过 None，转小写去空格，不足6词跳过，把结果存进 DataFrame，列名 post_id、words、has_ai，保存成 results.csv。最后用 f-string 打印含AI比例（:.1%）。
import pandas as pd

data_frame = []
has_ai_count =0
for element in posts:
    pid, subreddit, body = element
    if body is None:
        continue
    body_c = body.lower().strip()
    count = len(body_c.split())
    if count<6:
        continue
    if "chatgpt" in body_c or "claude" in body_c: 
        has_ai = True
        has_ai_count += 1
    else:
        has_ai = False
    data = {}
    data["post_id"] = pid
    data["words"] = count
    data["has_ai"] = has_ai
    data_frame.append(data)
frame = pd.DataFrame(data_frame)
print(frame)
frame.to_csv("result.csv", index=False, encoding="utf-8-sig")
valid_posts_count = len(data_frame)
hit_rate = has_ai_count/valid_posts_count
print(f"AI比例:{hit_rate:.1%}")






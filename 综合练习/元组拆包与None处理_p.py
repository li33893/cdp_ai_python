import re
import pandas as pd
import os

# 题1
# 元组拆包遍历，打印每条：abc123 来自 r/mentalhealth
records = [("abc123", "mentalhealth"), ("xyz999", "depression"), ("def456", "Anxiety")]

for record in records:
    id, subreddit = record
    print(f"{id}来自r/{subreddit}")



# 题2：
texts = ["I talked to ChatGPT today", "Feeling sad", "Claude really helped me", "I don't know"]
# 过滤掉不足5词的，剩下的检查有没有 "chatgpt" 或 "claude"，打印结果。
pattern = re.compile(r"chatgpt|claude", re.IGNORECASE)
filtered = [text for text in texts if len(text.strip().split())>=5 and pattern.search(text)]
print(filtered)

# 题3：
posts = [
    ("abc123", "mentalhealth", "  I talked to ChatGPT and it really helped me feel better  "),
    ("xyz999", "depression", None),
    ("def456", "Anxiety", "  Feeling very sad today  "),
    ("ghi789", "therapy", "  Claude helped me process my trauma and anxiety  "),
]
# 元组拆包遍历，跳过 None，转小写去空格，不足6词跳过，把结果存进 DataFrame，列名 post_id、words、has_ai，保存成 results.csv。最后用 f-string 打印含AI比例（:.1%）。
pattern_ai = re.compile(r"\bAI\b|chatgpt|claude", re.IGNORECASE)
data = []
for post in posts:
    id, sub, content    = post
    if content is None:
        continue
    data_log            = {}
    post_lower          = content.lower().strip()
    words               = len(post_lower.split())
    if words<6:
        continue
    has_ai              = bool(pattern_ai.search(post_lower))
    data_log["post_id"] = id
    data_log["has_ai"]  = has_ai
    data_log["words"]   = words
    data.append(data_log)

current_dir      = os.path.dirname(__file__)
path             = os.path.join(current_dir, "d4", "results.csv")
pd_post_filtered = pd.DataFrame(data)

pd_post_filtered.to_csv(path, index=False, encoding="utf-8")

print(f"含AI比例:{pd_post_filtered['has_ai'].mean():.1%}")
    

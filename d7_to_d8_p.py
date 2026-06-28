# 题目一
# 新建一个 posts.csv，内容：
# post_id,subreddit,text,score
# p1,mentalhealth,I use AI every day,42
# p2,depression,feeling sad today,8
# p3,Anxiety,ChatGPT helps me cope,15
# p4,therapy,not related,5
# 用 pd.read_csv 读入，用 df.iterrows 遍历，用 continue 跳过 text 里不含 "ai"（.lower()）的行，对剩下的行用三元表达式判断 score 大于 10 打印 "high" 否则 "low"，格式：p1: high

# 题目二
# 定义 records = [{"id": "p1", "label": "ES"}, {"id": "p2", "label": "XX"}, {"id": "p3", "label": "CO"}]，用 enumerate() 从 1 开始遍历，对每条记录用 assert 检查 label 在 ["ES", "CO", "VE", "NM"] 里，用多重 except 捕获 AssertionError 打印 "invalid: XX"，通过则打印 "1. p1 ES"

# 题目三
# 用题目一的 posts.csv，过滤含 "ai" 的行（列表推导式 + .get() fallback），把结果写成 JSONL，再读回来用 enumerate 打印，加 __name__ == "__main__" 保护。
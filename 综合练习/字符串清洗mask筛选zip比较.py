# 题目1(基础,偏 d9)
import pandas as pd

df = pd.DataFrame({
    "post_id": ["p1", "p2", "p3", "p4", "p5", "p6"],
    "subreddit": ["  Depression", "THERAPY ", "anxiety", " MentalHealth", "depression", "Therapy"],
    "risk_level": [1, 3, 2, 1, 3, 2],
    "word_count": [45, 120, 80, 45, 60, 200],
})

# 把 subreddit 列统一清洗:去空格 + 转小写,保存回原列
# 构造一个 mask,标记 risk_level == 3 的行
# 用这个 mask,把非高风险(~mask)的帖子取出来,赋值给 safe_df
# 对 safe_df 统计清洗后的 subreddit 出现次数,print

df["subreddit"] = df["subreddit"].str.lower().str.strip()
mask            = df["risk_level"] == 3
safe_df         = df[~mask]

print(safe_df["subreddit"].value_counts())

# 题目2(中等,d8 + d9 混合)
posts = [
    {"post_id": "p1", "score": 15, "body": "I talked to ChatGPT about my anxiety"},
    {"post_id": "p2", "score": 8,  "body": "just a random post"},
    {"post_id": "p3", "score": 30, "body": "Claude helped me process grief"},
    {"post_id": "p4", "score": 22, "body": "AI is interesting but this isn't relevant"},
]

# 用 max(..., key=) 找出 score 最高的帖子,print 它的 post_id
# 用列表推导式 + 三元表达式,给每条帖子打标签:body 字数(用 .split())大于等于6个词的标 "长",否则标 "短",生成一个新列表(每个元素是 (post_id, 标签) 的元组)
# 用 enumerate(start=1) 遍历 posts,print 每条帖子的序号(从1开始)和 post_id

max_score = max(posts, key=lambda x: x["score"])
print(max_score["post_id"])

post_length = []
# for post in posts:
#     post_single_length = {}
#     post_single_length[post["post_id"]] = "long" if len(post["body"].split()) >= 6 else "short"
#     post_length.append(post_single_length)
# print(post_length)

# label = [(post["post_id"], "long" ) for post in posts if len(post["body"].split) >= 6 else (post["post_id"], "short" )]
# 这里 if...else 跟在 for 后面,这是列表推导式的过滤语法——它只能决定"要不要保留这个元素",不能接 else(过滤语法压根没有"否则怎样"的概念,只有"要"或"不要")。你在 if 后面又加了个 else,Python 语法解析器会直接报 SyntaxError。
# 列表推导式最基本的形式:
# [表达式 for 元素 in 可迭代对象]
# 意思是:"对每个元素,算一下表达式,把结果收集成一个新列表"。
# 加了 for 后面的 if,是在原基础上"插了一句话"
# [表达式 for 元素 in 可迭代对象 if 条件]
# 翻译成人话是:"对每个元素,先问一句'这个元素满足条件吗?'——不满足的,直接跳过,压根不进入'算表达式'这一步;满足的,才继续算表达式,放进结果里。"
# 举个例子:
# python[x for x in [1,2,3,4,5] if x > 2]
# 读作:"遍历 1到5,只要 x>2 的,把 x 本身放进结果里;x<=2 的,直接跳过,不出现在结果里。"
# 结果:[3, 4, 5]——注意,结果只有3个元素,不是5个。不满足条件的直接消失了,不会以任何形式出现在结果里。
# 这就是为什么这个 if 后面不需要、也不能有 else——因为它的任务从头到尾只有一件事:筛选,要还是不要。
# 它根本没有"不满足条件的时候该输出什么"这个概念,因为不满足条件就是"不出现",没有"输出个啥"的问题。

post_length = [(post["post_id"], "long") if len(post["body"].split()) >= 6 else (post["post_id"], "short") for post in posts]
print(post_length)

for i, row in enumerate(posts, start=1):
    print(f"{i}: {row["post_id"]}")

# 题目3(较难,综合应用,模拟真实流程)
records = [
    {"post_id": "p1", "human_relevant": "True",  "llm_relevant": "True"},
    {"post_id": "p2", "human_relevant": "False", "llm_relevant": "True"},
    {"post_id": "p3", "human_relevant": "True",  "llm_relevant": "True"},
    {"post_id": "p4", "human_relevant": None,    "llm_relevant": "False"},
    {"post_id": "p5", "human_relevant": "False", "llm_relevant": "False"},
]

df2 = pd.DataFrame(records)

# 用 .notna() 筛选出 human_relevant 不是缺失值的行,赋值给 valid_df(对应真实项目里"排除人工判断缺失的行"这个操作)
# 把 valid_df 里的 human_relevant 和 llm_relevant 两列,分别用 == "True" 的方式转成真正的布尔值(不要用 .astype(bool),你已经知道为什么)
# 用 assert 检查:转换后 human_relevant 列的长度必须等于 llm_relevant 列的长度,否则报错并附带信息
# 用 .tolist() 把两列分别转成 Python list,命名为 human_list 和 llm_list
# 用 zip() 遍历这两个 list(提示:zip 你在 d8 前应该没系统学过,这里只需要用最简单的方式——for h, l in zip(human_list, llm_list): ——配合 set(),统计有多少条 h != l(即人机判断不一致的条数),print 出来

valid_df = df2[df2["human_relevant"].notna()]
print(valid_df)

valid_df["human_relevant"] = valid_df["human_relevant"] == "True"
valid_df["llm_relevant"]   = valid_df["llm_relevant"] == "True"

assert len(valid_df["human_relevant"]) == len(valid_df["llm_relevant"]), "两列长度必须相等"
print("长度对齐检查通过。")

human_list = valid_df["human_relevant"].tolist()
llm_list   = valid_df["llm_relevant"].tolist()
print(human_list)
print(llm_list)

mismatch_count = 0
for h, l in zip(human_list, llm_list):
    if h != l:
        mismatch_count += 1
print(mismatch_count)


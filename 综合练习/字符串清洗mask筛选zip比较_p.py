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
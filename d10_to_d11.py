# 题目1
# 用 argparse 接一个带值参数 --input（默认 "posts_list_screened.csv"），一个开关参数 --dedup，打印这两个值。
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--input", default="posts_list_screened.csv")
parser.add_argument("--dedup", action="store_true")
args   = parser.parse_args()

print(args.input)
print(args.dedup)



# 题目2
# input_path = "data/raw/posts_list_screened.csv"。从这串路径取出不带扩展名的纯文件名，接上 "_cleaned.csv" 拼成 output_name，print 出来。
import os

base_dir   = os.path.basename("data/raw/posts_list_screened.csv")
file_split = os.path.splitext(base_dir)
file_name  = file_split[0]
final_dir  = file_name + "_cleaned.csv"

print(final_dir)


# 题目3
import pandas as pd

llm_a = pd.DataFrame({"post_id": ["p1", "p2", "p3"], "llm_source": ["Primary", "NM", "Solo"]})
llm_b = pd.DataFrame({"post_id": ["p4", "p5"], "llm_source": ["Primary", "Parallel"]})
human = pd.DataFrame({"post_id": ["p1", "p3", "p4", "p5"], "human_source": ["Primary", "NM", "Primary", "Solo"]})
# 把 llm_a、llm_b 上下合并成 all_llm（重置 index）；再和 human 按 post_id 合并，只保留两边都有的，叫 merged；算出 merged 里 llm_source 和 human_source 一致的条数，print。
pd.merge([llm_a, llm_b])



# 题目4
# 已知 done = 300、total = 1200。写计时代码算出经过的秒数 elapsed（开始记时刻、中间 sleep 1 秒、结束记时刻、相减）；用 elapsed 和 done 算每秒处理几条存进 rate，防止除数太小导致出问题；用 rate 和剩余条数算出预计剩余秒数 eta，print。

# 题目5
import pandas as pd

df = pd.DataFrame({
    "post_id":      ["p1", "p2", "p3", "p4", "p5", "p6", "p7", "p8"],
    "subreddit":    ["depression", "Anxiety", "depression", "therapy",
                     "Anxiety", "depression", "therapy", "Anxiety"],
    "llm_excluded": [False, True, False, False, False, True, False, False],
    "llm_source":   ["Primary", None, "NM", "Solo", "Primary", None, "NM", "Primary"],
})

# 只保留 llm_excluded 是 False 的帖子，存进 coded，重置 index
# 找出 coded 里 llm_source 出现次数最多的类别是什么、几次，分别 print
# 交叉表：行 llm_source、列 subreddit、带 margins，print
# 把 coded 的 llm_source 列改名成 source_final，print 改名后的列名
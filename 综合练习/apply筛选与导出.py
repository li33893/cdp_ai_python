# 你有一份学生数据，需要处理并保存结果。
import pandas as pd
import json

students = [
    {"name": "Alice", "score": 82, "comment": "doing well"},
    {"name": "Bob", "score": 45, "comment": None},
    {"name": "Charlie", "score": 91, "comment": "excellent"},
    {"name": "Di", "score": 58, "comment": "[deleted]"},
    {"name": "Eve", "score": 73, "comment": "needs improvement"},
]

# 任务：
# 把 students 转成 DataFrame
# 加一列 name_len，存每个名字的字符数
# 加一列 comment_valid，comment 不是 None 也不是 "[deleted]" 的为 True，否则为 False
# 筛出 score 大于 60、且 comment_valid 为 True 的行，存进 df_filtered，记得加 .copy()
# 检查 df_filtered 是否为空，如果空就打印 "没有符合条件的学生" 然后结束
# 不为空的话，用 f-string 打印："符合条件的学生共 X 名"（X是实际数量）
# 把 df_filtered 存成 result.csv
# 把一个字典 {"total": X, "names": [...]} 写进 result.json，X 是人数，names 是符合条件的名字列表

def len_co (word):
    return len(word)

def comment_valid (comment):
    if comment == "[deleted]" or comment is None:
        return False
    return True

df = pd.DataFrame(students)
# print(data_frame)

# df["name_len"] = df["name"].apply(lambda x: len(x))

df["name_len"] = df["name"].apply(len_co)
# print(df)

df["comment_valid"] = df["comment"].apply(comment_valid)
# print(df)

df_filtered = df[(df["comment_valid"] == True) & (df["score"]>60)].copy()  # & 是专门为列设计的，它会把两列 True/False 逐行对比，两边都是 True 才保留。
                                                                           # df["score"] > 60 & df["comment_valid"] == True
                                                                           # Python 先算 60 & df["comment_valid"]
if df_filtered.empty:
    print("没有学生符合条件")
else:
    print(f"符合条件的学生共{len(df_filtered["name"])}名")
    

df_filtered.to_csv("result.csv", index=False, encoding="utf-8-sig")

result = {}
names = []

result["names"] = df_filtered["name"].tolist()
result["total"] = len(df_filtered)

with open ("result.json", "w", encoding="utf-8") as f:
    json.dump(result, f)
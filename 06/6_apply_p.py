#  1. 理解题： 下面的代码，add_exclamation 会被调用几次？每次传进去的是什么？
# pythondata = {"word": ["hello", "good", "bye", "cool"]}
# df = pd.DataFrame(data)
# df["excited"] = df["word"].apply(add_exclamation)


#  2.  操作题： 新建 day6_01_apply.py，写下面的内容并运行：
import pandas as pd

data = {"name": ["Alice", "Bob", "Charlie"]}
df = pd.DataFrame(data)

# 用 .apply() 加一列 name_len，存每个名字的字符数

def len_count (text):
    return len(text)

df["name_len"] = df["name"].apply(len_count)

print(df)
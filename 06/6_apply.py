"""

.apply() — pandas 里，一列数据就是很多行堆在一起。.apply() 的作用是：把这一列的每一行，一行一行地喂给某个函数，把返回值收集起来变成新的一列

也可以用 lambda，不用单独写函数：
df["excited"] = df["word"].apply(lambda x: x + "!")
lambda x: x + "!" 的意思就是"传进来的值叫 x，返回 x + '!'"。效果完全一样。

"""

def add_exclamation(text):
    return text + "!"

data = {"word": ["hello", "good", "bye"]}
df   = pd.DataFrame(data)

df["excited"] = df["word"].apply(add_exclamation)  # 这里没有参数的原因是.apply()自己会把参数填进去，这个参数就是da["word"]

# 也可以用 lambda，不用单独写函数：
# df["excited"] = df["word"].apply(lambda x: x + "!")


#____________  练习 _________________________


#  1. 理解题： 下面的代码，add_exclamation 会被调用几次？每次传进去的是什么？
# pythondata = {"word": ["hello", "good", "bye", "cool"]}
# df = pd.DataFrame(data)
# df["excited"] = df["word"].apply(add_exclamation)

#4, 传进去的word列的每一行


#  2. 操作题： 新建 day6_01_apply.py，写下面的内容并运行：
import pandas as pd

data = {"name": ["Alice", "Bob", "Charlie"]}
df = pd.DataFrame(data)

# 用 .apply() 加一列 name_len，存每个名字的字符数
# 提示：len("Alice") == 5

df["name_len"] = df["name"].apply(lambda x: len(x))
# 补一个小知识：lambda x: len(x) 可以再简写成直接传 len，因为 len 本身就是个函数：

print(df)
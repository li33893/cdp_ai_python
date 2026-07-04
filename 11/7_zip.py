"""
zip()

第 1 小块:它做什么
zip() 把两个列表按位置一一配对，一对一对地拿出来。
names  = ["a", "b", "c"]
scores = [90, 85, 77]

for name, score in zip(names, scores):
    print(name, score)
打印:
a 90
b 85
c 77
它像拉链——左边一颗齿、右边一颗齿，咬合成一对。第 1 个配第 1 个，第 2 个配第 2 个，第 3 个配第 3 个（zip 这个词本身就是"拉链"的意思）。
配对之后，for 循环里用 name, score 两个变量，一次接住一对里的两个值。


第 2 小块:两个列表长度不一样怎么办
规则:以短的那个为准，长的那个多出来的部分直接丢掉。
a = [1, 2, 3]
b = ["x", "y"]

for num, letter in zip(a, b):
    print(num, letter)
打印:
1 x
2 y
a 有 3 个，b 只有 2 个。zip 配到第 2 对时，b 已经用完了，就停下——a 里的 3 没有对象配，被丢掉，不报错。
所以 zip 出来的对数 = 两个列表里较短的那个的长度。
第 3 小块:项目里怎么用
agreement_check.py 要算"人工和 LLM 判断一致的有几条"。人工标签是一个列表，LLM 标签是另一个列表，两个列表一样长，第 i 个位置对应同一条帖子。
agree = sum(h == l for h, l in zip(human_labels, llm_labels))
拆开:

zip(human_labels, llm_labels) —— 把"第 i 条的人工标签"和"第 i 条的 LLM 标签"配成一对
h == l —— 每一对里，人工标签和 LLM 标签是否相等，相等得 True，不等得 False
sum(...) —— True 当作 1、False 当作 0 累加，数出有多少对相等，也就是一致的条数

混淆矩阵那几行也是同一招，比如数"两边都判相关"的：
tp = sum(h and l for h, l in zip(human_labels, llm_labels))
h and l 是"人工判相关且 LLM 判相关"，逐对看、累加。
zip 在这里的价值就是:让你能逐条对齐比较两个列表，而不用手动写 human_labels[0] vs llm_labels[0]、human_labels[1] vs llm_labels[1] 这样一个个索引。

"""

# 题目1（预测题）
a = [10, 20, 30, 40]
b = ["p", "q", "r"]

for x, y in zip(a, b):
    print(x, y)

# 会打印几行？分别是什么？
# 3 行
# 10 p
# 20 q
# 30 r


# 题目2（操作题）
# 模拟 agreement_check.py 的核心逻辑:
human_labels = [True, False, True, True, False]
llm_labels   = [True, True,  True, False, False]

# 用 zip 把这两个列表配对
# 数出有多少对是相等的（人工和 LLM 判断一致），存进变量 agree，print 出来
# 提示只在于结构:你需要 zip + 一个能累加"相等次数"的方式

agree = sum(human == llm for human, llm in zip(human_labels, llm_labels))

print(agree)
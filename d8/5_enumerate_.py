"""

enumerate() 在遍历列表的时候同时给你下标和值，不用自己维护一个计数变量。
fruits = ["apple", "banana", "cherry"]

for i, fruit in enumerate(fruits):
    print(i, fruit)
# 0 apple
# 1 banana
# 2 cherry

如果想从 1 开始计数，传第二个参数：
for i, fruit in enumerate(fruits, start=1):
    print(i, fruit)
# 1 apple
# 2 banana
# 3 cherry

没有 enumerate() 的话你得写：
i = 0
for fruit in fruits:
    print(i, fruit)
    i += 1

"""

# 定义 subreddits = ["mentalhealth", "depression", "Anxiety", "therapy"]，用 enumerate() 遍历，从 1 开始编号，每行打印格式为 1. mentalhealth、2. depression 这样。

subreddits = ["mentalhealth", "depression", "Anxiety", "therapy"]
for i, subreddit in enumerate(subreddits, start=1):
    print(f"{i}. {subreddit}")
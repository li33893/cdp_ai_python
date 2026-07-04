"""

df.empty — 检查 DataFrame 是否为空

if df.empty:
    print("没有数据")
    return
就一个属性，没有括号(意思是它不是方法，不需要加括号调用)，返回 True 或 False。

DataFrame 有数据 → df.empty 是 False
DataFrame 没有任何行 → df.empty 是 True


常见用法是在主流程里做保护，数据采集完发现是空的，就提前退出，不继续往下跑。


df.empty 只看行数是不是0，不看值是什么。
所以：
python{"name": [""]}   # 有1行，值是空字符串 → df.empty 是 False
{"name": [0]}    # 有1行，值是0 → df.empty 是 False
{"name": []}     # 有0行 → df.empty 是 True
"" 和 0 是值，只要有行就不算空。

"""

# 理解题： 下面哪种情况 df.empty 是 True？
# # 情况A
# df = pd.DataFrame({"name": []})

# # 情况B
# df = pd.DataFrame({"name": ["Alice"]})


"""

01_.tolist(),.astype(),.str accessor
.tolist()
把一个 pandas Series 转换成普通 Python list。

df["post_id"].tolist()
# ['p1', 'p2', 'p3']

用途:有些地方(比如给 API 传参、写 JSON)需要普通 list,不能直接用 Series。

02_.astype()
强制转换一列的数据类型。

df["risk_level"].astype(str)     # 数字转字符串
df["is_active"].astype(bool)     # 转布尔
df["score"].astype(int)          # 转整数(会截断小数)

03_.str accessor
一列如果是字符串,想用字符串方法(比如 .lower(),.strip()),不能直接 df["col"].lower()(会报错,因为整列不是单个字符串,是 Series)。
要先加 .str,表示"对这一列里每个字符串分别执行这个方法":

df["subreddit"].str.lower()      # 整列都变小写
df["subreddit"].str.strip()      # 整列去掉首尾空格
df["subreddit"].str.startswith("r/")   # 判断每个值是否以 "r/" 开头,返回布尔 Series
df["subreddit"].str.upper()      # 整列变大写

04_什么情况下会遍历列表什么时候不能：
核心规律
pandas Series 天生支持"向量化"操作的,只有这几类:

比较运算符:==, !=, >, <, >=, <=
逻辑运算符(专属 pandas 版本):&(且), |(或), ~(非)——注意不是 Python 的 and/or/not
数学运算符:+, -, *, /
pandas/numpy 提供的方法:.isin(), .str.xxx(), .astype(), .fillna(), .notna() 等等——这些方法内部已经帮你写好了"遍历每一行"的逻辑,你调用它就等于自动遍历了

这几类"天生不支持"整列,只能处理单个值:

Python 内置的 if...else / 三元表达式 —— 设计给单个值判断用的
Python 内置的 and / or / not —— 同样只认单个 True/False,不认一整列(这也是为什么 pandas 要专门发明 & | ~ 来替代)
列表推导式里裸的 for + 你自己写的逻辑(除非你手动指定"我知道我在一行行处理")

怎么快速判断能不能用向量化?
问自己一句话:"pandas 有没有现成的方法/运算符,直接做这件事?"

想判断"等不等于某个值" → 有,==,直接用
想判断"属不属于一组值" → 有,.isin(),直接用
想判断"字符串是否包含某内容" → 有,.str.contains()(还没教,但存在)
想做"复杂的、pandas 没有对应方法的自定义逻辑"(比如"如果A列大于10就取B列,否则取C列乘以2") → 这种复杂情况,才需要用到 d6 学的 .apply(),或者 np.where()(还没教)

简单说:两个值互相比较、字符串处理、类型转换——这些常见需求,pandas 几乎都有现成的"一次处理一整列"的方法。只有当你的逻辑复杂到 pandas 没有现成方法覆盖时,才需要 .apply() 或者写循环。

"""


import pandas as pd

df = pd.DataFrame({
    "post_id": [1, 2, 3, 4],
    "subreddit": ["  Depression", "THERAPY ", "anxiety", " MentalHealth"],
    "is_relevant": ["True", "False", "True", "True"],
})

# 把 subreddit 列统一去掉首尾空格,再转成小写,结果保存回 df["subreddit"],print 整个 df
df["subreddit"] = df["subreddit"].str.strip().str.lower()
print(df)
# 把 is_relevant 列(现在是字符串 "True"/"False")用 .astype(bool) 转成真正的布尔类型,print 这一列的 dtype
df["is_relevant"] = df["is_relevant"] == "True"
print(df["is_relevant"])
# 把处理好的 post_id 列用 .tolist() 转成普通 list,print 出来看看它是不是普通的 [1, 2, 3, 4]
list = df["post_id"].tolist()
print(list)
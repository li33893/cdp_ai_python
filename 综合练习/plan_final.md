# 学习计划（从Day 4开始）

> d1-d3已学：datetime, error, pagination, params, requests.get, sleep,
> json.dump(dict→文件), pd.DataFrame(list→表), df.to_csv, re.search/compile,
> f-string, json.loads(str→dict), payload, requests.post, try/except
>
> 以下全部是你还没学的。
> 每天30分钟，数据流日45–60分钟。

---

# collect 补课（Day 4）

## Day 4 — 列表 list

```python
all_raw = []           # 创建空列表
all_raw.append({"title": "hi"})  # 往后面加一个元素
len(all_raw)           # 数长度 → 1
all_raw[0]             # 取第一个元素（从0开始）→ {"title": "hi"}
all_raw[0]["title"]    # 先取列表第一个元素(字典)，再取字典的title → "hi"
```

列表推导式（collect第184行和239行）：
```python
# 普通写法
result = []
for p in TIME_PERIODS:
    if p[2] == "202501":
        result.append(p)

# 列表推导式（一行搞定，含义完全一样）
result = [p for p in TIME_PERIODS if p[2] == "202501"]
# 读法：对TIME_PERIODS里的每个p，如果p[2]=="202501"，就放进新列表
```

练：
```python
numbers = [1, 2, 3, 4, 5]
big = [n for n in numbers if n > 3]
print(big)  # → [4, 5]
```

---

d1/d2你学了字典基础。这三个你没学过：

```python
log = {}

# ⚠️ dict[key] = value → key不存在就新建，存在就覆盖
log["depression"] = {}           # 新建了 "depression" 这个key
log["depression"]["202301"] = {"raw_count": 50}  # 在嵌套字典里又新建了key
log["depression"]["202301"]["kw_hit_rate"] = 0.23  # 再深一层新建key
# 现在log长这样：
# {"depression": {"202301": {"raw_count": 50, "kw_hit_rate": 0.23}}}
```

```python
# dict.get(key, default) → 安全取值
p = {"title": "hello"}
p["body"]              # ❌ 报错KeyError，因为没有"body"这个key
p.get("body", "")      # ✅ 返回""，不报错
p.get("title", "")     # ✅ 返回"hello"
```

练：
```python
log = {}
log["anxiety"] = {}
log["anxiety"]["202501"] = {"count": 10}
log["anxiety"]["202501"]["hit_rate"] = 0.15
print(log["anxiety"]["202501"])  # → {"count": 10, "hit_rate": 0.15}
```

---
None + or兜底 + += 和其他小运算

```python
# None是Python的"空"——不是0，不是""，不是False，是"什么都没有"
x = None
print(x)  # → None

# or "" 兜底（collect第264行）
# .get防key不存在，or ""防value是None
title = p.get("title", "") or ""
# 情况1：p没有"title"这个key → get返回"" → ""是falsy → or不触发 → 结果""
# 情况2：p有"title"但值是None → get返回None → None是falsy → or触发 → 结果""
# 情况3：p有"title"值是"hello" → get返回"hello" → "hello"是truthy → or不触发 → 结果"hello"
# 为什么要双重保护：title后面要和body做字符串拼接，None + "text"会报TypeError
```

```python
# += 就是 x = x + 更新值 的缩写
total = 0
total += 5       # 等于 total = total + 5 → total现在是5
total += 3       # → total现在是8

# "=" * 50 → 字符串重复
print("=" * 50)  # 打印50个等号

# int() 类型转换
x = 3.7
int(x)  # → 3（截断小数，不是四舍五入）

# round() 四舍五入
round(0.2333, 3)  # → 0.233（保留3位小数）
round(0.2333, 1)  # → 0.2
```

---

## Day 5 
```python
# 元组：用()创建，创建后不能改
period = (datetime(2023,1,1), datetime(2023,1,31), "202301")
period[0]   # → datetime(2023,1,1) 和列表一样用[0]取值
period[2]   # → "202301"

# 元组拆包：一次性把元组里的值分别赋给多个变量
# collect第251行：
for (start_dt, end_dt, period_name) in periods_to_run:
    # 每次循环，元组的三个值分别赋给 start_dt, end_dt, period_name
    # 等价于：
    # start_dt = period[0]
    # end_dt = period[1]
    # period_name = period[2]
    print(period_name)

# _ 占位符：不需要的变量用_接住（collect第303行）
for (_, _, period_name) in periods_to_run:
    # 只需要第三个值，前两个用_丢弃
    print(period_name)
```

```python
# not in 检查不存在（collect第184行）
seen_ids = ["abc", "def"]
"xyz" not in seen_ids   # → True（xyz不在列表里）
"abc" not in seen_ids   # → False（abc在列表里）

# in 检查存在（collect关键词过滤）
"chatgpt" in "I use chatgpt daily"  # → True
"chatgpt" in "I use Claude daily"   # → False
```

---

```python
text = "  I use ChatGPT for therapy  "

text.lower()    # → "  i use chatgpt for therapy  " 全小写
text.strip()    # → "I use ChatGPT for therapy"    去头尾空格
text.split()    # → ["I", "use", "ChatGPT", "for", "therapy"] 按空格切成列表
len(text.split())  # → 5 算词数（collect的word_count函数）

# 拼接
title = "AI therapy"
body = "I use ChatGPT"
full_text = (title + " " + body).strip()  # collect第267行

# r"..." raw string（给正则用）
# 普通字符串：\b被Python当成退格符
# raw字符串：\b原样保留，传给re当"单词边界"
r"\bai\b"   # 正则引擎收到的是 \bai\b → 匹配独立的"ai"

# f-string格式化后缀（d3你学了f-string基础，这是新的）
hit_rate = 0.2333
f"{hit_rate:.1%}"    # → "23.3%" — .1%表示百分比保留1位小数
f"{hit_rate:.3f}"    # → "0.233" — .3f表示浮点数保留3位小数
```


```python
# return提前返回（collect的keyword_filter函数）
def keyword_filter(text):
    for keyword in KEYWORDS:
        if keyword in text:
            return True    # 找到了！直接返回True，下面的代码不执行
    return False           # 全部没找到，才走到这里返回False
# return True是"提前出口"——不需要遍历完整个列表

# 默认参数（collect的fetch函数）
def fetch_posts(subreddit, after, before, limit=100000):
    ...
# 调用时：
fetch_posts("depression", start, end)          # limit用默认值100000
fetch_posts("depression", start, end, 300)     # limit用300

# lambda匿名函数
# 普通函数：
def is_valid(x):
    return x not in ["[deleted]", "[removed]", "", None]

# lambda写法（一行搞定，含义完全一样）：
is_valid = lambda x: x not in ["[deleted]", "[removed]", "", None]
# lambda 参数: 返回值
# 冒号左边是参数（x），右边是返回值（x not in [...]）
# collect里lambda只在.apply()里用，不单独存在
```

---

## Day 6 
#— .apply + boolean indexing + .copy

```python
# .apply(函数) — 对一列的每一行调用函数（collect第285-292行）
# 传普通函数：
df["kw_pass"] = df["full_text"].apply(keyword_filter)
# full_text有1000行 → keyword_filter被调用1000次
# 每次传入一行的full_text值 → 返回True或False → 存进新列kw_pass

# 传lambda：
df["body_valid"] = df["body"].apply(
    lambda x: x not in ["[deleted]", "[removed]", "", None]
)
# 每行的body传进去当x → 判断 → 返回True/False

# boolean indexing 布尔索引（collect第295行）
df_filtered = df_raw[
    df_raw["kw_pass"] &              # kw_pass为True
    (df_raw["word_count"] >= 50) &   # 且word_count≥50
    df_raw["body_valid"]             # 且body_valid为True
]
# & 在DataFrame里表示"且"（不能用Python的and）
# 每个条件要用()括起来

# .copy() 创建独立副本（collect第298行）
df_filtered = df_raw[...].copy()
# 不加.copy()：df_filtered是df_raw的"视图"，改df_filtered会连带改df_raw
# 加了.copy()：完全独立，互不影响
```

---

#— with open + import + \_\_name\_\_

```python
# with open（collect第313行）
with open("log.json", "w", encoding="utf-8") as f:
    json.dump(log, f, ensure_ascii=False, indent=2)
# "w" → 写模式（write），文件不存在就创建，存在就覆盖
# as f → 给打开的文件取名叫f
# with结束时自动关闭文件 → 不用手动f.close()
# ensure_ascii=False → 中文不会变成\uXXXX
# indent=2 → JSON格式化缩进2格，方便人看
# d2你学json.dump时可能见过这个结构

# import（collect开头）
import requests              # 导入整个库 → 用requests.get()
import pandas as pd          # 导入并取别名pd → 用pd.DataFrame()
from datetime import datetime # 只导入库里的某个东西 → 直接用datetime()

# __name__ == "__main__"（collect最后）
if __name__ == "__main__":
    main()
# 直接运行 python collect.py → __name__自动等于"__main__" → 条件成立 → main()执行
# 别的文件 import collect → __name__等于"collect" → 条件不成立 → main()不执行
# 防止import时自动跑main()

# df.empty（collect第282行）
if df_raw.empty:   # DataFrame是否为空（0行）
    print("没数据")
    return
```

---

##  — 🔁 collect 完整数据流

通读你注释过的collect文件，只追数据走向：
```
配置区
 ├─ SUBREDDITS列表、TIME_PERIODS列表、KEYWORDS列表
 └─ TEST_MODE决定跑哪些

main()
 ├─ all_raw = []  空列表
 ├─ log = {}  空字典
 │
 ├─ 双层for循环：subreddit × time_period
 │   └─ fetch_posts() → API返回字典列表
 │       └─ 每个帖子取title/body/id → append到all_raw
 │       └─ log[sub][period] = {"raw_count": N}  ← dict新建key
 │
 ├─ pd.DataFrame(all_raw) → df_raw → 存raw.csv
 │
 ├─ .apply(keyword_filter)  → kw_pass列（True/False）
 ├─ .apply(word_count)      → word_count列（数字）
 ├─ .apply(lambda)          → body_valid列（True/False）
 │
 ├─ boolean indexing 三条件过滤 → df_filtered.copy() → 存filtered.csv
 │
 └─ for循环统计hit_rate → log[sub][period]["hit_rate"] = N  ← 嵌套dict新建key
     └─ json.dump(log) → 存log.json
```

**自测**：指着代码任意一行，能说出"这行在干什么、用了哪个概念"就过关。

---

# screening_prompt.py

## Day 7 — pd.read_csv + df.iterrows + continue

```python
# pd.read_csv 从文件读表格（collect用pd.DataFrame从列表创建，这是从文件创建）
df = pd.read_csv("posts_list_kw_filtered.csv", encoding="utf-8-sig")
# 返回一个DataFrame，和pd.DataFrame()创建的一模一样，只是数据来源不同

# df.iterrows 逐行遍历
for i, row in df.iterrows():
    # i是行号（0, 1, 2...）
    # row是这一行的数据
    title = row["title"]  # 取这行的title列的值
    body = row["body"]
    # 和.apply()区别：
    # .apply → 整列统一做同一个操作，不能中途控制
    # iterrows → 手动控制每一行干什么，可以加if判断、跳过、提前终止

# continue 跳过当前行
for i, row in df.iterrows():
    if row["body"] == "[deleted]":
        continue  # 跳过这一行，直接进入下一行
    # continue之后的代码不执行
    result = screen_post(row["title"], row["body"])  # 只有没被跳过的行才到这里
```

另外你会看到类型注解，不用学，认识就行：
```python
def screen_post(title: str, body: str) -> dict:
# ": str"表示参数应该是字符串，"-> dict"表示返回字典
# Python不强制执行，只是给人看的说明，删掉也不影响运行
```

---

 — 🔁 screening 数据流

```
kw_filtered.csv
  → pd.read_csv 读进来
  → for i, row in df.iterrows(): 逐行遍历
      → 每行：row["title"] + row["body"] 塞进f-string模板做prompt  [d3]
      → requests.post 发给Claude API  [d3]
      → try/except 防单条报错  [d3]
      → json.loads 解析返回字符串为字典  [d3]
      → 取 relevant / confidence / reason 三个字段
      → append到结果列表  [Day 4: list.append]
  → pd.DataFrame(结果列表)  [Day 4 + d2]
  → df.to_csv → screened.csv  [d2]
```

方括号里标了每个操作对应哪天学的。如果有看不懂的就回去翻那天的笔记。

---

# agreement_check.py（Day 15–18）

## pd.merge

```python
# 两个表按共同列合并（像Excel的VLOOKUP）
human_df = pd.read_csv("agreement_sample.csv")       # 有post_id + human_relevant
llm_df   = pd.read_csv("agreement_sample_llm_labels.csv")  # 有post_id + llm_relevant

merged = pd.merge(human_df, llm_df, on="post_id")
# on="post_id" → 按post_id对齐
# 结果merged既有human_relevant又有llm_relevant

# how参数（默认"inner"）
pd.merge(df1, df2, on="key", how="inner")  # 只保留两边都有的key
pd.merge(df1, df2, on="key", how="left")   # 保留左表全部，右表没有的填NaN

# suffixes 防列名冲突
# 如果两个表都有"label"列：
pd.merge(df1, df2, on="id", suffixes=("_human", "_llm"))
# 结果会有 label_human 和 label_llm 两列
```

练：
```python
import pandas as pd
df1 = pd.DataFrame({"id": [1,2,3], "score": [80,90,70]})
df2 = pd.DataFrame({"id": [2,3,4], "score": [85,75,95]})
merged = pd.merge(df1, df2, on="id", suffixes=("_a", "_b"))
print(merged)
# id只有2和3（inner join），两个score列变成score_a和score_b
```

---

## Day 16 — df.dropna + df.sample + pd.concat

```python
# df.dropna 删空行
merged = merged.dropna(subset=["human_relevant"])
# 只检查human_relevant这一列 → 如果是NaN（空）就删掉这行
# subset指定查哪些列，不写的话任何列有空都删

# df.sample 随机抽样
relevant = df[df["llm_relevant"] == True].sample(n=100, random_state=42)
# 先过滤出relevant为True的行，再从中随机抽100条
# random_state=42 → 每次运行结果一样（可重复）
# n=100 → 抽100条
# frac=0.5 → 抽50%（和n二选一）

df.sample(frac=1, random_state=42)
# frac=1 = 抽100% = 打乱顺序（所有行都在，但顺序随机了）

# pd.concat 上下拼接
sample = pd.concat([relevant, not_relevant])
# 把两个表纵向拼起来（行数相加）
# 注意和pd.merge区别：merge是横向按key对齐，concat是纵向堆叠
```

---

## Day 17 — cohen_kappa_score + np.array + .fillna + .astype

```python
# 安装sklearn（一次性）
# pip install scikit-learn --break-system-packages

from sklearn.metrics import cohen_kappa_score
import numpy as np

# cohen_kappa_score 计算两人标注一致性
human = [True, True, False, True, False]
llm   = [True, False, False, True, False]
kappa = cohen_kappa_score(human, llm)
# kappa → 0到1之间的数
# < 0.4 弱一致  0.4-0.6 中等  0.6-0.8 强  > 0.8 很强

# np.array 创建数组（比列表快，用于数学计算）
arr = np.array([1, 2, 3])
np.sum(arr)  # → 6

# .fillna 填充空值
df["col"].fillna("")
# NaN（空值）替换成""
# 为什么需要：cohen_kappa_score不接受NaN，会报错

# .astype 类型转换
df["col"].astype(str)
# 把这一列全部转成字符串
# 为什么需要：有时候True/False存成了字符串"True"/"False"，需要统一类型
```

---

## Day 18 — 🔁 agreement_check 数据流

```
screened.csv
  → 按llm_relevant分层抽样（True抽100 + False抽100 = 200条）  [Day 16: sample]
  → 存 agreement_sample.csv → 你手动标注human_relevant列
  → pd.read_csv 读回人类标注 + 读LLM标注
  → pd.merge 按post_id对齐  [Day 15]
  → dropna 删掉没标注的行  [Day 16]
  → cohen_kappa_score 算κ  [Day 17]
  → κ ≥ 0.8 → 通过，用LLM筛查结果
  → κ < 0.8 → 检查disagreements，修改coding manual
  → 不一致行：df[human != llm] 导出 → disagreements.csv  [Day 10: boolean indexing]
```

---

# data_cleaning.py（Day 19–20）

## Day 19 — drop_duplicates + value_counts

```python
# drop_duplicates 去重
df = df.drop_duplicates(subset=["body"], keep="first")
# subset=["body"] → 按body列判断重复（两条帖子body完全一样就算重复）
# keep="first" → 重复的只保留第一条
# 不写subset → 所有列都一样才算重复

# value_counts 频率统计
df["subreddit"].value_counts()
# → depression     800
#   Anxiety         500
#   therapy         400
#   ...
# 自动从多到少排序

df["subreddit"].value_counts(normalize=True)
# → depression     0.40
#   Anxiety         0.25
#   therapy         0.20
#   ...
# normalize=True → 变成百分比（小数形式）
```

练：
```python
import pandas as pd
df = pd.DataFrame({"name": ["a","b","a","c","b","a"], "score": [1,2,1,3,2,1]})
print(df.drop_duplicates(subset=["name"]))  # 只剩a,b,c各一行
print(df["name"].value_counts())  # a:3, b:2, c:1
```

---

## Day 20 — 🔁 data_cleaning 数据流

```
screened.csv
  → pd.read_csv
  → 删掉 llm_relevant == False 的行  [Day 10: boolean indexing]
  → drop_duplicates(subset=["body"]) 按body去重  [Day 19]
  → 过滤掉 body为[deleted]/[removed]/空 的行
  → 存 cleaned.csv（最终语料库，约2047条）
```

93行，最短的文件。30分钟够。

---

# rickwood_coding.py（Day 21–27）

## Day 21 — argparse 命令行参数

```python
# 之前的文件都是直接改代码里的变量来配置（比如collect改TEST_MODE）
# argparse让你在终端传参数：python script.py --input data.csv

import argparse

parser = argparse.ArgumentParser()                     # 创建解析器
parser.add_argument("--input", required=True)          # 添加必须的参数
parser.add_argument("--limit", type=int, default=10)   # 可选参数，默认10
args = parser.parse_args()                             # 解析命令行

print(args.input)  # → 用户传的值
print(args.limit)  # → 用户传的值，或默认值10

# 运行方式：
# python script.py --input pilot_sample.csv
# python script.py --input pilot_sample.csv --limit 5
```

练：写一个脚本接收 --name 参数并打印 hello {name}

---

## Day 22 — os.path + sys.exit

```python
import os
import sys

# os.path.exists 检查文件是否存在
if os.path.exists("output.csv"):
    print("文件已存在")

# os.path.basename 从路径取文件名
os.path.basename("/home/user/data.csv")  # → "data.csv"

# os.path.splitext 拆文件名和扩展名
os.path.splitext("data.csv")  # → ("data", ".csv")

# os.path.join 拼路径（比手动+安全）
os.path.join("output", "result.csv")  # → "output/result.csv"

# sys.exit 强制退出
sys.exit(1)  # 1表示异常退出，0表示正常退出
# 出错时用：发现输入文件不存在 → 打印错误信息 → sys.exit(1)
```

---

## Day 23 — set集合 + 断点续传模式

```python
# set 集合 → 元素不重复，查找极快
done = set(["abc", "def", "ghi"])  # 创建集合
"abc" in done   # → True  ← 查找O(1)，不管集合多大都一样快
"xyz" in done   # → False

# 对比list查找：
done_list = ["abc", "def", "ghi"]
"abc" in done_list  # 也是True，但要一个一个找，O(n)，数据多了很慢

# 从DataFrame创建set：
done = set(old_df["post_id"])  # 把post_id列的所有值放进集合

# 断点续传模式（rickwood_coding的核心设计）：
if os.path.exists("output.csv"):                # 有上次的输出文件吗？
    old_df = pd.read_csv("output.csv")          # 有 → 读进来
    done = set(old_df["post_id"])               # 取已处理的ID
else:
    done = set()                                 # 没有 → 空集合

for idx, row in df.iterrows():
    if row["post_id"] in done:                   # 这条处理过了？
        continue                                  # 跳过 [Day 13]
    # ... 处理新的 ...
    # 处理完后保存（防止跑到一半崩了全丢）
```

---

## Day 24 — while + break + df.rename + json.dumps

```python
# while循环（d1 pagination你见过，这里是重试模式）
attempt = 0
while attempt < 3:          # 最多试3次
    try:
        response = requests.post(url, json=payload)
        result = json.loads(response.text)
        break                # ✅ 成功 → break跳出while循环
    except Exception as e:
        attempt += 1         # ❌ 失败 → 计数+1，回到while判断
        print(f"第{attempt}次失败: {e}")
# break → 强制跳出最近的while/for循环
# continue(Day 13) → 跳过当前这一轮，进入下一轮

# df.rename 改列名
df = df.rename(columns={"old_name": "new_name", "col2": "new_col2"})
# columns参数是个字典：{旧名: 新名}

# json.dumps（注意有个s）
# d1/d2学的：json.dump(dict, file)  → 字典写进文件
# d3学的：  json.loads(string)      → 字符串变字典
# 新的：    json.dumps(dict)        → 字典变字符串（在内存里，不写文件）
# dump + s = dump to string
import json
text = json.dumps({"a": 1, "b": 2})
print(text)       # → '{"a": 1, "b": 2}' 是个字符串
print(type(text)) # → <class 'str'>
```

---

## Day 25 — 🔁 rickwood_coding 数据流（上：输入到prompt）

```
命令行：python rickwood_coding.py --input pilot_sample.csv
  → argparse解析参数  [Day 21]
  → pd.read_csv 读数据  [Day 13]
  → os.path.exists 检查断点文件  [Day 22]
      → 有 → 读取 → set()取已处理ID  [Day 23]
      → 没有 → done = set()
  → coding manual（Rickwood三个维度的编码规则）嵌入prompt模板
  → for idx, row in df.iterrows():  [Day 13]
      → if post_id in done: continue  [Day 23]
      → row["title"] + row["body"] 塞进f-string prompt
```
今天只看到prompt构造为止。

---

## Day 26 — 🔁 rickwood_coding 数据流（下：API到输出）

```
      → requests.post 发给Claude API  [d3]
      → try/except 防报错  [d3]
      → json.loads 解析返回  [d3]
      → 从返回字典里取 timeframe / source / usage_intent 三个值
      → append到结果列表  [Day 4]
  → 每N条 df.to_csv 中间保存（断点续传的另一半）
  → 全部完成 → 最终输出编码结果CSV

和screening对比：
  - screening：1个判断（relevant/not）
  - rickwood：3个维度（timeframe/source/usage_intent）+ 排除判断
  - rickwood多了：argparse、断点续传、更复杂的prompt
```

---

# batch_coding.py（Day 27–28）

## Day 27 — 指数退避 + HTTP状态码 + 中间保存

```python
# ** 指数运算
2 ** 0  # → 1
2 ** 1  # → 2
2 ** 2  # → 4
2 ** 3  # → 8

# 指数退避（exponential backoff）
# rickwood Day 24学了while+break重试，batch在此基础上加了"越等越久"
base_wait = 1
attempt = 0
while attempt < 5:
    try:
        response = requests.post(...)
        if response.status_code == 200:  # 成功
            break
        elif response.status_code == 429:  # 太快了
            wait = base_wait * (2 ** attempt)  # 1s, 2s, 4s, 8s, 16s
            print(f"限流，等{wait}秒")
            time.sleep(wait)
            attempt += 1
        elif response.status_code >= 500:  # 服务器挂了
            attempt += 1
    except Exception:
        attempt += 1

# HTTP状态码（三个要记住的）
# 200 → 成功
# 429 → "你请求太快了，稍等" → 指数退避
# 5xx (500, 502, 503) → 服务器自己出问题 → 等一下重试

# 中间保存（每100条存一次）
for i, row in df.iterrows():
    results.append(process(row))
    if len(results) % 100 == 0:          # % 是取余数：100÷100余0，200÷100余0
        pd.DataFrame(results).to_csv("checkpoint.csv")
        print(f"已保存{len(results)}条")
# 为什么：跑2047条可能要几小时，中途崩了不至于全丢
```

---

## Day 28 — 🔁 batch_coding 数据流

```
cleaned.csv（约2047条）
  → 和rickwood_coding几乎一样的流程，但增强了：
    ✦ 指数退避重试（rickwood只是简单重试）  [Day 27]
    ✦ HTTP状态码判断（429等/5xx等/200继续）  [Day 27]
    ✦ 每100条中间保存checkpoint  [Day 27]
  → 输出 llm_coded.csv（全量编码结果）
```

对比着看rickwood_coding，找到多出来的代码块。

---

# rickwood_validation.py（Day 29–33）

## Day 29 — Counter + np.nan

```python
# Counter 自动计数
from collections import Counter
labels = ["Primary", "Supplement", "Primary", "NM", "Primary"]
Counter(labels)  # → {"Primary": 3, "Supplement": 1, "NM": 1}
Counter(labels).most_common(2)  # → [("Primary", 3), ("Supplement", 1)] 取最多的两个

# np.nan 代表缺失值
import numpy as np
np.nan           # 不是0，不是""，不是None——是pandas/numpy专用的"空"
np.nan == np.nan # → False ⚠️ NaN连自己都不等于自己！
# 所以不能用 == np.nan 判断，要用 pd.notna() 或 pd.isna()
```

---

## Day 30 — np.zeros + 混淆矩阵手写 + np.trace

```python
import numpy as np

# np.zeros 创建全零矩阵
cm = np.zeros((3, 3))  # 3行3列，全是0
# → [[0, 0, 0],
#    [0, 0, 0],
#    [0, 0, 0]]

# 混淆矩阵的含义（以3个类别为例）
# 行 = 实际标签，列 = 预测标签
#              预测Primary  预测Supplement  预测NM
# 实际Primary      8            1            0
# 实际Supplement    2            6            1
# 实际NM            0            1            5

# 对角线（8, 6, 5）= 预测正确的
# 非对角线 = 预测错的

# 手写填充逻辑
labels = ["Primary", "Supplement", "NM"]
for i in range(len(human)):
    row = labels.index(human[i])   # 实际标签对应第几行
    col = labels.index(llm[i])     # 预测标签对应第几列
    cm[row][col] += 1              # 那个格子+1

# np.trace 对角线之和
np.trace(cm)  # → 8+6+5 = 19（预测对了的总数）
np.sum(cm)    # → 所有格子之和 = 总数
accuracy = np.trace(cm) / np.sum(cm)  # → 正确率
```

---

## Day 31 — pd.notna + df.loc + print(file=f)

```python
# pd.notna 判断非空
pd.notna("hello")    # → True
pd.notna(np.nan)     # → False
pd.notna(None)       # → False

# 用在DataFrame里
mask = pd.notna(df["source"])  # 返回True/False列
valid = df[mask]               # 只保留source非空的行

# df.loc 按条件定位行和列
# Day 10学的 df[condition] 只能选行
# df.loc[condition, "col"] 能同时指定行和列
df.loc[df["kappa"] > 0.6, "status"] = "通过"
# 找到kappa>0.6的行，把它们的status列设为"通过"

# 也能用来取值
value = df.loc[df["name"] == "depression", "count"]

# print(file=f) 把打印内容写到文件
with open("matrices.txt", "w") as f:
    print("混淆矩阵:", file=f)      # 写进文件而不是打印到屏幕
    print(cm, file=f)               # 矩阵也写进文件
```

---

## Day 32 — 🔁 rickwood_validation 数据流

```
pilot人类编码 + LLM编码
  → pd.read_csv 读两份  [Day 13]
  → merge 按post_id对齐  [Day 15]
  →
  → 第一步：排除判断验证
  │  人类说排除 vs LLM说排除 → 算accuracy
  →
  → 第二步：三个维度分别验证（只看双方都未排除的帖子）
  │  → pd.notna过滤  [Day 31]
  │  → 每个维度：手写confusion matrix  [Day 30]
  │  → 每个维度：手写kappa  [Day 30: trace/sum]
  │  → 打印结果
  →
  → 第三步：不一致案例导出
  │  → df[human != llm] 过滤  [Day 10: boolean indexing]
  │  → 存 disagreements.csv
  →
  → 混淆矩阵写入txt  [Day 31: print(file=f)]
```

---

# spot_check_sample.py（Day 33）

## Day 33 — 🔁 spot_check_sample 数据流（无重大新概念）

所有概念都学过了：pd.read_csv、argparse、set()、df.sample、os.path.join、value_counts。

```
llm_coded.csv
  → pd.read_csv
  → 排除已标记excluded的行  [Day 10: boolean indexing]
  → df.sample(n=50, random_state=...)  [Day 16]
  → 输出两个文件：
    - spot_check_blind.csv（去掉LLM编码列 → 给人类盲编码用）
    - spot_check_llm_codes.csv（保留LLM编码 → 验证时对比用）
```

78行。30分钟够。

---

# spot_check_validate.py（Day 34–35）

## Day 34 — .fillna + sklearn confusion_matrix

```python
# .fillna 填充空值（和Day 29的np.nan配合）
df["col"].fillna("")  # NaN替换成空字符串
df["col"].fillna("unknown")  # NaN替换成"unknown"
# 为什么需要：很多函数（kappa、confusion_matrix）不接受NaN

# sklearn版confusion_matrix（和Day 30手写版对比）
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(human_labels, llm_labels, labels=["Primary", "Supplement", "NM"])
# 一行搞定，不用手写for循环填充
# labels参数指定类别顺序 → 决定矩阵的行列顺序
# 返回的cm和手写版格式一样，是个numpy二维数组

# 手写版 vs sklearn版：
# rickwood_validation.py → 手写（为了更细的控制和输出）
# spot_check_validate.py → 用sklearn（够用就行）
```

---

## Day 35 — 🔁 spot_check_validate 数据流

```
spot_check_blind.csv（你手动编码完成后）
  + spot_check_llm_codes.csv
  → pd.merge 对齐  [Day 15]
  → .fillna("").astype(str) 预处理  [Day 17 + Day 34]
  → 三个维度分别：
      → cohen_kappa_score  [Day 17]
      → confusion_matrix   [Day 34]
      → 不一致行打印出来看
  → 打印最终κ值 → 写进论文Section 3.5

和agreement_check对比：
  - agreement：二分类（relevant / not）→ 1个κ
  - spot_check：三个Rickwood维度 → 3个κ
```

87行。30分钟够。

---

# descriptive_stats.py（Day 36–38）

## Day 36 — pd.crosstab + reset_index

```python
# pd.crosstab 交叉表
ct = pd.crosstab(df["subreddit"], df["timeframe"])
#                  Habitual   One-time
# depression          120        80
# Anxiety              90        60
# therapy              70        50
# 行是第一个参数，列是第二个参数，格子里是计数
# 和value_counts的区别：value_counts是一维的，crosstab是二维的

# 取交叉表里某个格子
ct.loc["depression", "Habitual"]  # → 120  [Day 31: .loc]

# margins=True 加合计行和列
ct = pd.crosstab(df["subreddit"], df["timeframe"], margins=True)
# 多出一行All和一列All

# reset_index 把行名变回普通列
ct_flat = ct.reset_index()
# 原来subreddit是"行名"（index），reset后变成普通的一列
# 为什么需要：to_csv时index会丢失，reset后存CSV更干净
```

---

## Day 37 — np.sqrt + Wilson置信区间

```python
import numpy as np

# np.sqrt 开平方根
np.sqrt(4)    # → 2.0
np.sqrt(9)    # → 3.0

# Wilson置信区间（简化版）
# 一句话：某个比例的真实值有95%概率在这个区间内
p = 0.35      # 某类别占比35%
n = 2047      # 总数
z = 1.96      # 95%置信水平对应的值（固定的）

# 公式
margin = z * np.sqrt(p * (1 - p) / n)
ci_lower = p - margin
ci_upper = p + margin
# → 比如 (0.329, 0.371)
# 含义：真实比例有95%概率在32.9%到37.1%之间
```

练：p=0.35, n=200, 算一次CI → 区间会比n=2047时宽很多（样本少 → 不确定性大）

---

## Day 38 — 🔁 descriptive_stats 数据流

```
llm_coded.csv
  → pd.read_csv
  →
  → 第一步：单维度统计
  │  → 三个维度分别 value_counts  [Day 19]
  │  → 每个类别算Wilson CI  [Day 37]
  │  → 存 descriptive_stats_output.csv
  →
  → 第二步：交叉表
  │  → pd.crosstab(维度 × subreddit)  [Day 36]
  │  → 存 cross_tabs.csv
```

---

# 收尾（Day 39）

## Day 39 — 🔗 全pipeline串联

画一张完整链条，用自己的话说每一步：
```
Arctic Shift API
  → collect → kw_filtered.csv
      你学到的：list, dict, .apply, boolean indexing

  → screening → screened.csv
      你学到的：pd.read_csv, iterrows, requests.post

  → agreement_check（验证筛查质量，κ ≥ 0.8才通过）
      你学到的：merge, kappa

  → data_cleaning → cleaned.csv（2047条）
      你学到的：drop_duplicates, value_counts

  → rickwood_coding（pilot 80条，验证编码方案）
      你学到的：argparse, 断点续传, set

  → rickwood_validation（验证pilot编码，κ ≥ 0.6才通过）
      你学到的：confusion_matrix, Counter

  → batch_coding → llm_coded.csv（全量编码）
      你学到的：指数退避, 中间保存

  → spot_check（验证batch编码，κ再次检查）
      你学到的：sklearn confusion_matrix

  → descriptive_stats → 统计表
      你学到的：crosstab, Wilson CI
```

---

## 总览

| 文件 | Day | 概念天 | 数据流天 |
|---|---|---|---|
| collect补课 | 4–12 | 8 | 1 |
| screening | 13–14 | 1 | 1 |
| agreement | 15–18 | 3 | 1 |
| cleaning | 19–20 | 1 | 1 |
| rickwood_coding | 21–27 | 4 | 2 |
| batch_coding | 27–28 | 1 | 1 |
| validation | 29–32 | 3 | 1 |
| spot_check_sample | 33 | 0 | 1 |
| spot_check_validate | 34–35 | 1 | 1 |
| descriptive_stats | 36–38 | 2 | 1 |
| 串联 | 39 | 0 | 1 |
| **合计** | **39天** | **24** | **12+串联** |

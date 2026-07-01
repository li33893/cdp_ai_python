"""

df.loc[mask, col]

你已经会用 df[mask] 筛选出符合条件的整行。但有时候你不想看整行,只想看/改某一列。

df.loc[mask, "列名"]

.loc[] 里逗号前面是"筛选哪些行"(可以放 mask),逗号后面是"选哪一列或哪几列"。

举例,只看高风险帖子的 subreddit:
df.loc[mask, "subreddit"]

等价于先 df[mask] 再取 ["subreddit"],但 .loc 是一步到位,而且更重要的是——它可以用来赋值修改,普通的链式写法不行或不安全。
比如你想把高风险帖子的某一列统一改成某个值:
df.loc[mask, "note"] = "高风险已排除"
这样只会修改 mask 为 True 的那些行的 note 列,其他行不动。

"""

import pandas as pd

df = pd.DataFrame({
    "post_id": ["p1", "p2", "p3", "p4", "p5"],
    "subreddit": ["depression", "therapy", "Anxiety", "mentalhealth", "depression"],
    "risk_level": [1, 3, 1, 2, 3],
    "status": ["", "", "", "", ""]
})

# 用 .loc 只取出 risk_level 为 3 的帖子的 post_id 这一列,print 出来
# 用 .loc 把 risk_level 为 3 的行的 status 列,统一改成 "排除",然后打印整个 df 看看效果

risk_3  = df["risk_level"] == 3
print(risk_3)
id_of_3 = df.loc[risk_3, "post_id"]
print(id_of_3)
df.loc[risk_3, "status"] = "排除"
print(df)
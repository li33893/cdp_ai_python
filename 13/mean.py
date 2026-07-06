"""
01_.mean()

是 pandas / numpy 里求算术平均值的方法。

对一列数值求平均:总和 ÷ 个数。
pd.Series([2, 4, 6]).mean()   # (2+4+6)/3 = 4.0, series在df["post_id"]的时候就已经是series的形式了

关键点:布尔列上的 .mean()
你代码里 (human == llm).mean() 的 .mean() 作用在布尔列上,不是数值列。机制是:
求均值时,True 当 1、False 当 0。
pd.Series([True, True, False, True]).mean()
# = (1 + 1 + 0 + 1) / 4
# = 3/4 = 0.75

所以布尔列的均值 = True 的个数 ÷ 总个数 = True 的比例。

套到你的场景:
(human == llm)        # 一列布尔:每行是否一致
        .mean()       # = 一致的行数 / 总行数 = 一致率
195 行里若 180 行一致,结果就是 180/195 ≈ 0.923。这就是为什么一行 .mean() 能直接算出一致率——布尔转 0/1 求平均,恰好就是比例。
几个要注意的行为

1. 默认跳过 NaN
pd.Series([1, 2, None, 4]).mean()   # (1+2+4)/3 = 2.33,不是 /4
.mean() 默认 skipna=True,缺失值不计入分母。你这里 human/llm 都是完整 bool、无缺失,不受影响;但换个有空值的列时要留意分母变了。

2. Series 和 DataFrame 上行为不同
series.mean()      # 一个数
df.mean()          # 每列各算一个 → 返回一行(每列一个均值)
df.mean(axis=1)    # 每行各算一个
你用在单列 Series 上,返回单个数,正确。

3. list 没有 .mean()
[True, False, True].mean() 
原生 list 不带这个方法,得先转 Series 或 numpy 数组,或用 sum(lst)/len(lst)。
这跟之前讲的 list vs Series 是同一条线:.mean() 是 pandas/numpy 的方法,不是 Python list 的。


02_series

df["post_id"]的时候就已经是series的形式

跟numpy一样，有==的时候成对作比较返回bool

"""
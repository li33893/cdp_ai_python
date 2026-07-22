"""
GROUPBY

作用：
    根据一个或多个列进行分组。

用法：
    df.groupby(["column1", "column2"])

说明：
    值完全相同的行会被分到同一组。

常见搭配：
    .size()   -> 统计每组有多少行
    .count()  -> 统计每组非空值数量
    .sum()    -> 统计每组总和
    .mean()   -> 统计每组平均值

最常见写法：
    df.groupby(["column1", "column2"]).size()

记忆：
    groupby = 把相同的东西放到一起。
"""
"""
SIZE

作用：
    统计 DataFrame 或 groupby 对象中的元素数量。

常见用法：

    df.size

        返回整个 DataFrame 的元素总数。

        例如：
            3 行 × 4 列 = 12

    df.groupby(...).size()

        返回每个分组包含的行数。

示例：

    df.groupby("type").size()

结果：

    A    10
    B     5
    C     8

说明：

    size() 统计的是“行数”，包括 NULL（缺失值）。

记忆：

    size = 数有几个。
"""
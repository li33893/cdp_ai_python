"""

    datetime

    - the difference betweenb timestamp and datatime
        
        1. datetime模块概述#
        datetime模块是Python标准库中用于处理日期和时间的模块，它提供了几个重要的类：

        datetime.date：表示日期（年、月、日）。
        datetime.time：表示时间（时、分、秒、微秒）。
        datetime.datetime：表示日期和时间的组合。
        datetime.timedelta：表示两个日期或时间之间的差值。

        2. timestamp概述#
        timestamp（时间戳）是一个表示特定时间点的浮点数，它表示从1970年1月1日午夜（UTC）到指定时间点所经过的秒数。在Python中，可以使用time模块的time()函数获取当前的时间戳。


"""

from datetime import datetime

# datetime → 时间戳
dt = datetime(2023, 1, 1)
timestamp = int(dt.timestamp()) # dt.timestamp() 返回的是一个 float（浮点数），例如 1719360000.0。
                                # 加 int() 是为了把它转成整数，去掉小数点后的秒数部分，例如 1719360000。
                                # 注意：int() 是向零截断，不是四舍五入。如果需要四舍五入用 round() 替代。
print(f"datetime转时间戳：{timestamp}")

# 时间戳 → datetime
dt2 = datetime.fromtimestamp(timestamp)
print(f"时间戳转datetime：{dt2}")
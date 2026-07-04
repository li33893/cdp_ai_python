"""

    pd.read_csv 做的事情是把磁盘上已有的 CSV 文件读进来，变成同样的 DataFrame。读进来之后完全一样，之前学的所有操作都能用。

"""

# 先建一个练习用的 CSV 文件。在你的练习文件夹里新建 sample.csv，内容如下：
# name,score,status
# Alice,82,pass
# Bob,45,fail
# Carol,91,pass
import pandas as pd

df_list = [{"name": "Alice", "score": 82, "status": "pass"}, {"name": "Bob", "score": 45, "status": "fail"}, {"name": "Carol", "score": 91, "status": "pass"}]

df = pd.DataFrame(df_list)

df.to_csv("sample.csv", index=False, encoding="utf-8-sig")


# 用 pd.read_csv 读入 sample.csv
# 打印总行数
# 打印所有列名（用 .columns.tolist()）
result = pd.read_csv("sample.csv")
print (len(result))
print(result.columns.tolist())
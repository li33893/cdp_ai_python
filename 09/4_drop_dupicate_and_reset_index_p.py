import pandas as pd

df = pd.DataFrame({
    "post_id": ["p1", "p1", "p2", "p3", "p3", "p4"],
    "body": ["text a", "text a copy", "text b", "text c", "text c", "text d"],
    "word_count": [50, 80, 60, 40, 90, 70],
})

# 按 word_count 降序排序
# 对 post_id 去重,保留第一条(也就是排序后字数最大的那条)
# 重置索引(不保留旧索引)
# print 最终结果,观察一下:p1 和 p3 各自保留下来的是不是字数更大的那条?
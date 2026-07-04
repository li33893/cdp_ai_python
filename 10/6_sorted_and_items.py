"""

sorted() 带 key=
sorted 是把所有元素排序。
posts = [
    {"post_id": "p1", "score": 5},
    {"post_id": "p2", "score": 20},
    {"post_id": "p3", "score": 1},
]

sorted_posts = sorted(posts, key=lambda x: x["score"])
print(sorted_posts)

输出（按 score 从小到大排）：
[{'post_id': 'p3', 'score': 1}, {'post_id': 'p1', 'score': 5}, {'post_id': 'p2', 'score': 20}]

reverse=True：默认从小到大，加这个参数变成从大到小：

sorted(posts, key=lambda x: x["score"], reverse=True)

跟 pandas 的 .sort_values()（d9学过）有什么区别？

.sort_values() 是 pandas DataFrame/Series 专用方法，排的是表格数据
sorted() 是 Python 内置函数，可以排任何可迭代对象（列表、字典的 keys 等），不限于 pandas

场景：你手头是普通 list/dict（不是 DataFrame）的时候，就得用 sorted()，.sort_values() 用不了。


"""

subreddit_counts = {
    "depression": 320,
    "Anxiety": 150,
    "therapy": 480,
    "mentalhealth": 90
}

# 把这个字典转成 (key, value) 元组列表（提示：.items()，d5学过），按 value 从大到小排序，赋值给 sorted_list
# print sorted_list
# 用 sorted_list[0] 取出数量最多的 subreddit，print 出来

items_list   = list(subreddit_counts.items())
sorted_list = sorted(items_list, key=lambda x: x[1], reverse=True)
print(sorted_list)

top = sorted_list[0]
print(top)


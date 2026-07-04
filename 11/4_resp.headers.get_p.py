# 题目1（预测题）
# headers = {"retry-after": "45"}

# a = headers.get("retry-after")
# b = headers.get("content-type")

# print(a)
# print(type(a))
# print(b)
# （这里我用普通字典模拟 headers，效果和 resp.headers 一样）
# 三行各打印什么？特别注意第二行 type(a)——a 是字符串还是数字？


# 题目2（操作题）

# 建一个字典模拟 headers：headers = {"retry-after": "10"}
# 用 .get() 读出 retry-after 的值，存进变量 retry_after
# 用 if retry_after: 判断有没有读到
# 如果读到了，用 float() 把它转成数字，加上 5，print 出结果（应该是 15.0）
# 再试一次读一个不存在的键，比如 headers.get("does-not-exist")，把结果 print 出来，看它是什么


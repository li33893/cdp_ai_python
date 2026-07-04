"""

tuple: 元组用 () 创建，跟列表很像，区别是创建之后不能改里面的值

元组经常用来打包"一组相关的数据"，比如一个时间段的开始、结束、标签，放一起比较整洁
元组存在的意义就是：表达"这几个东西是一组，不能单独改"

列表是"一堆同类的东西"，可以随时加减改。元组是"配套的一组东西"，打包好就不动了。
("2023-01-01", "2023-01-31", "202301") 这三个值是一个时间段的开始、结束、标签，它们必须配套使用，哪个单独被改掉都没意义——用元组就是在告诉 Python（也告诉读代码的人）：这三个是一组，别动。
另外元组比列表稍微快一点点

"""

#  1. 有这个元组：
record = ("mentalhealth", "abc123", True)
# 用元组拆包把它分成三个变量 subreddit、post_id、relevant，然后打印：
# subreddit: mentalhealth
# post_id: abc123
# relevant: True

subreddit, post_id, relevant = record
print(f"subreddit: {subreddit}\npost_id: {post_id}\nrelevant: {relevant}")


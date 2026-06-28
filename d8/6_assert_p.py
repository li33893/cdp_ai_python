"""

assert 用来检查某个条件是否为 True，如果不是就立刻报错停下来。语法：
assert 条件, "错误信息"
x = 10
assert x > 0, "x 必须是正数"   # 通过，什么都不发生

y = -5
assert y > 0, "y 必须是正数"   # 失败，抛出 AssertionError: y 必须是正数

主要用来在代码里设置"检查点"——你认为某个值在这里一定满足某个条件，如果不满足说明出了问题，应该立刻知道，而不是让程序带着错误数据继续跑下去。
比如处理数据之前先确认数据不是空的：
data = [1, 2, 3]
assert len(data) > 0, "数据不能为空"

"""
# 第一个：定义 sample_size = 100，断言它大于 0，打印 "sample size ok"
sample_size = 100
assert sample_size>0,  "sample must be positive"
print("sample is ok")

# 第二个：定义 label = "Habitual"，断言它在 ["Habitual", "Episodic", "NM"] 里，打印 "label ok"
label = "Habitual"
assert label in ["Habitual", "Episodic", "NM"], "the unkown is not available"
print("label ok")
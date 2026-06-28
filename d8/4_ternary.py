"""

三元表达式

把简单的 if/else 写成一行的语法：

python值A if 条件 else 值B
条件为 True 返回值A，条件为 False 返回值B。

score = 85
result = "pass" if score >= 60 else "fail"
print(result)   # "pass"


等价于：
pythonif score >= 60:
    result = "pass"
else:
    result = "fail"

"""

# 定义 temperature = 38，用三元表达式赋值给变量 status：温度大于 37.5 就是 "fever"，否则是 "normal"，打印 status
temperature =38

status = "normanl" if temperature<37.5 else "fever" 
print(status)
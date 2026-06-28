"""

多重 except 是针对不同类型的错误分别处理，而不是用一个 except 捕获所有：
try:
    x = int("abc")
except ValueError:
    print("值不对，无法转换")
except TypeError:
    print("类型不对")
except Exception as e:
    print(f"其他错误：{e}")
从上往下匹配，匹配到第一个符合的就执行，不再往下看。Exception 放最后作为兜底。

"""

# 写一个函数 safe_divide(a, b)，用多重 except 处理两种情况：b 为 0 时打印 "不能除以零"，a 或 b 不是数字时打印 "必须是数字"，正常情况打印结果。

def safe_divide(a, b):
    try:
        result = a / b
        print(result)
    except ZeroDivisionError:
        print("不能除以零")
    except TypeError:
        print("必须是数字")

safe_divide(10, 2)     # 5.0
safe_divide(10, 0)     # 不能除以零
safe_divide(10, "a")   # 必须是数字



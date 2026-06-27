"""

__name__ == "__main__" — 既能被 import，又能直接运行

"""

# 有时候一个文件你希望它：

# 被别人 import 时，只提供函数，不自动执行任何东西
# 直接运行时，执行测试或主流程

# 这时候就用 if __name__ == "__main__"。



# Python 运行文件时，会自动给这个文件设置 __name__ 变量：

# 直接运行 → __name__ 自动等于 "__main__"
# 被 import → __name__ 自动等于文件名，比如 "calculator"



def add(a, b):
    return a + b

if __name__ == "__main__":
    print(add(1, 2))


# 直接运行这个文件 → 条件成立 → print 执行
# 被 import → 整个文件从头走一遍，走到条件时不成立 → print 跳过

# 如果你的文件只会被直接运行，不会被别人 import，不写这个也完全没问题。
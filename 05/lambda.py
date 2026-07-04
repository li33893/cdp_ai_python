"""

lambda 是一种简写函数，适合只用一次、逻辑很简单的情况

1. 普通函数：
def is_valid(x):
    return x not in ["[deleted]", "[removed]", "", None]

2. lambda 写法，完全等价：
is_valid = lambda x: x not in ["[deleted]", "[removed]", "", None]
格式就是：lambda 参数: 返回值，冒号左边是参数，右边是返回的东西

"""


#  用 lambda 写一个函数 word_count，接收一段文字，返回词数

word  = "ChatGPT helped me feel less alone"

word_count = lambda word: len(word.split())

print(word_count(word))
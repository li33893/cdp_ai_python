"""

知识点1:argparse

01_它是干什么的

先看你平时怎么跑脚本:

python day11_01_argparse.py --input abc.csv

1. python 1_argparse.py 在python运行这个文件
2. --input abc.csv 输入的内容会原封不动地塞给脚本

但这里有个问题：
python 拿到这个文件以后并不会直接看懂是什么意思
所以我们需要提前告诉它规则：
“如果这串字里出现--input，他后面跟着的那个词就是我要的词“

import argparse                       # import

parser = argparse.ArgumentParser()    # 制造一个空的规则本
parser.add_argument("--input")        # 写入第一条规则："遇到 --input，把它后面那个词存起来。"
                                      # add_argument 直译就是"添加参数"——每写一行，规则本里多一条规则。
args = parser.parse_args()            # Python 拿着规则本，去看终端塞进来的那串字（--input abc.csv），按规则拆开——"哦，--input 后面是 abc.csv，存起来。
print(args.input)                     # 怎么取出来？用 args. + 参数名


02_终端那里什么都没敲的时候会发生什么？

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--input")
args = parser.parse_args()
print(args.input)                      #打印None

这时候可以给规则加一个“没传的时候的默认值”：

parser.add_argument("--input", default="pilot_sample.csv")

意思是："遇到 --input 就存它后面的值；如果整串字里根本没有 --input，就用 pilot_sample.csv 顶上。"


03_不跟值的开关参数

前面学的--input 文件名是带值的：参数名后面跟一个值

还有一种参数后面不跟值：

python day11_01_argparse.py --resume

敲了--resume -> 开（True）
没敲         -> 关（False）

规则是这么写的：

parser.add_argument("--resume", action="store_true")

action="store_true" 是固定写法，直译是"存入 True"。意思是告诉规则本：

"这个参数是开关。终端那串字里出现了 --resume，就把它记为 True；没出现，就记为 False。别去找它后面的值，它没有值。"

取值方式不变，还是 args.resume



04_type

带值参数收到的值，是什么类型
看这段代码：

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--n", default=50)
args = parser.parse_args()
print(args.n)

终端敲：
python day11_01_argparse.py --n 100
打印出 100。但问题是：这个 100 是整数 100，还是字符串 "100"？
答案：字符串 "100"。

原因回到第 1 小块——终端塞给 Python 的本来就是一串字。--n 100 里的 100，在那串字里就是三个字符 1、0、0。Python 拆完存起来，存的还是字符串。它不会自作主张帮你转成数字。
这会踩坑。比如你拿它去算术：
print(args.n + 1)   # 报错！字符串不能加数字

解决办法：在规则里加 type=int
pythonparser.add_argument("--n", type=int, default=50)
type=int 的意思是："拆出这个值之后，顺手帮我转成整数再存。"
加了之后，args.n 就是整数 100，可以直接算术。

一个容易混的细节
如果终端没敲 --n，用的是 default=50 —— 这个 50 本来就是你在代码里写的整数，不经过"终端那串字"，所以它天生就是整数。
也就是说不加 type=int 时会出现很别扭的情况：


"""

# 题目 1（预测题）
# import argparse

# parser = argparse.ArgumentParser()
# parser.add_argument("--limit", default=200)
# parser.add_argument("--test", action="store_true")
# args = parser.parse_args()
# print(args.limit)
# print(args.test)
# 终端敲：python day11_01_argparse.py --test
# 两行 print 各打印什么？
# 200    True

# 题目 2（判断题）
# 同样的代码，终端敲：python day11_01_argparse.py --limit 500
# 第一行打印的 500 是整数还是字符串？如果我想让 args.limit + 100 能算出 600，代码要怎么改一处？
# 字符串  
# parser.add_argument("--limit", type=int, default=200)
# print(args.limit + 100)

# 题目 3（操作题）
# 在 day11_01_argparse.py 里写一段完整的 argparse 代码，要求：
# 一个带值参数 --corpus，默认值 "posts_list_cleaned.csv"
# 一个带值参数 --seed，要求是整数，默认值 42
# 一个开关参数 --verbose
# 最后把三个值都 print 出来

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--corpus", default="posts_list_cleaned.csv")
parser.add_argument("--seed", type=int, default=42)
parser.add_argument("--verbose", action="store_true")
args = parser.parse_args()
print(args.corpus)
print(args.seed)
print(args.verbose)

# python d11/1_argparse.py --corpus abc.csv --seed 7 --verbose

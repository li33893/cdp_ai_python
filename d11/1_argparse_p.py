# 题目 1（预测题）
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--limit", default=200)
parser.add_argument("--test", action="store_true")
args = parser.parse_args()
print(args.limit)
print(args.test)
# 终端敲：python day11_01_argparse.py --test
# 两行 print 各打印什么？
# 题目 2（判断题）
# 同样的代码，终端敲：python day11_01_argparse.py --limit 500
# 第一行打印的 500 是整数还是字符串？如果我想让 args.limit + 100 能算出 600，代码要怎么改一处？
# 题目 3（操作题）
# 在 day11_01_argparse.py 里写一段完整的 argparse 代码，要求：

# 一个带值参数 --corpus，默认值 "posts_list_cleaned.csv"
# 一个带值参数 --seed，要求是整数，默认值 42
# 一个开关参数 --verbose
# 最后把三个值都 print 出来
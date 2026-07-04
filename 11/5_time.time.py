"""

知识点 6:time.time()
文件名:day11_06_time.py

关联文件:batch_coding.py（算进度、预估剩余时间那段）。

第 1 小块:它返回什么

import time

time.time()
返回当前这一刻的时间戳——从 1970 年 1 月 1 日 0 点开始，到现在过了多少秒，是一个很大的浮点数，类似:

1782000000.123456
这个数字本身没法直接看懂（谁能一眼看出这是哪年哪月），它唯一的用途是:拿两次调用的结果相减，算出中间经过了多少秒。


start = time.time()
# ...中间做点什么事，比如跑一个循环...
end = time.time()

elapsed = end - start   # 这段代码跑了多少秒
结束时刻减开始时刻 = 经过的秒数。这就是 time.time() 的全部作用。

第 2 小块:别跟 time.sleep() 搞混
你早就用过 time.sleep(0.5)——那是让程序暂停 0.5 秒。

time.time() 不暂停任何东西，它只是"看一眼现在几点了"，瞬间执行完，跟暂停完全无关。

一个是"停一下"，一个是"看一眼表"，作用完全不同，但名字很像，容易搞混。

先停这两小块。确认:time.time() 返回当前时间戳（一个数字），用两次调用相减算出经过的秒数；它不会让程序暂停，这一点和 time.sleep() 不一样——通了吗？

通了我讲第 3 小块:项目里怎么用它算进度和预估剩余时间。

继续


Progressed toward implementing time-based functionality
Progressed toward implementing time-based functionality
规则确认，全部记下，继续按这套走。

time.time() 前两小块讲完（返回时间戳、和 sleep 的区别），继续第 3 小块。

知识点 6:time.time()（继续）
文件名:day11_06_time.py

第 3 小块:项目里怎么用它
batch_coding.py 要跑 1200 条帖子，很花时间。代码里用 time.time() 做两件事:算已经跑了多久、预估还要多久。


start_time = time.time()

# ... 循环处理每条帖子 ...

elapsed = time.time() - start_time
rate = coded_count / max(elapsed, 1) * 60    # 每分钟处理多少条
eta = remaining / (rate / 60)                 # 预计还要多少秒
逐行拆:

start_time = time.time() —— 循环开始前，记一下"现在几点"
循环跑完一部分后，time.time() - start_time —— 拿"现在几点"减去"开始时几点"，算出已经过了多少秒，存进 elapsed
coded_count / elapsed —— 已完成条数除以用掉的秒数 = 每秒处理几条，乘 60 换算成每分钟几条，这就是 rate（速度）
remaining / (rate / 60) —— 剩下的条数除以每秒速度，算出还要多少秒才能跑完，这就是 eta（预计剩余时间，estimated time of arrival 的缩写）
关于 max(elapsed, 1)——这是 d8 学过的 max 用法在这里的实战。刚开始跑的时候，elapsed 可能非常接近 0（比如 0.001 秒），如果直接拿它当除数，coded_count / elapsed 会因为除数太小而算出一个离谱的巨大数字，甚至如果正好是 0 会直接报错（除以零）。
用 max(elapsed, 1) 保证这个除数最小是 1，就不会出这个问题。

"""
# 题目1（预测题，不用跑代码）

import time

# start = time.time()
# total = 0
# for i in range(1000000):
#     total += i
# end = time.time()

# elapsed = end - start
# print(elapsed > 0)

# 这段代码跑一个循环（做点耗时的运算），最后判断 elapsed（经过的时间）是不是大于 0。这行 print 会打印 True 还是 False？说一下你的判断理由。
# true，因为现在的时间一定比start大，更何况经过了1000000次循环


# 题目2（操作题）

# 记录开始时间 start
# 用 time.sleep(2) 让程序暂停 2 秒（这是模拟"干活花了2秒"）
# 记录结束时间 end
# 算出 elapsed = end - start，print 出来（应该接近 2，比如 2.001 之类）
start = time.time()

time.sleep(2)

end = time.time()

elapsed = end - start

print(elapsed)
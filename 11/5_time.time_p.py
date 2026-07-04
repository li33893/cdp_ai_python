import time

# start = time.time()
# total = 0
# for i in range(1000000):
#     total += i
# end = time.time()

# elapsed = end - start
# print(elapsed > 0)

# 这段代码跑一个循环（做点耗时的运算），最后判断 elapsed（经过的时间）是不是大于 0。这行 print 会打印 True 还是 False？说一下你的判断理由。


# 题目2（操作题）

# 记录开始时间 start
# 用 time.sleep(2) 让程序暂停 2 秒（这是模拟"干活花了2秒"）
# 记录结束时间 end
# 算出 elapsed = end - start，print 出来（应该接近 2，比如 2.001 之类）
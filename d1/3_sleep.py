"""

    time.sleep()
    你发请求太快，服务器会觉得你在攻击它，然后把你封掉。time.sleep() 就是让程序等一会儿再继续。

"""


import time

print("开始")
time.sleep(2)    # 等2秒
print("2秒后")
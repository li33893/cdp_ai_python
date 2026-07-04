"""

01_os.path.exists() —— 文件真的存在吗

前面说 os.path 大多只摆弄文字、不管文件在不在。这一件是唯一的例外——它真的会去硬盘上查。

import os

os.path.exists("1_argparse.py")

这个文件/文件夹真的存在 → 返回 True
不存在 → 返回 False


02_os.path.basename() —— 从整串路径里抠出文件名

回到第 1 小块说的:一整串路径 = 文件夹部分 + 文件名部分。

C:\Users\32283\OneDrive\python\d11\1_argparse.py
└──────────── 文件夹部分 ────────────┘ └── 文件名 ──┘

basename 的作用:把前面文件夹部分全砍掉,只留最后的文件名。
pythonimport os

os.path.basename("C:/Users/32283/python/d11/1_argparse.py")

# 返回 "1_argparse.py"
base = 基本, name = 名字,合起来"基本名字",也就是最末尾那个文件名。不管前面文件夹有多少层,它只保留最后一段。
注意:它只是切字符串,不查文件在不在。 就算这个文件根本不存在,basename 照样能把文件名切出来——它只是在处理这串文字。(这点和上一件 exists 相反,exists 要查硬盘,basename 不查。


03_os.path.splitext() —— 把文件名和扩展名分开
先认一个词:扩展名。就是文件名最后那个点后面的部分，标明文件类型:

spot_check.csv → 扩展名是 .csv
1_argparse.py → 扩展名是 .py

splitext 的作用:把"名字"和"扩展名"从中间那个点切成两半。（split = 切开，ext = extension 扩展名）
pythonimport os

os.path.splitext("pilot_sample.csv")
# 返回 ("pilot_sample", ".csv")
注意两点:

它返回的是两个东西，用括号包着——("pilot_sample", ".csv")。前半是名字，后半是扩展名（扩展名带着那个点）。
切的位置是最后一个点，点前面归名字，点和后面归扩展名。

怎么只取其中一半
返回的是两个东西，你想只要名字那半，用 [0]（第 0 个）:
pythonname = os.path.splitext("pilot_sample.csv")[0]
# name = "pilot_sample"
想要扩展名那半，用 [1]（第 1 个）:
pythonext = os.path.splitext("pilot_sample.csv")[1]
# ext = ".csv"
（这个"返回两个东西、用 [0] [1] 分别取"的形式叫元组，你 d10 的 crosstab、value_counts 那边接触过按位置取值，是同一个道理。）

04_os.environ.get()

第 1 小块:什么是环境变量
前面几件都是处理"路径文字"。这一件不一样，它读的是环境变量。
先讲环境变量是什么。它是存在操作系统里的键值对——不在你的 Python 代码里，而在系统层面。你可以把它想成"操作系统自己维护的一个大字典"，里面存着一些 名字→值 的对子，任何程序跑起来都能去问系统要。
为什么要用它?最典型的场景:存 API key。
你项目里 API key 现在是写死在代码里的:
pythonAPI_KEY = "sk-ant-api03-gAOx1Z...(一长串)"

问题:这份代码你要 push 到 GitHub（li33893/python）。key 写在代码里，一传上去，全世界都能看到你的 key，别人能拿去乱花你的钱。
解决办法:把 key 存到操作系统的环境变量里（不在代码文件中），代码运行时再去系统里读。这样代码文件本身不含 key，传 GitHub 也安全。

第 2 小块:os.environ.get() 怎么读

import os

API_KEY = os.environ.get("ANTHROPIC_API_KEY", "YOUR_API_KEY_HERE")

拆开:

os.environ —— 就是"操作系统那个大字典"
.get("名字", "默认值") —— 从字典里按名字取值，取不到就用默认值

参数:

第一个 "ANTHROPIC_API_KEY":要读的环境变量名字
第二个 "YOUR_API_KEY_HERE":如果系统里没设这个环境变量，就用这个顶上

这个 .get(名字, 默认值) 的用法，和你 d9 学的字典 .get() 一模一样——因为 os.environ 本质就是个字典。有就返回值，没有就返回默认值，不会报错。你已经会字典 get 了，这里是同一件事换了个字典。

第 3 小块:怎么在系统里设这个环境变量

代码负责"读"，但你得先在系统里"设"进去。你是 Windows + PowerShell，命令是:
$env:ANTHROPIC_API_KEY = "sk-ant-api03-你的key"
（你项目注释里写的 export ANTHROPIC_API_KEY='...' 是 Mac/Linux 的写法，Windows PowerShell 用 $env:，别照注释抄错。）
设完之后，代码里 os.environ.get("ANTHROPIC_API_KEY", ...) 就能读到这个 key 了。
"""

import os

a = os.environ.get("ANTHROPIC_API_KEY", "YOUR_API_KEY_HERE")
b = os.environ.get("SOME_KEY_NOT_SET", "default-value")
print(a)
print(b)
# （b 那行读的是一个没设过的环境变量，你判断它拿到什么。）
# default_value

# 题目2（操作题）
# 用 os.environ.get() 读一个叫 MY_TEST 的环境变量，读不到就用默认值 "nothing"，结果存进变量 val，然后 print 出来
# 先直接跑一次（不设环境变量），看打印什么
# 然后在 PowerShell 里敲 $env:MY_TEST = "hello" 设好，再跑一次同一个文件，看打印什么


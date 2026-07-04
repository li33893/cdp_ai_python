"""
resp.headers.get()

第 1 小块:HTTP 响应不止有正文
你之前用过 requests.get() / requests.post()，也用过 resp.json() 拿数据。但服务器回你的东西其实分两部分：

body（正文）——真正的数据内容，resp.json() 拿的就是这个

headers（头部）——附带的说明信息，跟数据本身无关，是"关于这次回复的元信息"

打个比方：你收快递，body 是箱子里的货，headers 是箱子外面贴的物流标签——上面写着"易碎品"、"重量多少"这类和货物本身不同的附加信息。


第 2 小块:headers 怎么读

resp.headers 用起来像字典——所以取值的方法你已经会了，就是 .get()：
resp.headers.get("retry-after")

如果这次响应里有这个头 → 返回它的值
如果没有 → 返回 None

注意一个关键点：headers 里的值，永远是字符串，不管内容看起来像不像数字。
比如 retry-after 就算返回 "30"，那也是字符串 "30"，不是整数 30。
这个和你之前学的 argparse 里"终端传进来的值都是字符串"是同一个道理——都是"外部传进来的原始数据，默认当字符串处理"。


第 3 小块:项目里为什么要读这个
你的 batch_coding.py 里调 API 调太快时，服务器会返回状态码 429（意思是"你请求太频繁了"）。
这时候服务器经常会顺便在 headers 里告诉你该等多久再来，那个信息就存在 retry-after 这个头里。
代码里这么用：
if resp.status_code == 429 or resp.status_code >= 500:
    retry_after = resp.headers.get("retry-after")
    if retry_after:
        wait = max(wait, float(retry_after))
逐行拆：

resp.headers.get("retry-after")——去读服务器有没有告诉你该等多久，读到就是字符串（比如 "30"），没读到就是 None
if retry_after:——检查有没有读到东西。这里在利用一个规律：None 在 if 判断里等同于 False，非空字符串等同于 True。所以这行是在问"服务器有没有给我这个提示？"
float(retry_after)——把字符串 "30" 转成数字 30.0，因为后面要拿它跟别的数字比大小（max(wait, ...)），字符串没法比大小运算

"""

# 题目1（预测题）
# headers = {"retry-after": "45"}

# a = headers.get("retry-after")
# b = headers.get("content-type")

# print(a)
# print(type(a))
# print(b)
# （这里我用普通字典模拟 headers，效果和 resp.headers 一样）
# 三行各打印什么？特别注意第二行 type(a)——a 是字符串还是数字？
# 45 string
# 字符串


# 题目2（操作题）

# 建一个字典模拟 headers：headers = {"retry-after": "10"}
# 用 .get() 读出 retry-after 的值，存进变量 retry_after
# 用 if retry_after: 判断有没有读到
# 如果读到了，用 float() 把它转成数字，加上 5，print 出结果（应该是 15.0）
# 再试一次读一个不存在的键，比如 headers.get("does-not-exist")，把结果 print 出来，看它是什么

headers        = {"retry-after": "10"}
retry_after    = headers.get("retry-after")
does_not_exist = headers.get("does-not-exist")

if retry_after:
    print(f"{float(retry_after) + 5}")

print(does_not_exist)


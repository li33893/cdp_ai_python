"""

    raise_for_status() 错误处理

    try:
        正常跑这里
        如果出错 → 跳到except
    except:
        出错了跑这里
        程序继续，不崩

    状态码:
    200成功
    404找不到这个页面
    500服务器出错

"""

import requests

# resp = requests.get("https://jsonplaceholder.typicode.com/posts/1")
# resp.raise_for_status()
# print("请求成功！", resp.status_code)


#  1.请求一个成功的URL、一个失败的URL，都用 try/except 包起来，打印出不同的提示信息 

# 成功的
try:
    resp = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    resp.raise_for_status()
    print("请求成功！", resp.status_code)
except requests.exceptions.HTTPError as e:
    print("请求出错了！", e)
#raise_for_status() —— 负责制造异常（看到坏状态码就扔出去）
# except HTTPError —— 负责接住异常（处理后续）
# 缺了前者，后者就是个永远不触发的摆设。

# 失败的
try:
    resp = requests.get("https://jsonplaceholder.typicode.com/posts/99999")
    resp.raise_for_status()
    print("请求成功！", resp.status_code)
except requests.exceptions.HTTPError as e:
    print("请求出错了！", e)
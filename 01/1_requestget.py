"""
  request.get()
  用来发送get请求，从服务器那里吧内容拿过来。

  我们平时在浏览器输入网址访问的时候，浏览器就是发送了一个get请求，服务器把内容返回给浏览器，浏览器把内容展示出来。
  request.post()就是让python去做这件事
"""

#引入requests库，requests是一个第三方库，专门用来发送http请求的，安装好requests库之后，就可以在python代码中引入requests库了。
import requests

resp = requests.get("https://jsonplaceholder.typicode.com/posts/1")


#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————

#  练习

#————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————

#  1. url → 请求的地址，服务器的地址
#  url的组成：
#  部分                         |      叫什么          |            意思
#  https://                            协议                    用加密方式传输
#  jsonplaceholder.typicode.com        域名                      服务器在哪
#  /posts                              路径                我要访问这个服务器上的哪个资源
#  /1                                  参数                     具体要第几条


#  2. 查看返回内容
#resp.status_code → 请求成不成功？200 = 成功
#resp.text → 服务器返回的内容，是个字符串

print(resp.status_code)
print(resp.text)


#  3. resp.text 是字符串，字符串只能用数字取第几个字符
#  print(resp.text["title"]) → 报错，字符串不能用字符串当索引


#  4. .json()把传回来的内容从 JSON 字符串转成 Python 字典
data = resp.json()
print(type(data))        # 看看现在是什么类型
print(data["title"])     # 现在试试取 title


#  5. 打印userId，idtitle
print(data["userId"])
print(data["id"])
print(data["title"])
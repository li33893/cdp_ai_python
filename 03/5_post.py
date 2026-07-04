
"""
requests.post(): 发请求


headers 是请求头，告诉服务器一些元信息：

Content-Type → 我发的是JSON格式
x-api-key → 我的身份验证key
anthropic-version → 用哪个版本的API

json=payload → 把payload字典自动转成JSON字符串发出去
timeout=60 → 60秒没回应就报错（Claude比普通API慢，所以给60秒）


返回内容：
{
    "id": "msg_123",
    "content": [
        {
            "type": "text",
            "text": "{\"relevant\": true, \"reason\": \"user describes AI use\"}"
        }
    ],
    ...
}


"""
import requests

resp = requests.post(
    "https://api.anthropic.com/v1/messages",
    headers={
        "Content-Type": "application/json",
        "x-api-key": "...",
        "anthropic-version": "2023-06-01"
    },
    json=payload,
    timeout=60
)
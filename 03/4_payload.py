"""
    payload 就是一个普通的Python字典，名字你自己起的，叫什么都行。
    约定俗成叫payload是因为它装的是"要发送出去的数据"——就像快递的包裹内容。

    # 字段         作用
    # model        用哪个Claude
    # max_tokens   最多回复多少token。token是文字的碎片。
                   中文大概1个字=1个token，英文大概4个字母=1个token
    # system       系统提示，告诉Claude它的角色，在对话开始之前就生效。
    # messages     对话内容，role只能是user或assistant

"""

# 构造一个payload字典，要求：

# model用 "claude-sonnet-4-20250514"
# max_tokens用 100
# messages里发一条用户消息："Is this post relevant to AI mental health?"

# 然后打印出 payload["messages"][0]["content"]

post_text = "Is this post relevant to AI mental health?"
SYSTEM_PROMPT = "You are a helpful assistant"

payload = {
    "model" : "claude-sonnet-4-20250514",
    "max_tokens" : 100,
    "system" : SYSTEM_PROMPT,
    "messages" : [
        {"role" : "user", "content" : post_text}
    ]
}

print(payload["messages"][0]["content"])
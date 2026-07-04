"""

.lower() 把字符串全转小写：
text = "I use ChatGPT"
text.lower()   # → "i use chatgpt"

.strip() 去掉头尾的空格（中间的不动）：
text = "  hello  "
text.strip()   # → "hello"

.split() 按空格切成列表：
text = "I use ChatGPT daily"
text.split()   # → ["I", "use", "ChatGPT", "daily"]
len(text.split())  # → 4，这就是词数

拼接用：
title = "AI therapy"
body = "I use ChatGPT"
full_text = (title + " " + body).strip()
# → "AI therapy I use ChatGPT"


(就是说strip有两个用法)

"""

text = "  ChatGPT really Helped Me  "
# 用这个变量，打印出：

# 全小写版本（去掉头尾空格）
# 这句话有几个词

final_text = text.lower().strip()
print(final_text)

number = len(final_text.split())
print(number)
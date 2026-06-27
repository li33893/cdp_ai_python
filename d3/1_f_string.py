"""

    知识点 1：f-string 模板字符串
    文件名：day3_01_fstring.py
    变量有值，字符串里想直接用它，就在字符串前加f，变量放{}里：
    pythonname = "ChatGPT"
    print(f"I used {name} last night")
    # → I used ChatGPT last night
    \n 是换行，\n\n 是空一行。

"""

#  有两个变量：
sub = "mentalhealth"
post_id = "abc123"

#  用f-string打印出：Post abc123 from r/mentalhealth
print(f"Post {post_id} from r/{sub}")
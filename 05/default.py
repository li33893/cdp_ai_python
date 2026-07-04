"""

函数定义时可以给参数一个默认值，调用时不传那个参数就用默认值

"""

def summarize(text, max_words=50):
    word_count = len(text.split())
    print(word_count)
    if word_count > max_words:
        print("超过限制")

# 直接调，不需要 main
summarize("ChatGPT helped me feel less alone")
summarize("ChatGPT helped me feel less alone", max_words=3)

# .replace(old, new)
# ------------------------------------------------
# - 是字符串(str)自带的方法,专门做"查找并替换"
# - 作用:把字符串里所有出现的 old 子串,换成 new 子串,返回一个新字符串
# - 常用来清掉模型输出里夹带的 markdown 代码围栏(```json 和 ```),
#   因为这些围栏不是合法 JSON 的一部分,直接 json.loads 会报错
#
# 例子:
# text = '```json\n{"excluded": false}\n```'
# text = text.replace("```json", "").replace("```", "").strip()
# # 结果: '{"excluded": false}'  —— 干净的 JSON 字符串,可以喂给 json.loads 了

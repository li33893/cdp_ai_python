"""

None 是 Python 的"空"，表示"什么都没有"

or 的逻辑是：左边有值就用左边，左边是"空的"就用右边

"""

a = None
b = ""
c = "hello"
d = 0
e = []
f = {}

print(a or "默认值")
print(b or "默认值")
print(c or "默认值")
print(d or "默认值")
print(e or "默认值")
print(f or "默认值")

# total = 0
# total += 5
# total += 3
# print(total)

# print("=" * 10)

# x = 3.7
# print(int(x))

# print(round(0.2333, 2))
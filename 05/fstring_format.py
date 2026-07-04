"""

fstring format: 在 {} 里控制数字的显示格式

:.1% 把小数转成百分比，保留1位小数

:.3f 保留3位小数的浮点数

"""

hit_rate = 0.6789
kappa = 0.841234

# 打印出：

# 命中率：67.9%
# Kappa：0.841

# 都是四舍五入，不是直接抹掉
print(f"{hit_rate:.1%}")
print(f"{kappa:.3f}")
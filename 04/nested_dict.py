"""

nested dictionary 嵌套字典

"""
# 1. 做一个这样的嵌套字典（至少有一个嵌套过程用了另一种方法）
# {'anxiety': 
#   {'202501': 
#     {'count': 10, 'hit_rate': 0.15}
#   }
# }

log = {}
log["anxiety"] = {}
log["anxiety"]["202501"] = {"count": 10}  # log["anxiety"]["202501"] [ "count"]=10
log["anxiety"]["202501"]["hit_rate"] = 0.15
print(log["anxiety"]["202501"])

# 2. 
# print(log.get("anxiety","none"))
# print(log["anxiety"]["202501"].get("count",0))
# print(log["anxiety"]["202501"].get("hit_rates",0))
# 分别打印出的是什么？
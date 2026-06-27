from datetime import datetime
# 1. 2024年6月15日 12时30分00秒  datetime → 时间戳
dt = datetime(2024,6,15,00,30,00)
ts = int(datetime.timestamp(dt))
print(f"{dt}转为时间戳{ts}。")
# 2. 时间戳 → datetime
dt_fromst = datetime.fromtimestamp(ts)
print(f"转回datetime:{dt_fromst}。")
#  1. 把下面这个字典存成 log.json，要求中文正常显示，每层缩进2个空格：
import json

pythonlog = {
    "mentalhealth": {
        "202301": {"raw_count": 150},
        "202302": {"raw_count": 200},
    }
}

with open("log.json", "w", encoding="utf-8") as log:
    # 带 = 的参数因为有名字，顺序无所谓。
    json.dump(pythonlog, log, ensure_ascii=False, indent=2)


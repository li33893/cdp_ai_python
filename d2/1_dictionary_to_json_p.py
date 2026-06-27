#  1. 把下面这个字典存成 log.json，要求中文正常显示，每层缩进2个空格：
import json
import os

pythonlog = {
    "mentalhealth": {
        "202301": {"raw_count": 150},
        "202302": {"raw_count": 300},
    }
}

folder = os.path.dirname(__file__)
path   = os.path.join(folder, "log.json")

with open(path, "w", encoding="utf-8") as log:
    json.dump(pythonlog, log, ensure_ascii=False, indent=2)
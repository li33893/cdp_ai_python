"""

混淆矩阵没有新的知识点，就理解了下面这个题就行了

"""

import numpy as np

# ── 材料1:文字→编号字典 ──
labels = ["苹果", "香蕉"]
label_to_idx = {l: i for i, l in enumerate(labels)}
# label_to_idx = {"苹果": 0, "香蕉": 1}

# ── 数据:5个水果,甲(人工)和乙(LLM)各判一次 ──
y1 = ["苹果", "苹果", "香蕉", "苹果", "香蕉"]   # 甲 = 人工
y2 = ["苹果", "苹果", "香蕉", "香蕉", "香蕉"]   # 乙 = LLM

# ── 材料2:建一面全0的靶子墙(2类 → 2×2)──
k = len(labels)                    # k = 2
cm = np.zeros((k, k), dtype=int)   # [[0,0],[0,0]]

# ── 核心:遍历5个水果(不是遍历格子!),每个水果砸中一个格子 ──
for a, b in zip(y1, y2):     # 一层循环,走的是"水果",跑5轮
    i = label_to_idx[a]      # 甲判的 → 行号
    j = label_to_idx[b]      # 乙判的 → 列号
    cm[i][j] += 1            # 这一个水果,砸中一个格子

print(cm)
# 题1(判断题,不用写代码)
# 如果 cohen_kappa_score(human, llm) 算出来是 0.85,按项目 κ≥0.7 通过的标准,这个维度通过还是不通过?这个 0.85 大概说明人工和 LLM 判得像不像?
# 像。

# 题2(操作题,写代码)
# 两串判断:
human = ["yes", "no", "yes", "yes", "no"]
llm   = ["yes", "no", "no", "yes", "no"]
# 用 sklearn 的两个函数:

# 打印 cohen_kappa_score 算出的 κ
# 打印 confusion_matrix,labels 用 ["yes", "no"]
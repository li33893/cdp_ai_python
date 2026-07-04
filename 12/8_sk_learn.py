"""

① cohen_kappa_score(a, b) —— 一行算出一致性分数 κ
from sklearn.metrics import cohen_kappa_score

human = ["ES", "CO", "ES", "TA"]   # 人工的判断
llm   = ["ES", "CO", "TA", "TA"]   # LLM的判断
kappa = cohen_kappa_score(human, llm)
print(kappa)
传进去两串判断(等长),它直接吐出一个数(κ 值)。你不用自己建矩阵、算 po/pe,它内部全做完了。
κ 的含义简单记:越接近 1,两人越一致;0 表示跟瞎猜一样;负数表示比瞎猜还差。 项目里一般要 κ ≥ 0.7 才算通过。


② confusion_matrix(a, b, labels=...) —— 一行建出混淆矩阵
from sklearn.metrics import confusion_matrix

human = ["ES", "CO", "ES", "TA"]
llm   = ["ES", "CO", "TA", "TA"]
cm = confusion_matrix(human, llm, labels=["ES", "CO", "TA"])
print(cm)
你上一个知识点用 zip 循环手工建的那张表,这个函数一行就建好了。

第一个参数 = 人工(行)
第二个参数 = LLM(列)
labels=[...] = 指定类别顺序(表的行列按这个顺序排)


那既然有现成函数,前面手工建表白学了吗?
没有。两个原因:

gwet_ac1 这个指标 sklearn 没有现成函数,项目里必须自己手写(下一步综合练习就写它),手写就要靠你前面学的 np.sum、trace、边际概率。
懂了内部原理,你才知道这个 κ 数字是怎么来的、为什么低,不是黑箱。

sklearn 版是「日常快速用」,手写版是「没有现成的只能自己写 + 真正理解」。项目里两种都出现了。

一句话规则:cohen_kappa_score(人工, LLM) 一行出 κ 分数;confusion_matrix(人工, LLM, labels=[...]) 一行出混淆矩阵。都是现成工具,直接调。


"""

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

from sklearn.metrics import cohen_kappa_score
from sklearn.metrics import confusion_matrix
kappa = cohen_kappa_score(human, llm)
cm    = confusion_matrix(human, llm, labels=["yes", "no"])
print(kappa)
print(cm)
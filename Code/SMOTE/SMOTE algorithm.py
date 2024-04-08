import numpy as np
from sklearn.neighbors import NearestNeighbors

def SMOTE(TMIN, TMAJ, N, t, k):
    TSMOTE = []  # 初始化SMOTE后的训练集
    for p in TMIN:
        TNN = NearestNeighbors(n_neighbors=k+1).fit(TMIN).kneighbors([p])[1][0][1:]  # 找到p的k个最近邻
        for i in range(N):
            v = TNN[np.random.randint(0, k)]  # 随机选择一个最近邻v
            s = create_new_string(p, v, t)  # 创建新样本s
            TSMOTE.append(s)  # 将新样本添加到TSMOTE中
        TSMOTE.append(p)  # 将原始样本p也添加到TSMOTE中
    TSMOTE += TMAJ  # 将TMAJ中的样本也添加到TSMOTE中
    return TSMOTE

def create_new_string(p, v, t):
    s = []  # 初始化新样本s
    for i in range(len(p)):
        if np.random.random() < t:
            s.append(p[i])
        else:
            s.append(v[i])
    return s

# 示例用法
TMIN = [[1, 2, 3], [2, 3, 4], [3, 4, 5]]
TMAJ = [[5, 6, 7], [6, 7, 8], [7, 8, 9]]
N = 5
t = 0.5
k = 3
TSMOTE = SMOTE(TMIN, TMAJ, N, t, k)
print(TSMOTE)

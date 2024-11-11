import numpy as np
def gaussian_elimination(A, b):
    n = len(A)
 
    # 将数组的数据类型转换为float64
    A = A.astype(np.float64)
    b = b.astype(np.float64)
 
    # 高斯消元
    for i in range(n - 1):
        max_idx = i
 
        # 选取列主元
        for j in range(i + 1, n):
            if abs(A[j][i]) > abs(A[max_idx][i]):
                max_idx = j
 
        # 交换行
        A[[i, max_idx]] = A[[max_idx, i]]
        b[[i, max_idx]] = b[[max_idx, i]]
 
        for j in range(i + 1, n):
            # 计算倍数
            multiplier = A[j][i] / A[i][i]
 
            # 更新矩阵
            A[j][i:] -= multiplier * A[i][i:]
            b[j] -= multiplier * b[i]
 
    # 回代求解
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (b[i] - np.dot(A[i][i + 1:], x[i + 1:])) / A[i][i]
 
    return x
 
 
# 示例
# A = np.array([[1.1348, 3.8326, 1.1651,3.4017], [0.5301, 1.7875, 2.5330,1.5435], [3.4129, 4.9317, 8.7643,1.3142],[1.2371,4.9998,10.6721,0.0147]])
 
# b = np.array([9.5342, 6.3941, 18.4231,16.9237])
A=np.array([[10,-1,-2],[-1,10,-2],[-1,-1,5]])
b=np.array([7.2,8.3,4.2])
 
x = gaussian_elimination(A, b)
print("解：", x)
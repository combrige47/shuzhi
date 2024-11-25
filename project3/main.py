import numpy as np
def Jacobi(A, b, max_iter=100, err=1e-3):
    n = len(b)
    x = np.zeros(n)  # 初始解
    x_new = np.zeros(n)  # 存储更新后的解向量
    for iter in range(max_iter):
        for i in range(n):
            sum_ax = np.dot(A[i], x) - A[i][i] * x[i]  # 计算除去对角元素的和
            x_new[i] = (b[i] - sum_ax) / A[i][i]  # 更新解向量的第i个分量
        # 判断终止条件
        if np.linalg.norm(x_new - x) < err:
            break
 
        x = np.copy(x_new)  # 更新解向量
        print(f"第{iter+1}次迭代: x = {x}")
    return x
A=np.array([[10,-1,-2],[-1,10,-2],[-1,-1,5]])
b=np.array([7.2,8.3,4.2])

x=Jacobi(A,b)
print("解:","x1=",x[0],"x2=",x[1],"x3=",x[2])
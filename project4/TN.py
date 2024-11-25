import numpy as np
import math
def compute_Tn(func, x_min=0, x_max=1, epoch=100,n=0,err=1e-6):
    Tn_list = []
    Tn = 0
    h0 = x_max - x_min  
    h = h0  
    x_half_list = np.array([0])  

    for k in range(epoch + 1):
        if k == 0:  
            Tn = 0.5 * h * (func(x_min,n) + func(x_max,n))  
            Tn_list.append(Tn.item())
            x_half_list = np.array([(x_min + x_max) / 2]) 
        else:
            Tn = 0.5 * Tn + 0.5 * h * np.sum(func(x_half_list,n))  
            Tn_list.append(Tn.item())
            h = 0.5 * h  
            x_half_list = np.linspace(0, 2 ** k, 2 ** k, endpoint=False) 
            x_half_list = h0 * (2 * x_half_list + 1) / (2 ** (k + 1)) + x_min  
            if(abs(Tn_list[-1]-Tn_list[-2]))<err: 
                break   
    return Tn_list[-1]



def f(x,n):
    y = np.exp(x-1)*np.power(x,n)
    if not isinstance(y, np.ndarray):
        y = np.array([y])
    y[np.where(np.isnan(y))] = 1
    return y

if __name__ == '__main__':
    for n in range(0,10):
        Tn_list = compute_Tn(f, x_min=0, x_max=1,n=n,err=1e-6)
        print("积分值为：",Tn_list,"n为",n)
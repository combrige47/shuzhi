import numpy as np
import math

def compute_Tn(func, x_min=0, x_max=1, epoch=100,n=0):
    Tn_list = []
    Tn = 0
    h0 = x_max - x_min  
    h = h0  
    x_half_list = np.array([0]) 

    for k in range(epoch + 1):
        if k == 0:  
            Tn = 0.5 * h * (func(x_min,n) + func(x_max,n))  
            Tn_list.append({"T_%d" % 2 ** k: Tn.item(), "k": k})
            x_half_list = np.array([(x_min + x_max) / 2])  
        else:
            Tn = 0.5 * Tn + 0.5 * h * np.sum(func(x_half_list,n))  
            Tn_list.append({"T_%d" % 2 ** k: Tn.item(), "k": k})
            h = 0.5 * h 
            x_half_list = np.linspace(0, 2 ** k, 2 ** k, endpoint=False)  
            x_half_list = h0 * (2 * x_half_list + 1) / (2 ** (k + 1)) + x_min 
    return Tn_list


def compute_Sn(Tn_list):
    Sn_list = []
    for i in range(len(Tn_list) - 1):
        Sn = list(Tn_list[i + 1].values())[0] * 4 / 3 - list(Tn_list[i].values())[0] / 3
        k = list(Tn_list[i + 1].values())[1]
        Sn_list.append({"S_%d" % 2 ** (k - 1): Sn, "k": k})
    return Sn_list

def compute_Cn(Tn_list=None, Sn_list=None):
    if Sn_list is None:
        Sn_list = compute_Sn(Tn_list)
    Cn_list = []
    for i in range(len(Sn_list) - 1):
        Cn = list(Sn_list[i + 1].values())[0] * 16 / 15 - list(Sn_list[i].values())[0] / 15
        k = list(Sn_list[i + 1].values())[1]
        Cn_list.append({"C_%d" % 2 ** (k - 2): Cn, "k": k})
    return Cn_list

def compute_Rn(Tn_list=None, Cn_list=None):
    if Cn_list is None:
        Cn_list = compute_Cn(Tn_list)
    Rn_list = []
    for i in range(len(Cn_list) - 1):
        Rn = list(Cn_list[i + 1].values())[0] * 64 / 63 - list(Cn_list[i].values())[0] / 63
        k = list(Cn_list[i + 1].values())[1]
        Rn=Rn
    return Rn
def sinx_div_x(x,n):
    y = np.exp(x-1)*np.power(x,n)
    if not isinstance(y, np.ndarray):
        y = np.array([y])
    y[np.where(np.isnan(y))] = 1
    return y

if __name__ == '__main__':
    for n in range(0,10):
        Tn_list = compute_Tn(sinx_div_x, x_min=0, x_max=1, epoch=24,n=n)
        Sn_list = compute_Sn(Tn_list)
        Cn_list = compute_Cn(Sn_list=Sn_list)
        Rn = compute_Rn(Cn_list=Cn_list)
        print("积分值为：",Rn,"n为",n)


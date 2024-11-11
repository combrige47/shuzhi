
#导入库
from math import *
import time
import numpy as np
import matplotlib.pyplot as plt
from pylab import mpl
 
 
print('两点插值的采样数据：')
x_samples_dot2 = [1, 2]#创建x列表存储数据x值
y_samples_dot2 = [4, 8]#创建y列表存储数据的y值
print("X:", x_samples_dot2)
print("Y:", y_samples_dot2)
plt.scatter(x_samples_dot2, y_samples_dot2, label="sample", color="black")
plt.plot   (x_samples_dot2, y_samples_dot2, label="sample", color="red")
 
mpl.rcParams['font.sans-serif'] = ['SimHei'] #设置中文字体
mpl.rcParams['axes.unicode_minus'] = False
plt.title("Dot2 采样数据")
plt.legend(loc="upper left")
plt.show()
# 插值基函数
#L0(x) = y0 * (x-x1)/(x0-x1)
def Dot2_L0(x, x_data,y_data):
    return (y_data[0] * (x-x_data[1])/(x_data[0]-x_data[1]))
 
#L1(x) = y1 * (x-x0)/(x1-x0)
def Dot2_L1(x, x_data,y_data):
    return (y_data[1] * (x-x_data[0])/(x_data[1]-x_data[0]))
 
# 插值函数：是基函数的线性叠加
def Dot2_F(x, x_data, y_data):
    return (Dot2_L0(x, x_data,y_data) + Dot2_L1(x, x_data,y_data))
 
 
#基函数的预测
#输入x数据序列
x_data_predict_dot2 = np.arange(0, 3, 0.2)
 
#基函数L0的预测序列
y_data_predict_dot2_L0 = Dot2_L0(x_data_predict_dot2, x_samples_dot2, y_samples_dot2)
 
#基函数L1的预测序列
y_data_predict_dot2_L1 = Dot2_L1(x_data_predict_dot2, x_samples_dot2, y_samples_dot2)
 
#插值函数的预测序列
y_data_predict_dot2_F = Dot2_F(x_data_predict_dot2, x_samples_dot2, y_samples_dot2)
 
 
#显示基函数与插值函数的图形
plt.scatter(x_samples_dot2, y_samples_dot2, label="sample", color="black")#画点
plt.plot   (x_data_predict_dot2, y_data_predict_dot2_L0, label="L0(x)", color="green")
plt.plot   (x_data_predict_dot2, y_data_predict_dot2_L1, label="L1(x)", color="blue")#画点
plt.plot   (x_data_predict_dot2, y_data_predict_dot2_F, label="f(x)", color="red")#画点
 
#设置属性
mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False
plt.title("Dot2 拉格朗日插值拟合过程")
plt.legend(loc="upper left")
plt.show()
print('三点插值的采样数据：')
x_samples_dot3 = [1, 2, 3]#创建x列表存储数据x值
y_samples_dot3 = [4, 8, 6]#创建y列表存储数据的y值
print("X:", x_samples_dot3)
print("Y:", y_samples_dot3)
plt.scatter(x_samples_dot3, y_samples_dot3, label="sample", color="black")#画点
plt.plot   (x_samples_dot3, y_samples_dot3, label="sample", color="red")#画点
 
plt.title("Dot3 采样数据")
plt.legend(loc="upper left")
plt.show()
# 基函数
#L0(x) = y0 * ((x-x1)*(x-x2))/((x0-x1)*(x0-x2))
def Dot3_L0(x, x_data,y_data):
    return (y_data[0] * ((x-x_data[1]) * (x-x_data[2]))/((x_data[0]-x_data[1]) * (x_data[0]-x_data[2])))
 
#L1(x) = y1 * ((x-x0)*(x-x2))/((x1-x0)*(x1-x2))
def Dot3_L1(x, x_data,y_data):
    return (y_data[1] * ((x-x_data[0]) * (x-x_data[2]))/((x_data[1]-x_data[0]) * (x_data[1]-x_data[2])))
 
#L0(x) = y2 * ((x-x0)*(x-x1))/((x2-x0)*(x2-x1))
def Dot3_L2(x, x_data,y_data):
    return (y_data[2] * ((x-x_data[0]) * (x-x_data[1]))/((x_data[2]-x_data[0]) * (x_data[2]-x_data[1])))
 
#插值函数：是基函数的线性叠加
def Dot3_F(x, x_data, y_data):
    return (Dot3_L0(x, x_data,y_data) + Dot3_L1(x, x_data,y_data) + Dot3_L2(x, x_data,y_data))
 
 
##函数的预测：输入数据序列为x
x_data_predict_dot3 = np.arange(0, 4.2, 0.2)
 
#基函数L0的预测序列
y_data_predict_dot3_L0 = Dot3_L0(x_data_predict_dot3, x_samples_dot3, y_samples_dot3)
 
#基函数L1的预测序列
y_data_predict_dot3_L1 = Dot3_L1(x_data_predict_dot3, x_samples_dot3, y_samples_dot3)
 
#基函数L2的预测序列
y_data_predict_dot3_L2 = Dot3_L2(x_data_predict_dot3, x_samples_dot3, y_samples_dot3)
 
#插值函数的预测序列
y_data_draw_dot3_F     = Dot3_F (x_data_predict_dot3, x_samples_dot3, y_samples_dot3)
 
 
#显示基函数与插值函数的关系
plt.scatter(x_samples_dot3, y_samples_dot3, label="sample", color="black")
plt.plot   (x_data_predict_dot3, y_data_predict_dot3_L0, label="L0(x)", color="green")
plt.plot   (x_data_predict_dot3, y_data_predict_dot3_L1, label="L1(x)", color="blue")
plt.plot   (x_data_predict_dot3, y_data_predict_dot3_L2, label="L2(x)", color="Orange")
plt.plot   (x_data_predict_dot3, y_data_draw_dot3_F, label="f(x)", color="red")
 
#设置属性
#mpl.rcParams['font.sans-serif'] = ['SimHei']
#mpl.rcParams['axes.unicode_minus'] = False
plt.title("Dot3 拉格朗日插值拟合过程")
plt.legend(loc="upper left")
plt.show()

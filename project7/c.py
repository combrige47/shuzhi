import numpy as np
from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt

def read_tsp(path):
    lines = open(path, 'r').readlines()
    assert 'NODE_COORD_SECTION\n' in lines
    index = lines.index('NODE_COORD_SECTION\n')
    data = lines[index + 1:-1]
    datax = []
    datay= []
    tmp = []
    ymp = []
    for line in data:
        line = line.strip().split(' ')
        if line[0] == 'EOF':
            continue
        tmpline = []
        tmpline.append(float(line[1]))
        tmpline.append(float(line[2]))
        tmp.append(tmpline)
        datax=tmp
    data=datax+datay
    return data
data=read_tsp('project7\data.la')
datax = []
datay = []
for x in data:
    datax.append(x[0])
    datay.append(x[1])

# 输入数据点
x = np.array(datax)
y = np.array(datay)

# 目标插值点
insert_x=[2,4,6,12,16,30,60,110,180,280,400,515]
x_interp = np.array(insert_x)
# 执行三次样条插值
cs = CubicSpline(x, y)
y_interp = cs(x_interp)
for i in range(len(x_interp)):
    print("横坐标:",x_interp[i],"预测纵坐标:",y_interp[i])

# 绘制原始数据点和插值结果
plt.xlim((0, 550))
plt.ylim((-100, 100))
plt.scatter(x, y, color='red', label='Original Data')
plt.plot(x_interp, y_interp, label='Cubic Spline')
plt.legend()
plt.show()
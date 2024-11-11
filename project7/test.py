
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator
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
    for line in data:
        line = line.strip().split(' ')
        if line[0] == 'EOF':
            continue
        tem=[]
        tem.append(float(line[1]))
        tem.append(-float(line[2]))
        ymp.append(tem)
        datay=ymp
    data=datax+datay
    return data
data=read_tsp('project7\data.la')

data = np.array(data)
print(data)

x_major_locator=MultipleLocator(50)
#把x轴的刻度间隔设置为1，并存在变量里
y_major_locator=MultipleLocator(30)
#把y轴的刻度间隔设置为10，并存在变量里
ax=plt.gca()
#ax为两条坐标轴的实例
ax.xaxis.set_major_locator(x_major_locator)
#把x轴的主刻度设置为1的倍数
ax.yaxis.set_major_locator(y_major_locator)
#把y轴的主刻度设置为1的倍数


plt.plot(data[:, 0], data[:, 1])
plt.xlim((0, 550))
plt.ylim((-225, 225))
plt.show()
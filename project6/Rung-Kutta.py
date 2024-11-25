import matplotlib.pyplot as plt
import numpy as np
def eluer(rangee,h,fun,x0,y0):
    step = int(rangee/h)
    x = [x0] + [h * i for i in range(step)]
    u = [y0] + [0     for i in range(step)]
    for i in range(step):
        u[i+1] = u[i] + h * fun(x[i],u[i])
    plt.plot(x,u,label = "eluer")
    return u
t = 0.
dt = .1
ts =  []
def func(y, t):
    return t * math.sqrt(y)
while t <= 10:
    t += dt
    ts.append(t)
rangee = 10
fun = lambda x,y:y-2*x/y
exact = [(t ** 2 + 4) ** 2 / 16. for t in ts]
plt.plot(ts, exact, label='exact')
eluer(rangee,0.1,fun,0,1)
plt.legend()
plt.show()
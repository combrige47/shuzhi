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
rangee = 1
fun = lambda x,y:y-2*x/y
 
# implicit_euler(rangee,0.0001,fun,0,1)
# order_4_runge_kutta(rangee,0.0001,fun,0,1)
# order_3_runge_kutta(rangee,0.0001,fun,0,1)
eluer(rangee,0.1,fun,0,1)
plt.legend()
plt.show()
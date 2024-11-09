import numpy as np
import math
x=1-np.exp(-1)
def f(x,n):
    return 1-n*x
for i in range(1,11):
    print(x,i)
    x=f(x,i)


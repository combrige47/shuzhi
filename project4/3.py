import numpy as np
import math
x=100
def f(x,n):
    return (1-x)/n
for i in range(50,1,-1):
    print(x,i)
    x=f(x,i)
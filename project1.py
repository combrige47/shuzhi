import math  

def f(x):  
    return 8 * math.exp(1 - x) + 7 * math.log(x)  

def golden_section_search(a=0.1, b=5, tol=0.23):  
    r = (math.sqrt(5) - 1) / 2  #黄金分割率
    c = b - r * (b - a)  
    d = a + r * (b - a)     
    fc = f(c)  
    fd = f(d)      
    while (b - a) > tol:  
        if fc < fd:  
            b = d  
            d = c  
            fd = fc  
            c = b - r * (b - a)  
            fc = f(c)  
        else:  
            a = c  
            c = d  
            fc = fd  
            d = a + r * (b - a)  
            fd = f(d)  
        print("a=", a, "b=",b)
    return (a + b) / 2  

res=golden_section_search()
print(res)
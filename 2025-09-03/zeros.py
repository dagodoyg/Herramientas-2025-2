import math as m

def fun(x):
    return x**2 - 2

def bisection(a: float, b: float, eps: float):
    m = (a + b)/2
    while abs(fun(m)) > eps:
        if fun(m)*fun(b) < 0:
            a = m
            m = (m + b)/2
        else:
            b = m
            m = (m + a)/2
    return m

print(bisection(1,2,0.0001)) 
print(m.sqrt(2))

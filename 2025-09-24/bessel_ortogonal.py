import numpy as np
import matplotlib.pyplot as plt
import scipy as sci

roots0 = sci.special.jn_zeros(0,11)
def fun(x, n, m):
    return x*sci.special.jn(0,x*roots0[n])*sci.special.jn(0,x*roots0[m])

def simpson(a, b, fun, n):
    h = (b-a)/n
    result = fun(a) + fun(b)
    for ii in range(1,n):
        if ii%2!=0:
            result += 4*fun(a + ii*h)
        else:
            result += 2*fun(a + ii*h)
    return (h/3)*result

X = np.linspace(0,1,1000)
M = np.zeros((11,11))

fl = lambda x: fun(x, n, m)
for n in range(0,11):
    for m in range(0,11):
        M[n][m] = sci.integrate.quad(fl, 0, 1)[0]

print(M)

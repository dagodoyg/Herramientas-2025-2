import numpy as np
import matplotlib.pyplot as plt

def fun(x, t):
    return 1.0/np.sqrt((1.0-(x*np.sin(t))**2))

def simpson(a, b, fun, n):
    h = (b-a)/n
    result = fun(a) + fun(b)
    for ii in range(1,n):
        if ii%2!=0:
            result += 4*fun(a + ii*h)
        else:
            result += 2*fun(a + ii*h)
    return (h/3)*result

K = []
X = []

fl = lambda t : fun(x,t)
for x in np.linspace(0,0.999,1000):
    K.append(simpson(0,np.pi/2,fl,100))
    X.append(x)

plt.ylabel(r'$K(x)$', size = 15)
plt.xlabel(r'$x$', size = 15)
plt.plot(X,K)
plt.show()

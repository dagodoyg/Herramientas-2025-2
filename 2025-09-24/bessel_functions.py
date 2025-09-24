import numpy as np
import matplotlib.pyplot as plt

def fun(x, n, t):
    return (1/np.pi)*np.cos(n*t - x*np.sin(t))

def simpson(a, b, fun, n):
    h = (b-a)/n
    result = fun(a) + fun(b)
    for ii in range(1,n):
        if ii%2!=0:
            result += 4*fun(a + ii*h)
        else:
            result += 2*fun(a + ii*h)
    return (h/3)*result

X = np.linspace(0,10,200)
N = [0,1,2,3]

fl = lambda t : fun(x, n, t)
for n in N:
    Y = []
    for x in X:
        Y.append(simpson(0,np.pi,fl,101))
    plt.plot(X, Y, label = f'n={n}')

plt.ylabel(r'$J_n(x)$', size = 15)
plt.xlabel(r'$x$', size = 15)
plt.xlim([0,10])
plt.legend()
plt.show()

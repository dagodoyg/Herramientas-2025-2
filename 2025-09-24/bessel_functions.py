import numpy as np
import matplotlib.pyplot as plt
import scipy as sci

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

X = np.linspace(0,20,1000)

#fl = lambda t : fun(x, n, t)
#for n in range(0,4):
#    Y = []
#    for x in X:
#        Y.append(simpson(0,np.pi,fl,1000))
#    plt.plot(X, Y, label = f'n={n}')
#
#plt.ylabel(r'$J_n(x)$', size = 15)
#plt.xlabel(r'$x$', size = 15)
#plt.xlim([0,10])
#plt.legend()
#plt.grid()
#plt.show()

for n in range(0,1):
    Y = sci.special.jn(n,X)
    K = sci.special.jn_zeros(n, 6)
    plt.plot(X, Y, '-', label = f'true n={n}')
    plt.plot(K, np.zeros(6), 'kx')

plt.ylabel(r'$J_n(x)$', size = 15)
plt.xlabel(r'$x$', size = 15)
plt.xlim([0,20])
plt.legend()
plt.grid()
plt.show()

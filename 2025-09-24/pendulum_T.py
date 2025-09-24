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
phi0 = np.linspace(0,np.pi-0.01,200)
X = np.sin(phi0/2)

fl = lambda t : fun(x,t)
for x in X:
    K.append(simpson(0,np.pi/2,fl,101))

K = np.array(K)
Y = (2/np.pi)*K
phi0 = phi0*180/(2*np.pi)

plt.ylabel(r'$\frac{T}{T*}(phi0)$', size = 15)
plt.xlabel(r'$phi0$', size = 15)
plt.xlim([0,20])
plt.plot(phi0,Y)
plt.show()

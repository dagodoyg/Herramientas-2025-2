import numpy as np
import matplotlib.pyplot as plt

def fun(x):
    return (1/np.sqrt(2*np.pi))*np.exp((-1/2)*x**2)

def step(a, b, fun):
    return ( b - a )*( fun(a) + fun(b) )/2

def integral_trap(a, b, fun, n):
    result = 0
    h = (b-a)/n
    for ii in range(0,n):
        result += step(a + ii*h, a + (ii + 1)*h, fun)
    return result

G = []
Z = []
for z in np.linspace(-20,20,100):
    g = integral_trap(0, z, fun, 10000)
    Z.append(z)
    G.append(g)

plt.plot(Z,G)
plt.xlabel(r'$z$', size = 15)
plt.ylabel(r'$g(z)$', size = 15)
plt.show()

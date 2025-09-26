import numpy as np
import scipy as sci
import matplotlib.pyplot as plt

def green_fun(x, z):
    if z < x:
        return (x - 1)*z
    else:
        return (z - 1)*x

def phi(z, alpha):
    return alpha*z**2

X = np.linspace(0,1,1000)
Z = []
alphas = [0, 0.2, 0.4, 0.6, 0.8, 1]

fl = lambda z : phi(z, alpha) * green_fun(x, z)
for alpha in alphas:
    Y = []
    for x in X:
        Y.append(sci.integrate.quad(fl, 0, 1)[0])
    plt.plot(X, Y, label = r'${\alpha}$' + f'={alpha}')

plt.legend()
plt.xlim([0,1])
plt.ylim([-0.1,0.1])
plt.show()

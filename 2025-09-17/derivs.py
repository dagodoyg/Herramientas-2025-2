import numpy as np
import matplotlib.pyplot as plt
import math as m

def fun(x):
    return m.sin(x)

def deriv_step(fun, x, h):
    return (fun(x+h) - fun(x))/h

H = [1e-2, 1e-3, 1e-4]
x = np.linspace(0,4*np.pi,num = 1000)
Z = np.cos(x)

for h in H:
    Y = []
    for t in x:
        Y.append(deriv_step(fun, t, h))
    plt.plot(x, Y, '--' ,label = f'h={h}')

plt.plot(x, Z, label = 'analitic')
plt.legend()
plt.show()

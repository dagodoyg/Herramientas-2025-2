import numpy as np
import matplotlib.pyplot as plt

pos = np.linspace(0, 5, 500)
a = []
x = np.zeros(500)
y = np.ones(500)
h = 0.01

def analitic(x):
    return (0.25)*(x + x**2 + 2)**2

def fun(x_i,y_i):
    return (1 + 2*x_i)*np.sqrt(y_i)

for ii in range(len(x)):
    k1 = fun(x[ii-1],y[ii-1])
    k2 = fun(x[ii-1] + h/2, y[ii-1] + (h/2)*k1)
    x[ii] = x[ii-1] + h
    y[ii] = y[ii-1] + h*k2

for p in pos:
    a.append(analitic(p))

plt.plot(pos, a, 'b-', label = 'analitic')
plt.plot(x, y, 'r--',label = 'numeric')
plt.xlabel('x')
plt.ylabel('y(x)')
plt.legend()
plt.show()

import numpy as np
import matplotlib.pyplot as plt

def fun(x_i,y_i):
    return (1 + 2*x_i)*np.power(y_i, np.sin(x_i*y_i), dtype = complex).real

def RK4(h, f, end):
    x = np.zeros(int(end/h))
    y = np.ones(int(end/h))
    for ii in range(len(x)):
        k1 = fun(x[ii-1],y[ii-1])
        k2 = fun(x[ii-1] + h/2, y[ii-1] + (h/2)*k1)
        k3 = fun(x[ii-1] + h/2, y[ii-1] + (h/2)*k2)
        k4 = fun(x[ii-1] + h, y[ii-1] + k3*h)
        x[ii] = x[ii-1] + h
        y[ii] = y[ii-1] + (h/6)*(k1 + 2*k2 + 2*k3 + k4) 
    return x,y

h = 0.001
x,y = RK4(h, fun, 5)
plt.plot(x, y, 'r--',label = f'h = {h}')

plt.xlabel('x')
plt.ylabel('y(x)')
plt.legend()
plt.show()

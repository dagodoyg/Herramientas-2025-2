import numpy as np
import matplotlib.pyplot as plt

g = 9.80665

def fun_x(t_i, x_i, y_i):
    return y_i

def fun_y(t_i, x_i, y_i):
    return (np.pi**2/12)**2*x_i*(np.sin(np.pi*t_i)**2) - g*np.sin((np.pi/12)*np.cos(np.pi*t_i))

def RK4(f,g,end):
    h = 0.01
    t = 0
    x = 0.75
    y = 0
    T = []
    X_RK4 = []
    Y_RK4 = []
    while t <= end:
        T.append(t)
        X_RK4.append(x)
        Y_RK4.append(y)
        k1x = f(t,x,y)
        k1y = g(t,x,y)
        k2x = f(t+h/2,x+k1x*h/2,y+k1y*h/2)
        k2y = g(t+h/2,x+k1x*h/2,y+k1y*h/2) 
        k3x = f(t+h/2,x+k2x*h/2,y+k2y*h/2)
        k3y = g(t+h/2,x+k2x*h/2,y+k2y*h/2)
        k4x = f(t+h,x+k3x*h,y+k3y*h)
        k4y = g(t+h,x+k3x*h,y+k3y*h)
        x = x + (k1x+2*k2x+2*k3x+k4x)*h/6
        y = y + (k1y+2*k2y+2*k3y+k4y)*h/6
        t = t + h
    return X_RK4, Y_RK4, T

x,_,t = RK4(fun_x, fun_y, 4)
plt.plot(t,x)
plt.axhline(y = 2, color = 'r')
plt.xlabel('t')
plt.ylabel('r(t)')
plt.show()

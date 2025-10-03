import numpy as np
import matplotlib.pyplot as plt

F = 1.0
b = 0.0011
w0 = 1
w = 1

def fun_x(t_i, x_i, y_i):
    return y_i

def fun_y(t_i, x_i, y_i):
    return F*np.sin(w*t_i) - x_i*(w0**2) - b*y_i 

def get_k(t, x, y, ii, fx, fy, h):
    kx = []
    ky = []
    kx.append(fx(t[ii-1],x[ii-1],y[ii-1]))
    ky.append(fy(t[ii-1],x[ii-1],y[ii-1]))
    kx.append(fx(t[ii-1] + h/2, x[ii-1] + (h/2)*kx[0], y[ii-1] + (h/2)*ky[0]))
    ky.append(fy(t[ii-1] + h/2, x[ii-1] + (h/2)*kx[0], y[ii-1] + (h/2)*ky[0]))
    kx.append(fx(t[ii-1] + h/2, x[ii-1] + (h/2)*kx[1], y[ii-1] + (h/2)*ky[1]))
    ky.append(fy(t[ii-1] + h/2, x[ii-1] + (h/2)*kx[1], y[ii-1] + (h/2)*ky[1]))
    kx.append(fx(t[ii-1] + h, x[ii-1] + h*kx[2], y[ii-1] + h*ky[2]))
    ky.append(fy(t[ii-1] + h, x[ii-1] + h*kx[2], y[ii-1] + h*ky[2]))
    return kx, ky

def RK4(h, fx, fy, end):
    t = np.zeros(int(end/h))
    x = np.zeros(int(end/h))
    y = np.zeros(int(end/h))
    x[0] = 0
    y[0] = 2
    for ii in range(1,len(x)):
        kx, ky = get_k(t,x,y,ii,fx,fy,h)
        t[ii] = t[ii-1] + h
        x[ii] = x[ii-1] + (h/6)*(kx[0] + 2*kx[1] + 2*kx[2] + kx[3])
        y[ii] = y[ii-1] + (h/6)*(ky[0] + 2*ky[1] + 2*ky[2] + ky[3]) 
    return x,y,t

x,y,t = RK4(0.001, fun_x, fun_y, 60)
plt.plot(t,x, label = 'posicion')
plt.plot(t,y, label = 'velocidad')
plt.legend()
plt.xlabel('t')
plt.ylabel('')
plt.show()

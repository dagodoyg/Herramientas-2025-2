import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def fun(t, y):
    eq1 = y[1]
    eq2 = -3*y[0]
    return [eq1,eq2] 

t_span = [0,2*np.pi]
t_eval = np.linspace(t_span[0], t_span[1], 1000)

def G(u):
    y0 = [0,u]    
    sol = solve_ivp(fun, t_span, y0, t_eval = t_eval)
    tmp = sol.y[0]
    return tmp[len(tmp) - 1]

a=-2
b=-1
for n in range(0,12):
    c=(a+b)/2
    if G(a)*G(c)<0:
        b=c
    else:
        a=c
    print(f'iter = {n}; c = {c}; G(c) = {G(c)}')

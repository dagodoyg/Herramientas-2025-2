import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

alpha = 0
beta = 4*np.pi**2
delta = 0.1*np.pi
gamma = 30*np.pi**2
omega = 2*np.pi

def fun(t,y):
    eq1 = y[1]
    eq2 = gamma*np.cos(omega*t) - delta*y[1] - alpha*y[0] - beta*y[0]**3
    return [eq1, eq2]

t_span = [0, 10000]
t_eval = np.linspace(t_span[0], t_span[1], 10001)
y0 = [1, 0]

sol = solve_ivp(fun, t_span, y0, t_eval = t_eval)

plt.plot(sol.y[0], sol.y[1], 'k.', markersize = 0.5)
plt.xlabel('x')
plt.ylabel('v')
plt.show()

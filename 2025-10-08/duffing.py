import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

alpha = -1
beta = 0.25
delta = 0.1
gamma = 2.5
omega = 2

def fun(t,y):
    eq1 = y[1]
    eq2 = gamma*np.cos(omega*t) - delta*y[1] - alpha*y[0] - beta*y[0]**3
    return [eq1, eq2]

t_span = [0, 50]
t_eval = np.linspace(t_span[0], t_span[1], 1000)
y0 = [0, 0.1]

sol = solve_ivp(fun, t_span, y0, t_eval = t_eval)

plt.plot(sol.t, sol.y[0])
plt.xlabel('t')
plt.ylabel('x(t)')
plt.show()

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

g = 9.80665

def fun(t, y):
    eq1 = y[1]
    eq2 = (np.pi**2/12)**2*y[0]*(np.sin(np.pi*t)**2) - g*np.sin((np.pi/12)*np.cos(np.pi*t))
    return [eq1, eq2]

t_span = [0,5]
t_eval = np.linspace(t_span[0], t_span[1], 100)
y0 = [0.75,0]

sol = solve_ivp(fun,t_span,y0, t_eval=t_eval)

plt.plot(sol.t, sol.y[0])
plt.xlabel('t')
plt.ylabel('r(t)')
plt.show()

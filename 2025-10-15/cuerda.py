import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def fun(t, y, k):
    eq1 = y[1]
    eq2 = -k**2*y[0]
    return [eq1,eq2] 

t_span = [0,2*np.pi]
t_eval = np.linspace(t_span[0], t_span[1], 1000)

def G(u,k):
    y0 = [0,u]
    f = lambda t,y: fun(t,y,k)
    sol = solve_ivp(f, t_span, y0, t_eval = t_eval)
    tmp = sol.y[0]
    return tmp[len(tmp) - 1]

N = 50
U = np.linspace(-3,3,N)
K = np.linspace(-3,3,N)
S = []
for u in U:
    s = []
    for k in K:
        s.append(G(u,k))
    S.append(np.array(s))

M = np.zeros([N,N])
for ii in range(0,N):
    for jj in range(0,N):
       if np.abs(S[ii][jj]) < 1e-3:
            M[ii][jj] = 1

plt.ylabel('u')
plt.xlabel('k')
plt.imshow(M)
#plt.colorbar()
plt.show()

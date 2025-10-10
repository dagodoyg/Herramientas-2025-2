import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

N = 20
matA = np.ones([N,N])
for n in range(0,N):
    matA[n][n] = 0
phase_0 = np.random.uniform(0,2*np.pi, N)

def fun(t, theta):
    tmp = np.zeros(N)
    for ii in range(0,N):
        tmp[ii] = np.sum(matA[ii][jj]*np.sin(theta[jj]-theta[ii]) for jj in range(0,N)) 
    return tmp

t_span = [0,10]
t_eval = np.linspace(t_span[0], t_span[1], 1000)
sol = solve_ivp(fun, t_span, phase_0, t_eval = t_eval)

#for ii in range(0,N):
#    plt.plot(sol.t, sol.y[ii])

#plt.xscale('log')
#plt.show()

theta = sol.y.T
r=[]
for m in theta:
    r.append(np.abs(sum(np.exp(1j*m)))/N)

plt.plot(sol.t,r)
plt.xlabel('t')
plt.ylabel('r(t)')
plt.xscale('log')
plt.show()

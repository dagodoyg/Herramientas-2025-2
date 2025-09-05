import numpy as np
import matplotlib.pyplot as plt

L = [[2,-1,-1],[-1,2,-1],[-1,-1,2]]

eigvals, Q = np.linalg.eig(L)
Qinv = np.linalg.inv(Q)

theta_1 = [] 
theta_2 = []
theta_3 = []
T = []

t = 0

def evolution(t):
    lam_f = np.diag(np.exp(-eigvals*t))
    return  np.matmul(np.matmul(Q,lam_f), np.linalg.inv(Q))

init = [np.pi/2, 5*np.pi/7, -3*np.pi/8]

while t <= 10:
    a,b,c = np.matmul(evolution(t), init)
    theta_1.append(a)
    theta_2.append(b)
    theta_3.append(c)
    T.append(t)
    t+=0.01

plt.plot(T,theta_1)
plt.show()


import numpy as np
import matplotlib.pyplot as plt

def get_stocastic(alpha):
    a = alpha / (1.0 + alpha)
    b = 1.0 / (1.0 + alpha) 
    return np.array([[a,b], [a,b]])

def error(A, B):
    return sum(np.abs((A-B).flatten()))

Xerr = []
param = []
alpha = 0
while alpha <= 100:
    W = get_stocastic(alpha)
    S = W + np.identity(2)

    eig_vals, Q = np.linalg.eig(S)
    Q_inv = np.linalg.inv(Q)
    lam_f = np.diag(np.log(eig_vals))

    left = np.matmul(np.matmul(Q,lam_f),Q_inv)
    right =  np.log(2)*W
    
    Xerr.append(error(left,right))
    param.append(alpha)

    alpha += 1

plt.plot(param, Xerr)
plt.show()

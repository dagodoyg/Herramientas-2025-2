import numpy as np

M = [[0,-1],[19/4,10]]
init = [-9,0]
eigvals, Q = np.linalg.eig(M)
t=0

def evolution(t):
    lam_f = np.diag(np.exp(-eigvals*t))
    return  np.matmul(np.matmul(Q,lam_f), np.linalg.inv(Q))
 
with open("data.txt", "w") as file:
    while t <= 10:
        a,b = np.matmul(evolution(t), init)
        file.write(str(a)+" "+str(b)+" "+str(t)+"\n")
        t += 0.01

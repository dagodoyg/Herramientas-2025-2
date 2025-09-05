import numpy as np
import matplotlib.pyplot as plt

A = [[2,3,-20],[3,np.pi,7],[-20,7,5]]

eig_vals, Q = np.linalg.eig(A)
lam = np.diag(eig_vals)

Z = np.matmul(A,Q)
S = np.matmul(Q,lam)
S_2 = np.matmul(S,np.linalg.inv(Q))

print(S-Z, "\n")
print(A-S_2, "\n")

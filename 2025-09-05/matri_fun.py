import numpy as np
import matplotlib.pyplot as plt

A = [[2,3,-20],[3,np.pi,7],[-20,7,5]]

eig_vals, Q = np.linalg.eig(A)
lam = np.diag(eig_vals)
Q_inv = np.linalg.inv(Q)

lam_f = np.diag(np.exp(-eig_vals))

np.matmul(np.matmul(Q,lam_f),Q_inv)

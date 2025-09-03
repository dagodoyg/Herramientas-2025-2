import numpy as np
import matplotlib.pyplot as plt

N = 1000
A = np.random.rand(N,N)
A_sim = (A + A.T)/2

eigen_vals = np.linalg.eigvals(A)
eigen_vals_sim = np.linalg.eigvals(A_sim)

x = np.real(np.real(eigen_vals)) 
y = np.real(np.imag(eigen_vals))

x_sim = np.real(np.real(eigen_vals_sim)) 
y_sim = np.real(np.imag(eigen_vals_sim))

plt.plot(x, y,"m.")
plt.plot(x_sim, y_sim, "b.")
plt.xlabel("real")
plt.ylabel("img")
plt.show()

import numpy as np
import matplotlib.pyplot as plt

def laplace_2D_sol(fun, x, y, h):
    eq1 = f(x+h,y) + f(x-h,y)
    eq2 = f(x,y+h) + f(x,y-h)
    return (1/4)*(eq1 + eq2)

X = np.linspace(0,1,101)
Y = np.linspace(0,1,101)

A,B = np.meshgrid(X,Y)
Psi = np.zeros(A.shape)

for ii in range(0,len(X)):
    Psi[ii][0] = 100*np.sin(2*np.pi*Y[ii])
    Psi[ii][len(X)-1] = -100*np.sin(2*np.pi*Y[ii])
    Psi[len(X)-1][ii] = -100*np.sin(2*np.pi*X[ii]) 
    Psi[0][ii] = 100*np.sin(2*np.pi*X[ii])

Phi = Psi.copy()
for n in range(0,5000):
    for ii in range(1,len(X)-1):
        for jj in range(1,len(Y)-1):
            Phi[jj][ii] = (1/4.0)*(Psi[jj-1][ii] + Psi[jj+1][ii] +
                                    Psi[jj][ii-1] + Psi[jj][ii+1])
    Psi = Phi.copy()

plt.imshow(Psi)
plt.xlabel('x')
plt.ylabel('y')
plt.colorbar()
plt.show()

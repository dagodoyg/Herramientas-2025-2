import numpy as np
import matplotlib.pyplot as plt
import scipy as sci

def fun(x, n, m, k, roots):
    return x*sci.special.jn(k,x*roots[n])*sci.special.jn(k,x*roots[m])

def get_ort_bessel(k):
    X = np.linspace(0,1,1000)
    M = np.zeros((11,11))
    roots = sci.special.jn_zeros(k,11)
    fl = lambda x: fun(x, n, m, k, roots)
    for n in range(0,11):
        for m in range(0,11):
            M[n][m] = sci.integrate.quad(fl, 0, 1)[0]
    return np.array(M)

K = 1
A = get_ort_bessel(K)
plt.imshow(A)
plt.title(f'k = {K}')
plt.show()

import numpy as np 
import matplotlib.pyplot as plt

def coin():
    a = np.random.rand()
    if a < 0.5:
        return -1
    else:
        return 1

for jj in range (2000):
    x = 0
    pos = []
    t = []
    for ii in range(1000):
        x += coin()
        pos.append(x)
        t.append(ii)
    plt.plot(t,pos,alpha=0.2)

plt.xlabel("steps")
plt.ylabel("x")
plt.show()
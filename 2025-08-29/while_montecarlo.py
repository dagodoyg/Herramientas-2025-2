import numpy as np

def MontecarloStep():
    x = np.random.rand()
    y = np.random.rand()
    if x**2 + y**2 <=1:
        return 1.0
    else:
        return 0.0


def MontecarloPrecision(eps):
    Nc = MontecarloStep()
    ii = 1
    d = np.abs(1.0 - 4*Nc/(ii*np.pi))

    while d > eps:
        ii += 1
        Nc += MontecarloStep()
        d = np.abs(1.0 - 4*Nc/(ii*np.pi))
        # print(d, "\n")
    return ii

print(MontecarloPrecision(0.1))
print(MontecarloPrecision(0.01))
print(MontecarloPrecision(0.001))

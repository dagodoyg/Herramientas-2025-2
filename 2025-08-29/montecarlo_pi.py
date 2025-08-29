import numpy as np

N = 1000000

def MontecarloPi(N):
    Nc = 0

    for i in range(N):
        x = np.random.rand()
        y = np.random.rand()
        if x**2 + y**2 <=1:
            Nc += 1

    # print("Montecarlo pi: ", 4*Nc/N)

    # d = 100*np.abs(1.0 - 4*Nc/(N*np.pi)) 
    # print("Delta: ", d)

    return 4*Nc/N


print(MontecarloPi(1),"\n")
print(MontecarloPi(10),"\n")
print(MontecarloPi(100),"\n")
print(MontecarloPi(1000),"\n")
print(MontecarloPi(10000),"\n")
print(MontecarloPi(100000),"\n")
print(MontecarloPi(10000000),"\n")
import numpy as np
import matplotlib.pyplot as plt
a = 0.04
b = 0.1
c = 0.005
e = 0.2

F = []
R = []
T = []

R.append(100)
F.append(20)
T.append(0)
for i in range(0,500):
    R.append(R[i] + a*R[i] - c*R[i]*F[i])
    F.append(F[i] + e*c*R[i]*F[i] - b*F[i])
    T.append(i)
plt.plot(T,R,"b", label="kaniner")
plt.plot(T,F,"r", label="rever")
plt.legend()
plt.xlabel("tid i uker")
plt.ylabel("antall dyr")
plt.show()

"""
Terminal>python .\lotka_volterra.py

"""

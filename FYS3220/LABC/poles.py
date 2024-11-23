import numpy as np
import matplotlib.pyplot as plt


R = 1e4
C = 10e-9
G = 4

a = 0
b = (R*C)/ (1 + G)
c = 1

poles = np.roots([a, b, c])
# print(poles)

omega = [0, 1 / (R*C), 1e200]

for o in omega:
    F = - G / (R * C * o * 1j + 1)
    print(F) 
import numpy as np

def my_convolve(a, b):
    # Convolve a and b
    c = np.zeros(len(a) + len(b) - 1)
    for i in range(len(a)):
        for j in range(len(b)):
            c[i + j] += a[i] * b[j]
    return c

a = np.array([1, 2, 3, 4,5])
b = np.array([3,6,9,7,3,1,0])
my = my_convolve(a, b)
num = np.convolve(a, b)

for i in range(len(my)):
    if abs(my[i] - num[i]) > 1e-6:
        print("Not equal")
        print(my[i], num[i])
        break
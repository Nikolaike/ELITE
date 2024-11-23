import numpy as np 


b = []

for n in range(1, 11):
    b.append(4/(n*np.pi) * (1 - np.cos(n*np.pi)))

print(b)

for i in range(1,11):
    print(500*i * 2* np.pi)

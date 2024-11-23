import numpy as np

x = [1, np.sqrt(2) / 2, 0, -np.sqrt(2) / 2, -1, -np.sqrt(2) / 2, 0, np.sqrt(2) / 2]

Xee = [x[0] + x[4], x[0] - x[4]]
Xoe = [x[1] + x[5], x[1] - x[5]]
Xeo = [x[2] + x[6], x[2] - x[6]]
Xoo = [x[3] + x[7], x[3] - x[7]]

k = [0, 1]

Xe = np.zeros(4, dtype=complex)
Xo = np.zeros(4, dtype=complex)

for i in k:
    
    Xe[i] = Xee[i] + np.exp(-1j * 2 * np.pi * (2 * i / 8)) * Xeo[i]
    Xe[i+2] = Xee[i] + np.exp(-1j * 2 * np.pi * (2 * i / 8)) * (-Xeo[i])

    Xo[i] = Xoe[i] + np.exp(-1j * 2 * np.pi * (2 * i / 8)) * Xoo[i]
    Xo[i + 2] = Xoe[i] + np.exp(-1j * 2 * np.pi * (2 * i / 8)) * (-Xoo[i])




k = [0, 1, 2, 3]

X = np.zeros(8, dtype = complex)
for i in k:
    X[i] = Xe[i] + np.exp(-1j * 2 * np.pi * (i / 8)) * Xo[i]
    X[i+4] = Xe[i] + np.exp(-1j * 2 * np.pi * (i / 8)) * (-Xo[i])


rounded_X = np.round(X, decimals=2)

x_fft = np.round(np.fft.fft(x))
print(rounded_X)
print(x_fft)


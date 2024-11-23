import numpy as np
import matplotlib.pyplot as plt

tau = 1e-4
G = 2.5
omega_0 = 1e4
Q = 20*np.log10(2)

omega = np.logspace(0, 6, 1000)

h = 20*np.log10(G * tau) + 20*np.log10(omega) - 40*np.log10(omega / omega_0)

plt.logplot(omega, h)
plt.scatter(omega_0, Q)
plt.show()
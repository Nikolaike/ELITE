import numpy as np
import matplotlib.pyplot as plt

# Constants
R = 10e3  # 10k Ohms
C = 10e-9  # 10n Farads
G = 4.0

# Angular frequency range
omega = np.logspace(0, 8, 500)

# Transfer function
s = 1j * omega  # j is the imaginary unit
H = (-G / (1 + G)) / ((R * C * s / (1 + G)) + 1)

# Nyquist plot
plt.figure()
plt.plot(-H.real, H.imag, label='Nyquist plot')
plt.plot(-H.real, -H.imag, linestyle='--', label='Mirror image')
plt.scatter([1], [0], color='red', zorder=5, label='Danger Limit (1, 0j)')
plt.xlabel('Real part')
plt.ylabel('Imaginary part')
plt.grid(True)
plt.legend()
plt.title('Nyquist Diagram')
plt.show()

import control as ctrl
import matplotlib.pyplot as plt
import numpy as np

# Constants
R = 10e3  # 10k Ohms
C = 10e-9  # 10n Farads
G = 2.2

# Create transfer function
numerator = [G * R * C, 0]
denominator = [R**2 * C**2, 3 * R * C - G * R * C, 1]

# numerator = [0, -G]
# denominator = [R*C / (1 + G), 1]
system = ctrl.TransferFunction(numerator, denominator)

# Nyquist plot
plt.figure()
ctrl.nyquist_plot(system, omega=np.logspace(0, 8, 500))
plt.xlabel('Real part')
plt.ylabel('Imaginary part')
plt.title('Nyquist Diagram using control library')
plt.legend()
plt.grid(True)
plt.show()

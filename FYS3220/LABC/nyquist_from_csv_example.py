import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sys

filename = sys.argv[1]

# Load the CSV file into a DataFrame


df = pd.read_csv(filename)

# Extract magnitude in dB and phase in degrees
magnitude_dB = df['DB(MAG(V(Out)))'].to_numpy()
phase_deg = df['PHDEG(V(Out))'].to_numpy()

# Convert to complex numbers
magnitude = 10 ** (magnitude_dB / 20)
phase_rad = np.radians(phase_deg)
H = magnitude * np.exp(1j * phase_rad)

# Nyquist plot
plt.figure()
plt.plot(H.real, H.imag, label='Nyquist plot')
plt.scatter([-1], [0], color='red', zorder=5, label='Danger Limit (-1, 0j)')
# plt.xlim(-4,4)
# plt.ylim(-4,4)
plt.xlabel('Real part')
plt.ylabel('Imaginary part')
plt.grid(True)
plt.legend()
plt.title('Nyquist Diagram from Bode Plot Data')
plt.show()
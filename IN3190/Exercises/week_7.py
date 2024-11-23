import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq


N = 1000
T = 0.01
t = np.linspace(0, T, N)
f = 500
f_s = 2000
t_s = np.arange(0, 0.01, T/f_s)


x_t = np.cos(2*f*np.pi*t)
x_s = np.cos(2*f*np.pi*t_s)

x_t_fft = fft(x_t)
x_t_freq = fftfreq(len(x_t), T/f_s)

x_s_fft = np.fft.fft(x_s)
x_s_freq = np.fft.fftfreq(len(x_s), T/f_s)

plt.figure(figsize=(12, 6))

# Amplitudespekter
plt.subplot(2, 1, 1)
plt.plot(x_t_freq, 2.0 / N * x_t_fft)
plt.title('Frekvensrespons (Amplitude)')
plt.xlabel('Frekvens (Hz)')
plt.ylabel('Amplitudeverdi')
plt.grid()
plt.xlim(-6000, 6000)
# Steg 5: Plot frekvensresponsens fase
plt.subplot(2, 1, 2)
plt.plot(x_s_freq, 2 / N * x_s_fft)
plt.title('Frekvensrespons (Fase)')
plt.xlabel('Frekvens (Hz)')
plt.ylabel('Fase (radianer)')
plt.grid()
plt.xlim(-6000, 6000)

plt.tight_layout()
plt.show()
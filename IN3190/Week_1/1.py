import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(-1.5, 2.5, 1000)

plt.subplot(4,1,1)
plt.plot(t, np.cos(2*np.pi*t), label='cos(2*pi*t)')
plt.xlabel('t')
plt.ylabel("Amplitude")
plt.legend()


plt.subplot(4,1,2)
plt.plot(t, np.cos(2*np.pi*t + np.pi), label='cos(2*pi*t + pi)')
plt.xlabel('t')
plt.ylabel("Amplitude")
plt.legend()

plt.subplot(4,1,3)
plt.plot(t, np.cos(8*np.pi*t), label='cos(8*pi*t)')
plt.xlabel('t')
plt.ylabel("Amplitude")
plt.legend()


plt.subplot(4,1,4) 
plt.plot(t, np.cos(4*np.pi*t - np.pi/3), label='cos(4*pi*t - pi/3)')
plt.xlabel('t')
plt.ylabel("Amplitude")
plt.legend()

plt.tight_layout()
plt.show()


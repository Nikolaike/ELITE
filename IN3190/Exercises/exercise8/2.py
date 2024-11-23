import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq, fftshift


def dft(x, tol=1e-10):
    N = len(x)
    X = [0] * N
    for k in range(N):
        for n in range(N):
            X[k] += x[n] * np.exp(-2j * np.pi * k * n / N)
            X[k] = np.round(X[k], 2)
  
    return X

# 1
# a) 
x1 = [1, 2, 1, 2]
X1 = dft(x1)
print(X1)
#Output: [(6+0j), (-0+0j), (-2-0j), 0j]

# b)
x2 = [2, 1, 3, 0, 4]
X2 = dft(x2)
print(X2)
#Output: [(10+0j), (1.12+1.09j), (-1.12+4.61j), (-1.12-4.61j), (1.12-1.09j)]

# c)
x3 = [2, 2, 2, 2]
X3 = dft(x3)
print(X3)
#Output: [(8+0j), (-0+0j), -0j, 0j]

# d)
x4 = [1, 0, 0, 0, 0, 0, 0, 0]
X4 = dft(x4)
print(X4)
#Output: [(1+0j), (1+0j), (1+0j), (1+0j), (1+0j), (1+0j), (1+0j), (1+0j)]

# 2
# Given signal parameters
F1 = 100  # Frequency of cosine component in Hz (200pi rad/s)
F2 = 150  # Frequency of sine component in Hz (300pi rad/s)
A = 5
B = 4
phi = np.pi / 6

# Sampling rates
F_T_list = [1000, 500, 100]  # Sampling frequencies in Hz

# Improved signal spectrum calculation

def signal_spectrum(x, F_T):
 
    # Perform FFT and shift zero frequency to center
    N = len(x)
    X = dft(x)
    X = fftshift(X) / N  # Normalize the FFT output

    # Create periodic copies of the spectrum
    X_periodic = np.tile(np.abs(X), 5)  # Create 5 copies of the spectrum
    freq_periodic = np.linspace(int(-2.5*F_T), int(2.5*F_T), len(X_periodic))

    # Plot the spectrum within the range -2F_T to 2F_T
    plt.figure(figsize=(10, 8))
    plt.subplot(2, 1, 1)
    plt.plot(freq_periodic, X_periodic, label=f"Spectrum (F_T = {F_T} Hz)")
    plt.xlim(-2 * F_T, 2 * F_T)
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("|X(F)|")
    plt.title(f"Frequency Spectrum with F_T = {F_T} Hz")
    plt.grid()
    plt.legend()

    # Plot normalized angular frequency
    omega = freq_periodic / F_T  # Normalized angular frequency
    plt.subplot(2, 1, 2)
    plt.plot(omega, X_periodic, label=f"Normalized Spectrum (F_T = {F_T} Hz)")
    plt.xlim(-2.5, 2.5)
    plt.xlabel("Normalized Angular Frequency (rad/sample)")
    plt.ylabel("|X(F)|")
    plt.title(f"Frequency Spectrum with Normalized Angular Frequency (F_T = {F_T} Hz)")
    plt.grid()
    plt.legend()

    plt.tight_layout()
    plt.show()

# Plotting the signal spectrum for different sampling rates
for F_T in F_T_list:
    # Time vector for one second
    t = np.arange(0, 1, 1/F_T)  # Use time vector for 1 second duration
    # Original signal
    x = A * np.cos(2 * np.pi * F1 * t + phi) + B * np.sin(2 * np.pi * F2 * t)
    signal_spectrum(x, F_T)


# 3
# a)
x1 = [1, -2, 1, -3]
x2 = [0, 2, -1, 0, 0, 4]

x3 = np.convolve(x1, x2)

print(x3)
#Output [  0   2  -5   4  -7   7  -8   4 -12]

#b)
def circular_convolution(x1, x2, N):
    y = np.zeros(N)
    for n in range(N):
        for k in range(N):
            y[n] += x1[k] * x2[(n - k) % N]
    return y

N = 6
x1_padded = np.pad(x1, (0, N - len(x1)), mode='constant')
x2_padded = np.pad(x2, (0, N - len(x2)), mode='constant')
x4 = circular_convolution(x1_padded, x2_padded, N)

print(x4)
#Output [ -8.   6. -17.   4.  -7.   7.]
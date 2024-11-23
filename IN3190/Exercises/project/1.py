import numpy as np
import matplotlib.pyplot as plt
import scipy.io


def convin3190(x, h, ylen):
    # Convolution of x and h
    # x: input signal
    # h: FIR filter
    # ylen: determine the length of the output signal, if ylen = 0, the length of the output signal is len(x)
    # if ylen is 1, the length of the output signal is len(x) + len(h) - 1
    # return: convolution of x and h

    if ylen == 0:
        y = np.zeros(len(x))
    elif ylen == 1:
        y = np.zeros(len(x) + len(h) - 1) 
    else:
        raise ValueError ('ylen must be 0 or 1') # raise an error if ylen is not 0 or 1
    for i in range(len(y)): 
        for j in range(len(h)):
            if i - j >= 0 and i - j < len(x): # check if the index is within the range of x
                y[i] += x[i - j] * h[j] # compute the convolution
    return y

# x = np.array([1, 2, 3, 4, 5])
# h = np.array([1, 2, 3])
# y = convin3190(x, h, 1)
# print(y)

# y = np.convolve(x, h)
# print(y)

def freqspecin3190(x, N, fs):
    # Compute the frequency spectrum of x
    # x: input signal
    # N: number of samples of the frequency spectrum
    # fs: sampling frequency
    # return: frequency spectrum X and frequency axis f
    n = len(x) 
    f = np.linspace(0, fs, N) # frequency axis
    X = np.zeros(N, dtype = complex) # frequency spectrum
    for i in range(N):
        for j in range(n):
            X[i] += x[j] * np.exp(-2j * np.pi * i * j / N) # compute the frequency spectrum
    X= X[:N//2] # only keep the first half of the frequency spectrum due to aliasing
    f = f[:N//2] # only keep the first half of the frequency axis due to aliasing
    return X, f

# Constants
f1 = 10 
f2 = 20
fs = 100
t = np.linspace(0, 5, 5 * fs)
x = np.sin(2 * np.pi * f1 *t ) + np.sin(2 * np.pi * f2 * t) # generate a signal with two frequencies

def h(n): # generate a FIR filter
    h = np.zeros(n)
    for i in range(n):
        h[i] = 1 / n
    return h

H, fh = freqspecin3190(h(5), 1000, fs) # compute the frequency spectrum of h
# plt.plot(fh, np.abs(H))
# plt.title('Frequency Spectrum of h')
# plt.xlabel('Frequency (Hz)')
# plt.ylabel('Magnitude')
# plt.show()


# X, fx = freqspecin3190(x, 1500, fs) # compute the frequency spectrum of x
# Y, fy = freqspecin3190(convin3190(x, h(5), 1), 1500, fs) # compute the frequency spectrum of the convolved signal



# fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

# # Plot the original signal's frequency spectrum
# ax1.plot(fx, np.abs(X))
# ax1.set_xlim(0, 30)
# ax1.set_title('Frequency Spectrum of signal X')
# ax1.set_xlabel('Frequency (Hz)')
# ax1.set_ylabel('Magnitude')

# # Plot the convolved signal's frequency spectrum
# ax2.plot(fy, np.abs(Y))
# ax2.set_xlim(0, 30)
# ax2.set_title('Frequency Spectrum of convolved signal Y')
# ax2.set_xlabel('Frequency (Hz)')
# ax2.set_ylabel('Magnitude')

# plt.tight_layout()
# plt.show()


# Generate two FIR filters
h1 = np.array([0.0002, 0.0001, -0.0001, -0.0005, -0.0011, -0.0017, -0.0019, -0.0016, -0.0005, 0.0015,
               0.0040, 0.0064, 0.0079, 0.0075, 0.0046, -0.0009, -0.0084, -0.0164, -0.0227, -0.0248,
               -0.0203, -0.0079, 0.0127, 0.0400, 0.0712, 0.1021, 0.1284, 0.1461, 0.1523, 0.1461,
               0.1284, 0.1021, 0.0712, 0.0400, 0.0127, -0.0079, -0.0203, -0.0248, -0.0227, -0.0164,
               -0.0084, -0.0009, 0.0046, 0.0075, 0.0079, 0.0064, 0.0040, 0.0015, -0.0005, -0.0016,
               -0.0019, -0.0017, -0.0011, -0.0005, -0.0001, 0.0001, 0.0002])

h2 = np.array([-0.0002, -0.0001, 0.0003, 0.0005, -0.0001, -0.0009, -0.0007, 0.0007, 0.0018, 0.0005,
               -0.0021, -0.0027, 0.0004, 0.0042, 0.0031, -0.0028, -0.0067, -0.0023, 0.0069, 0.0091,
               -0.0010, -0.0127, -0.0100, 0.0077, 0.0198, 0.0075, -0.0193, -0.0272, 0.0014, 0.0386,
               0.0338, -0.0246, -0.0771, -0.0384, 0.1128, 0.2929, 0.3734, 0.2929, 0.1128, -0.0384,
               -0.0771, -0.0246, 0.0338, 0.0386, 0.0014, -0.0272, -0.0193, 0.0075, 0.0198, 0.0077,
               -0.0100, -0.0127, -0.0010, 0.0091, 0.0069, -0.0023, -0.0067, -0.0028, 0.0031, 0.0042,
               0.0004, -0.0027, -0.0021, 0.0005, 0.0018, 0.0007, -0.0007, -0.0009, -0.0001, 0.0005,
               0.0003, -0.0001, -0.0002])



# Plot the FIR filters
# plt.plot(h1, label='h1')
# plt.plot(h2, label='h2')
# plt.title('FIR filters')
# plt.xlabel('t')
# plt.ylabel('Amplitude')
# plt.legend()
# plt.show()

# # Compute the frequency spectrum of the FIR filters
# H1, fh1 = freqspecin3190(h1, 1000, fs)
# H2, fh2 = freqspecin3190(h2, 1000, fs)

# # Plot the frequency spectrum of the FIR filters
# plt.plot(fh1, 20*np.log10(np.abs(H1)), label='H1')
# plt.title('Frequency Spectrum of h1')
# plt.xlabel('Frequency (Hz)')
# plt.ylabel('Magnitude')

# plt.plot(fh2, 20*np.log10(np.abs(H2)), label='H2')
# plt.title('Frequency Spectrum of h2')
# plt.xlabel('Frequency (Hz)')
# plt.ylabel('Magnitude')

# plt.legend()
# plt.tight_layout()
# plt.show()


hann = np.hanning(20)


# Load in .mat-file
mat_data = scipy.io.loadmat('31.mat')

# Get the data from the .mat-file
offset1 = mat_data['offset1'].flatten()  
offset2 = mat_data['offset2'].flatten() 
seismogram1 = mat_data['seismogram1']   
seismogram2 = mat_data['seismogram2']   
t = mat_data['t'].flatten()         


# for i in range(3):
#     plt.plot(t[:20], seismogram1[:20, i], label=f"Trace {i+1}  without windowing")
#     plt.plot(t[:20], seismogram2[:20, i]*hann, label=f"Trace {i+1} with hann window", linestyle='--')

# plt.title('Near traces with shallow reflector')
# plt.xlabel('Time (s)')
# plt.ylabel('Amplitude')
# plt.legend()
# plt.show()

# fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

# Compute the frequency spectrum of the seismograms
# hann = np.hanning(500)
# for i in range(3):
#     Seismogram1, fSeismogram1 = freqspecin3190(seismogram1[:20, i], 1000, 100)
#     plt.plot(fSeismogram1, 20*np.log10(np.abs(Seismogram1)), label=f"Trace {i+1} without windowing")
#     plt.plot(fSeismogram1, 20*np.log10(np.abs(Seismogram1*hann)), label=f"Trace {i+1} with hann window", linestyle='--')
# plt.title('Frequency Spectrum of near traces with shallow reflector')
# plt.xlabel('Frequency (Hz)')
# plt.ylabel('Magnitude')
# plt.legend()
# plt.show()

# fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))
# # Compute the frequency spectrum of the seismograms
# hann = np.hanning(500)
# for i in range(3):
#     Seismogram1, fSeismogram1 = freqspecin3190(seismogram1[:20, i], 1000, 100)

#     # Plot without windowing in ax1
#     ax1.plot(fSeismogram1, 20*np.log10(np.abs(Seismogram1)), label=f"Trace {i+1} without windowing")

#     # Plot with windowing in ax2
#     ax2.plot(fSeismogram1, 20*np.log10(np.abs(Seismogram1*hann)), label=f"Trace {i+1} with hann window", linestyle='--')

# # Set titles, labels, and legends for both subplots
# ax1.set_title('Frequency Spectrum without Windowing')
# ax1.set_xlabel('Frequency (Hz)')
# ax1.set_ylabel('Magnitude (dB)')
# ax1.legend()

# ax2.set_title('Frequency Spectrum with hanning Window')
# ax2.set_xlabel('Frequency (Hz)')
# ax2.set_ylabel('Magnitude (dB)')
# ax2.legend()

# # Adjust layout and show the plot
# plt.tight_layout()
# plt.show()

# y1 = convin3190(seismogram1, h1, 0)
# y2 = convin3190(seismogram1, h2, 0)


y1 = np.zeros((len(seismogram1), len(seismogram1[0])))
y2 = np.zeros((len(seismogram1), len(seismogram1[0])))
for i in range(len(seismogram1[0])):
    y1[:, i] = convin3190(seismogram1[:,i], h1, 0)
    y2[:, i] = convin3190(seismogram2[:,i], h2, 0)
plt.show()

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))
for i in range(3):
    ax1.plot(t, y1[:, i], label=f"Trace {i+1} with h1")
    ax2.plot(t, y2[:, i], label=f"Trace {i+1} with h2", linestyle='--')


fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))
for i in range(3):
    ax1.plot(t[:20], y1[:20, i], label=f"Trace {i+1} with h1")
    ax2.plot(t[:20], y2[:20, i], label=f"Trace {i+1} with h2", linestyle='--')

ax1.legend()
ax2.legend()
plt.show()
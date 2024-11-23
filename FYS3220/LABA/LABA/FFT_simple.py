import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys

# Read in the data
try:
    data = pd.read_csv(sys.argv[1])
except IndexError:
    data = pd.read_csv("2_complexsingal_example.csv")

# collects the header names
header = data.columns

# Extract the two first collumns from the DataFrame and converts to numpy arrays
time = data[header[0]].to_numpy()
voltage = data[header[1]].to_numpy()

# Calculate the FFT
fft = np.fft.fft(voltage)

# Calculate the frequency axis
freq = np.fft.fftfreq(len(time), time[1] - time[0])

# scales the amplitude to be comparable to the original signal
fft = 2 / len(time) * np.abs(fft)

# Plot the results
plt.plot(freq, np.abs(fft))
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude (V)')
plt.title('FFT of signal')

# (optional) change the range of the x-axis
plt.xlim(0, 3000) 

# change the size of the plot
plt.rcParams['figure.figsize'] = [20, 10]

# Show the plot
plt.show()


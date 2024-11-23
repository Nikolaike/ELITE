import numpy as np
import matplotlib.pyplot as plt
def readfile(filename):
    with open(filename,"r") as f:
        lines = f.readlines()
        delta_x = np.zeros(int(len(lines)/2))
        abs_error = np.zeros(int(len(lines)/2))
        n = np.zeros(int(len(lines)/2))
        j = 0
        for i in range(1, len(lines), 2):
            a = lines[i].split(",")
            delta_x[j] = float(a[0].split(":")[1])
            abs_error[j] = float(a[3].split(":")[1])
            n[j] = float(a[5].split("=")[1])
            j += 1
    plt.subplot(2,1,1)
    plt.semilogy(n,delta_x)

    plt.subplot(2,1,2)
    plt.semilogy(n,abs_error)
    plt.show()
readfile("output.txt")
"""
Terminal>python .\plot_round_off_error.py
"""

"""
Etter 10^-8 sliter pcen med å regne med så små tall, så beregningene blir ikke helt riktige.

"""

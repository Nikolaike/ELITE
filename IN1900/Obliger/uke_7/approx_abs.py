import numpy as np
import matplotlib.pyplot as plt
def abs_approx(x,N):
    for k in range(1,4):
        f = (np.pi/2)-(4/np.pi)*(np.cos(2*k-1)*x)/(2*k-1)**2
    return f

x = np.linspace(-np.pi, np.pi)
plt.plot(x,abs_approx(x,4), label="abs(x)")
plt.xlabel("x")
plt.ylabel("y")
plt.show()

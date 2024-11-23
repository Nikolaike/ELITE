import numpy as np
import matplotlib.pyplot as plt 

n = 1000
t = np.linspace(0, 2*np.pi, n)
m = 2
omega = 3
B = -4/3
C = 1/5
x = B * np.sin(omega*t) + C * np.cos(omega*t)
x_dot = B * omega * np.cos(omega*t) - C*omega * np.sin(omega*t)

plt.plot(x, x_dot*m)
plt.axis("equal")
plt.xlabel("x[m]")
plt.ylabel("V*m [m*kg/s]")
plt.savefig("3d.png")
plt.show()

A_x = max(x)
A_x_dot = max(x_dot)


plt.plot(x/A_x, x_dot/(A_x*omega))
plt.axis("equal")
plt.savefig("3e.png")



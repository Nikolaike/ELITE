import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d as Axes3D

t = np.linspace(0,np.pi,100)

x = np.cos(t)
y = np.sin(t)
z = 4*np.sin(4*t)**2

fig = plt.figure("Parametrisk kurve")

ax = fig.add_subplot(projection="3d")

ax.plot(x,y,z)


ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

plt.title("Parametrisk kurve")
plt.show()

"""
py .\oblig1_oppg3.py
"""
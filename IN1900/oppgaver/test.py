import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(-2,2,1000)
y = np.linspace(-2,2,1000)

fig = plt.figure()
ax = plt.axes(projection='3d')

ax = plt.axes(projection='3d')

# Data for a three-dimensional line
zline = np.linspace(0, 15, 1000)
xline = np.sin(zline)
yline = np.cos(zline)
ax.plot3D(xline, yline, zline, 'gray')

# Data for three-dimensional scattered points
zdata = 1
xdata = 1/x^2
ydata = 1/-y^2
ax.scatter3D(xdata, ydata, zdata, c=zdata, cmap='Greens');

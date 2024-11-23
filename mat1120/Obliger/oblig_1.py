import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
x = np.linspace(-10, 10, 100)
y = np.linspace(-10, 10, 100)
X, Y = np.meshgrid(x, y)

x_1 = np.array([2, 1, 0])
x_2 = np.array([4, 2, 3])

B = np.array([5, 0, 0])
C = np.array([2, 1, 1])

a, b, c = np.cross(x_1, x_2) / 3
d = (- a * x_1[0] - b * x_1[1] - c * x_1[2]) 

Z = (-a * X - b * Y) 

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')


#Vektor x_1 og x_2
ax.quiver(0, 0, 0, x_1[0], x_1[1], x_1[2], color='r', arrow_length_ratio=0.1)
ax.quiver(0, 0, 0, x_2[0], x_2[1], x_2[2], color='r', arrow_length_ratio=0.1)


#vektor b og c
ax.quiver(0, 0, 0, B[0], B[1], B[2], color='b', arrow_length_ratio=0.1)
ax.quiver(0, 0, 0, C[0], C[1], C[2], color='b', arrow_length_ratio=0.1)

#plan
ax.plot_surface(2*Y, 1/2*X, Z,  color = "g", alpha = 0.5)

#print(a, b, c, d)


ax.set_xlim([0, 6])
ax.set_ylim([0, 6])
ax.set_zlim([0, 6])

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.title('3D Vector Plot')


plt.show()

# import matplotlib.pyplot as plt
# import numpy as np

# x = np.linspace(-6, 6, 100)
# y = np.linspace(-6, 6, 100)
# X, Y = np.meshgrid(x, y)

# x_1 = np.array([2, 1, 0])
# x_2 = np.array([4, 2, 3])

# B = np.array([5, 0, 0])
# C = np.array([2, 1, 1])

# a, b, c = np.cross(x_1, x_2)/3
# d = (- a * x_1[0] - b * x_1[1] - c * x_1[2]) 

# Z = a * X + b * Y + d

# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')

# # Plan
# ax.plot_surface(X, Y, Z,  color="g", alpha=0.5)

# # Vektor x_1
# ax.quiver(x_1[0], x_1[1], x_1[2], x_2[0], x_2[1], x_2[2], color='r', arrow_length_ratio=0.1)

# # Vektor b og c
# ax.quiver(0, 0, 0, B[0], B[1], B[2], color='b', arrow_length_ratio=0.1)
# ax.quiver(0, 0, 0, C[0], C[1], C[2], color='b', arrow_length_ratio=0.1)

# ax.set_xlim([-6, 6])
# ax.set_ylim([-6, 6])
# ax.set_zlim([-6, 6])

# ax.set_xlabel('X')
# ax.set_ylabel('Y')
# ax.set_zlabel('Z')
# plt.title('3D Vector Plot')

# plt.show()
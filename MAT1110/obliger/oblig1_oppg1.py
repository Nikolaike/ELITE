import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

v_1 = np.array([1,
                1,
                1])
v_2 = np.array([1,
                1,
                -2])
v_3 = np.array([1,
                -1,
                0])

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.quiver(0, 0, 0, 1, 1, 1,)
ax.quiver(0, 0, 0, 1, 1, -2,)
ax.quiver(0, 0, 0, 1, -1, 0,)


ax.set_xlim([-3, 4])
ax.set_ylim([-3, 4])
ax.set_zlim([-3, 4])

dot1 = v_1.dot(v_3)
dot2 = v_1.dot(v_2)
dot3 = v_2.dot(v_3)


print(f"Dotproduktet mellom v1 og v2 er {dot1}")
print(f"Dotproduktet mellom v1 og v3 er {dot2}")
print(f"Dotproduktet mellom v2 og v3 er {dot3}")

plt.show()


A = np.array([[1, 1, 1],
              [1, 1, -1],
              [1, -2, 0]])
B = np.linalg.inv(A)
print(B)

v_1 = np.array([[1],
                [1],
                [1]])
v_2 = np.array([[1],
                [1],
                [-2]])
v_3 = np.array([[1],
                [-1],
                [0]])

print(B.dot(v_1))
print(B.dot(v_2))
print(B.dot(v_3))
"""
py .\oblig1_oppg1.py
Dotproduktet mellom v1 og v2 er 0
Dotproduktet mellom v1 og v3 er 0
Dotproduktet mellom v2 og v3 er 0
[[ 0.33333333  0.33333333  0.33333333]
 [ 0.16666667  0.16666667 -0.33333333]
 [ 0.5        -0.5        -0.        ]]
[[1.]
 [0.]
 [0.]]
[[1.11022302e-16]
 [1.00000000e+00]
 [0.00000000e+00]]
[[0.]
 [0.]
 [1.]]

"""
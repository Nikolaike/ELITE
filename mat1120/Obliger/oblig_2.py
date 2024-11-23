import sympy
import numpy as np
import matplotlib.pyplot as plt

matrix = np.array([[1, 2, 4, 8, 7],
                   [1, 3, 9, 27, 3],
                   [1, 4, 16, 64, 5],
                   [1, 5, 25, 125, 4],
                   [1, 6, 36, 216, 3]])

matrix_rref = sympy.Matrix(matrix).rref()

A = np.array([[1, 2, 4, 8],
              [1, 3, 9, 27],
              [1, 4, 16, 64],
              [1, 5, 25, 125],
              [1, 6, 36, 216]])

b = np.array([[7],
             [3],
             [5],
             [4],
             [3]])

ATA = np.array([[5, 20, 90, 440],
                [20, 90, 440, 2274],
                [90, 440, 2274, 12200],
                [440, 2274, 12200, 67170]])



matrix2_rref = sympy.Matrix([[5, 20, 90, 440, 22],
                            [20, 90, 440, 2274, 81],
                            [90, 440, 2274, 12200, 343],
                            [440, 2274, 12200, 67170, 1605]]).rref()

res = np.array(matrix2_rref[0]).astype(float)
c0 = res[0][4]
c1 = res[1][4]
c2 = res[2][4]
c3 = res[3][4]

t = np.linspace(1.9, 6.1, 100)

p = c0 + c1*t + c2*t**2 +c3*t**3

points_x = [2, 3, 4, 5, 6]
points_y = [7, 3, 5, 4, 3]
plt.plot(t, p, label="Polynomet p(t)")
plt.scatter(points_x, points_y, label="Punkter")
plt.ylabel("s")
plt.xlabel("t")
plt.legend()
plt.show()


matrix3_rref = sympy.Matrix([[5, 20, 90, 440, 2274, 22],
                [20, 90, 440, 2274, 12200, 81],
                [90, 440, 2274, 12200, 67170, 343],
                [440, 2274, 12200, 67170, 376760, 1605],
                [2274, 12200, 67170, 376760, 2142594, 8023]]).rref()
res2 = np.array(matrix3_rref[0]).astype(float)
print(matrix3_rref)

d0 = res2[0][5]
d1 = res2[1][5]
d2 = res2[2][5]
d3 = res2[3][5]
d4 = res2[4][5]


q = d0 + d1*t + d2*t**2 + d3*t**3 + d4*t**4

plt.plot(t, q, label="Polynomet q(t)")
plt.scatter(points_x, points_y, label="Punkter")
plt.ylabel("s")
plt.xlabel("t")
plt.legend()
plt.show()


def f(x):
    return x
L = 1.0  
N = 1000
x = np.linspace(-L, L, N)

y = f(x)

def fourier(N):
    y_approx = 0
    for n in range(1, N+1):
        bn = (2*np.sin(np.pi*n) - 2*np.pi*n*np.cos(np.pi*n))/(np.pi**2*n**2) 
        y_approx += bn * np.sin((n * np.pi * 2*x) / L)
    plt.plot(x, y, label="Original funksjon $f(x) = x$")
    plt.plot(2*x, y_approx, label=f"Fourier tilnærming N = {N}")
    plt.legend()
    plt.show()
fourier(4)
fourier(6)

import random
def klokkekabal():
    done = 0
    kabal = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13]]
    deck = [1,2,3,4,5,6,7,8,9,10,11,12,13] * 4
    random.shuffle(deck)
    while deck != []:
        for x in range(13):
            if deck == []:
                return (0)
            if kabal[x][-1] != "complete":
                if kabal[x][0] != deck[0]:
                    kabal[x].append(deck.pop(0))
                else:
                    for y in range(len(kabal[x])-1):
                        deck.append(kabal[x].pop(1))
                    kabal[x].append(deck[0])
                    kabal[x].append("complete")
                    done += 1
                    if done == 13:
                        return (1)

def repeatkabal():
    n = int(input("Hvor mange ganger skal kabalen legges "))
    a = 0
    b = 0
    for x in range(n):
        if klokkekabal():
            a+=1
        else:
            b+=1
    print(a)
    print(b)
    print(a/(a+b))
repeatkabal()


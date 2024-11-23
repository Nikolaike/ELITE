import numpy as np
import matplotlib.pyplot as plt
#e)
k = 500
h = 0.3
l0 = 0.5
g = 9.81
m = 5

x = np.linspace(-0.75, 0.75,100)
def F(x):
    return -k*x*(1-l0/(np.sqrt(x**2+h**2)))
plt.plot(x,F(x))
plt.xlabel("Posisjon")
plt.ylabel("Fjærkraft")
plt.show()
#f)
tmax = 10
dt = 0.01
n = int(tmax/dt)
a = np.zeros(n)
v = np.zeros(n)
x_pos = np.zeros(n)
t = np.zeros(n)
N = np.zeros(n)
EK = np.zeros(n)
def bev(x0, my=0):
    x_pos[0] = x0
    for i in range(n-1):
        N[i] = abs(k*h*(1-l0/(np.sqrt(x_pos[i]**2+h**2)))+m*g)
        EK[i+1] = (1/2)*m*v[i]**2
        t[i+1] = t[i]+dt
        a[i] = (F(x_pos[i])-(N[i]*my)*np.sign(v[i]))/m
        v[i+1] = v[i]+a[i]*dt
        x_pos[i+1] = x_pos[i]+v[i+1]*dt


    plt.subplot(3,1,1)
    plt.plot(t, a)
    plt.ylabel("Akselerasjon")
    plt.subplot(3,1,2)
    plt.plot(t,v)
    plt.ylabel("Fart")
    plt.subplot(3,1,3)
    plt.plot(t,x_pos)
    plt.xlabel("Tid")
    plt.ylabel("Posisjon")
    plt.show()
    plt.plot(x_pos,EK)
    plt.xlabel("Posisjon")
    plt.ylabel("Kinetisk energi")
    plt.show()

bev(0.6)

#g)
bev(0.65)

#k)
bev(0.75, 0.05)

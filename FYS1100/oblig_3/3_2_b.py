import numpy as np
import matplotlib.pyplot as plt

g = 9.81 #tyngdeakselerasjon
my = 0.5 #friksjonskoeffisient

x0 = 0. #startposisjon
v0 = 3 #startfart

tmax = 10.0 #største tiden
dt = 0.01
t = 0. #starttiden

n = int(tmax/dt)

a = np.zeros(n)
v = np.zeros(n)
x = np.zeros(n)
t = np.zeros(n)
x[0] = x0
v[0] = v0
t[0] = 0

i = 0


while i<n-1:
    a[i] = -my*g
    v[i+1] = v[i]+a[i]*dt
    x[i+1] = x[i] + v[i+1]*dt  # Euler-Cromer
    t[i+1] = t[i]+dt
    i = i+1
    if v[i]+a[i]*dt < 0:
        a = a[0:i+1]
        v = v[0:i+1]
        x = x[0:i+1]
        t = t[0:i+1]
        break


print(f"{x[-1]:.3f} meter")
plt.subplot(3,1,1)
plt.plot(t[:-1],x[:-1])
plt.xlabel('t [s]')
plt.ylabel('x [m]')

plt.subplot(3,1,2)
plt.plot(t[:-1],v[:-1])
plt.xlabel('t [s]')
plt.ylabel('v [m/s]')

plt.subplot(3,1,3)
plt.plot(t[:-1],a[:-1])
plt.xlabel('t [s]')
plt.ylabel('a [m/s$^2$]')

plt.show()

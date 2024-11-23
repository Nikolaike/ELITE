import numpy as np
import matplotlib.pyplot as plt
#oppgave e)
A0=0.45
CD = 1.2
p = 1.293
w = 0
m = 80
tmax = 10
dt = 0.001
F = 400
a1 = F/m
fc = 488
tc = 0.67
fv = 25.8

n = int(tmax/dt)
"""a = np.zeros(n)
v = np.zeros(n)
x = np.zeros(n)
t = np.zeros(n)
FN = np.zeros(n)

for i in range(n-1):
    t[i+1]= t[i]+dt
    a[i] = a1-1/2*(p*CD*A0*(v[i]-w)**2)/m
    v[i+1] = v[i]+a[i]*dt
    x[i+1] = x[i]+v[i+1]*dt

    if x[i+1] >= 100:
        a = a[:i+2]
        t = t[:i+2]
        v = v[:i+2]
        x = x[:i+2]
        break



plt.subplot(3,1,1)
plt.plot(t[:-1], a[:-1])
plt.ylabel("Akselerasjon [m/s^2]")
plt.subplot(3,1,2)
plt.plot(t,v)
plt.ylabel("Fart [m/s]")
plt.subplot(3,1,3)
plt.plot(t,x)
plt.xlabel("Tid [s]")
plt.ylabel("Posisjon [m]")
#plt.show()



#oppgave f)
#print(t[-1])

#oppgave h)
VT = np.sqrt(2*F/(p*CD*A0))
print(VT)
"""
#oppgave j)

a2 = np.zeros(n)
v2 = np.zeros(n)
x2 = np.zeros(n)
t2 = np.zeros(n)
FN = np.zeros(n)
def FC(t):
    return fc*np.exp(-(t/tc)**2)
def A(t):
    return A0*(1-0.25*np.exp(-(t/tc)**2))
def D(t,v):
    return 1/2*(p*CD*A(t)*(v-w)**2)
def Fv(v):
    return -fv*v

for i in range(n-1):
    t2[i+1] = t2[i]+dt
    FN[i] = F+FC(t2[i])+Fv(v2[i])-D(t2[i],v2[i])
    a2[i] = FN[i]/m
    v2[i+1] = v2[i]+a2[i]*dt
    x2[i+1] = x2[i]+v2[i+1]*dt
    if x2[i+1] >= 100:
        a2 = a2[:i+2]
        v2 = v2[:i+2]
        x2 = x2[:i+2]
        FN = FN[:i+2]
        t2 = t2[:i+2]
        break

plt.subplot(3,1,1)
plt.plot(t2[:-1], a2[:-1])
plt.ylabel("Akselerasjon [m/s^2]")
plt.subplot(3,1,2)
plt.plot(t2,v2)
plt.ylabel("Fart [m/s]")
plt.subplot(3,1,3)
plt.plot(t2,x2)
plt.xlabel("Tid [s]")
plt.ylabel("Posisjon [m]")
plt.show()

print(t2[-1])

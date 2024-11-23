import numpy as np
import matplotlib.pyplot as plt
def f(u,t):
    return u/5


def ForwardEuler(f, U0, T, N):
    t = np.zeros(N+1)
    u = np.zeros(N+1)
    u[0] = U0
    t[0] = 0
    dt = T/N
    for n in range(N):
        t[n+1] = t[n] + dt
        u[n+1] = u[n] + dt*f(u[n], t[n])
    return u, t

def u_exact(t):
    return 0.1*np.exp(0.2*t)


for N in [4,20,40,100,1000]:
    U0 = 0.1
    T = 20
    u,t = ForwardEuler(f,U0,T,N)
    plt.plot(t,u)
    plt.plot(t,u_exact(t))
    plt.legend(["numerical", "exact"])
    plt.xlabel(f"dt = {T/N}")
    plt.show()

"""
Terminal> py .\simple_ODE_func.py
"""

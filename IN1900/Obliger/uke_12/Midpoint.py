import numpy as np
import matplotlib.pyplot as plt
class ODESolver:
    def __init__(self, f):
        self.f = f
    def advance(self):
        raise NotImplementedError
    def set_initial_condition(self, U0):
        self.U0 = float(U0)
    def solve(self, time_points):
        self.t = np.asarray(time_points)
        N = len(self.t)
        self.u = np.zeros(N)
        self.u[0] = self.U0
        for n in range(N-1):
            self.n = n
            self.u[n+1] = self.advance()
        return self.u, self.t

class ForwardEuler(ODESolver):
    def advance(self):
        u, f, n, t = self.u, self.f, self.n, self.t
        dt = t[n+1] - t[n]
        unew = u[n] + dt*f(u[n], t[n])
        return unew

class Midpoint(ODESolver):
    def advance(self):
        u, f, n, t = self.u, self.f, self.n, self.t
        dt = t[n+1] - t[n]
        k1 = f(u[n], t[n])
        k2 = f(u[n] + dt/2*k1, t[n] + dt/2)
        unew = u[n] + dt*k2
        return unew


def u_a(t):
    return t*np.cos(t)
def f(u,t):
    return np.cos(t)-t*np.sin(t)
time_points = np.linspace(0,4*np.pi,20)

fe = ForwardEuler(f)
fe.set_initial_condition(U0=0)
u1, t1 = fe.solve(time_points)
plt.plot(t1, u1, label="Forward Euler")

mp = Midpoint(f)
mp.set_initial_condition(U0=0)
u2, t2 = mp.solve(time_points)
plt.plot(t2,u2, label="Midpoint")


plt.plot(time_points,u_a(time_points), label="Analytical solution")

plt.legend()

plt.show()

"""
Terminal> py .\Midpoint.py
"""

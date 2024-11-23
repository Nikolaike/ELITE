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
def f(u,t):
    return u/5
for N in [4,20,40,100, 1000]:
    time_points = np.linspace(0,20,N)
    fe = ForwardEuler(f)
    fe.set_initial_condition(U0=0.1)
    u1, t1 = fe.solve(time_points)
    plt.plot(t1, u1, label="Forward Euler")


    time_exact = np.linspace(0,20 ,301)
    plt.plot(time_exact,0.1*np.exp(0.2*time_exact),label="Exact")
    plt.legend()
    plt.show()
"""
py .\simple_ODE_class_ode_solver.py
"""

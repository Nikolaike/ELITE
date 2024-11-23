import numpy as np
import matplotlib.pyplot as plt
class ForwardEuler:
    def __init__(self, f, U0, T, N):
        self.f, self.U0, self.T, self.N = f, U0, T, N
        self.dt = T/N
        self.u = np.zeros(self.N+1)
        self.t = np.zeros(self.N+1)
    def solve(self):
        self.u[0] = float(self.U0)
        for n in range(self.N):
            self.n = n
            self.t[n+1] = self.t[n] + self.dt
            self.u[n+1] = self.advance()
        return self.u, self.t
    def advance(self):
        u, dt, f, n, t = self.u, self.dt, self.f, self.n, self.t
        unew = u[n] + dt*f(u[n], t[n])
        return unew

class f:
    def __init__(self,U0):
        self.U0 = U0
    def __call__(self,u,t):
        return u/5
def u_exact(t):
    return 0.1*np.exp(0.2*t)

for N in [4,20,40,100, 1000]:
    problem = f(0.1)
    method = ForwardEuler(problem, problem.U0, 20, N)
    u,t = method.solve()
    plt.plot(t,u)
    plt.plot(t,u_exact(t))
    plt.legend(["numerical", "exact"])
    plt.xlabel(f"dt = {20/N}")
    plt.show()

"""
Terimal> py .\simple_ODE_class.py
"""

import numpy as np
import matplotlib.pyplot as plt
class Cooling:
    def __init__(self, h, Ts):
        self.h = h
        self.Ts = Ts
    def __call__(self,T,t):
        return -self.h*(T-self.Ts)


def estimate_h(t1,Ts,T0,T1):
    return (T1-T0)/(t1*(Ts-T0))

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
def test_Cooling():
    success = False
    test = Cooling(3, 22)
    calculated = test(80,0)
    expected = -174
    if abs(calculated-expected)<= 10e-6:
        success = True
    assert success, f"expected {expected} got {calculated}"
test_Cooling()


time_points = np.linspace(0,2000,1001)
T0, T1, t1 = 95, 92, 15
Ts = (20,25)

for i in range(len(Ts)):
    h = estimate_h(t1, Ts[i], T0, T1)
    coffee = ForwardEuler(Cooling(h,Ts[i]))
    coffee.set_initial_condition(T0)
    heatfall = coffee.solve(time_points)
    plt.plot(heatfall[1], heatfall[0], label= f"Room temp {Ts[i]}")
    plt.xlabel("Time in seconds")
    plt.ylabel("Temp in celcius")
    plt.legend()
plt.show()

"""
Terminal> py .\coffee.py
"""

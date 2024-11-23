import numpy as np
import matplotlib.pyplot as plt
class F:
    def __init__(self,n,m):
        self.n = n
        self.m = m
    def __call__(self,x):
        return np.sin(self.n*x)*np.cos(self.m*x)

x = np.linspace(0,2*np.pi,1001)
u = F(7, 8)
v = F(-8, -5)
plt.plot(u(x),v(x))
plt.show()
"""
Terminal>py .\F.py
"""

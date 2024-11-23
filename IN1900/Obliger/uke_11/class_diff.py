import numpy as np
from numpy import sin,cos,pi
import matplotlib.pyplot as plt
class Diff:
    def __init__(self,f):
        self.f = f
    def diff1(self,x,f,h):
        f = self.f
        return (f(x+h)-f(x))/h
    def diff2(self,x,f,h):
        f = self.f
        return (f(x+h)-f(x-h))/(2*h)
    def diff3(self,x,f,h):
        f = self.f
        return (-f(x+2*h)+8*f(x+h)-8*f(x-h)+f(x-2*h))/(12*h)

def F(x):
    return sin(2*pi*x)

x = np.linspace(-1,1,100)
h = [0.9,0.6,0.3,0.1]
dydx = Diff(F)
y = 2*pi*cos(2*pi*x)
for i in range(len(h)):
    plt.subplot(4,4,i*4+1)
    plt.xlabel("Exact values")
    plt.ylabel(f"h = {h[i]}")
    plt.plot(x,y)
    y1 = dydx.diff1(x,2*pi,h[i])
    plt.subplot(4,4,i*4+2)
    plt.xlabel("Diff 1")
    plt.plot(x,y1)
    y2 = dydx.diff2(x,2*pi,h[i])
    plt.subplot(4,4,i*4+3)
    plt.xlabel("Diff 2")
    plt.plot(x,y2)
    y3 = dydx.diff3(x,2*pi,h[i])
    plt.subplot(4,4,i*4+4)
    plt.xlabel("Diff 3")
    plt.plot(x,y3)
plt.show()

"""
Terminal> py .\class_diff.py
"""

import numpy as np
import matplotlib.pyplot as plt
"""
class Person:
    def __init__(self,name,age,gender):
        self.name = name; self.age = age; self.gender = gender

    def new_info(self,new_name,new_age,new_gender):
        self.name = new_name; self.age = new_age; self.gender = new_gender
    def __str__(self):

        return f"Name: {self.name}, Age: {self.age}, Gender {self.gender}"
p = Person("John", 36, "male")
print(p)

p.new_info("finn atle", 8, "male")
print(p)
"""
"""
class RightTriangle:
    def __init__(self, a,b):
        if a < 0 or b < 0:
            raise ValueError
        self.a = a; self.b = b
        self.c = np.sqrt(a**2+b**2)
    def __str__(self):
        return f"triangle has sides {self.a} {self.b} {self.c}"
    def plot_triangle(self):
        a = [0,self.a,0,0]
        b = [0,0,self.b,0]
        plt.plot(a,b)
        plt.axis("equal")

        plt.show()

triangle1 = RightTriangle(1,1)

triangle2 = RightTriangle(3,4)
triangle2.plot_triangle()




def test_RightTriangle():
    success = False
    try:
        triangle3 = RightTriangle(1,-1)
    except ValueError:
        success = True
    assert success
test_RightTriangle()
"""
"""
class F:
    def __init__(self, n,m):
        self.m = m; self.n = n

    def __call__(self,x):
        return np.sin(self.n*x)*np.cos(self.m*x)

x = np.linspace(0, 2*np.pi, 1000)
u = F(2,3)
v = F(9,5)

plt.plot(u(x),v(x))

plt.show()
"""
"""
class Diff:
    def __init__(self,f):
        self.f = f
    def diff1(self,h,x):
        return (f(x+h)-f(x))/h
    def diff2(self,h,x):
        return (f(x+h)-f(x-h))/(2*h)
    def diff3(self,h,x):
        return (-f(x+2*h)+8*f(x+h)-8*f(x-h)+f(x-2*h))/(12*h)
h = [0.9,0.6,0.3,0.1]
x = np.linspace(-1,1,101)
def f(x):
    return np.sin(2*np.pi*x)
def f_derivative(x):
    return 2*np.pi*np.cos(2*np.pi*x)
for i in range(len(h)):
    d = Diff(f(x))

    plt.subplot(4,1,i+1)
    plt.plot(x,d.diff1(h[i], x), label=f"{h[i]}")
    plt.plot(x,f_derivative(x), label = "exact")

    plt.legend()
plt.show()
for i in range(len(h)):
    plt.subplot(4,1,i+1)
    plt.plot(x,d.diff2(h[i], x), label=f"{h[i]}")
    plt.plot(x,f_derivative(x), label = "exact")
    plt.legend()
plt.show()
for i in range(len(h)):
    plt.subplot(4,1,i+1)
    plt.plot(x,d.diff3(h[i], x), label=f"{h[i]}")
    plt.plot(x,f_derivative(x), label = "exact")
    plt.legend()
plt.show()
"""

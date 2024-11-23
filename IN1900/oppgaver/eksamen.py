"""
counties = {}
with open('counties.txt') as infile:
    for line in infile:
        w = line.split(';')
        #data = {"name":w[1], "pop":int(w[2]), "area":int(w[3])}
        data = {}
        data[name] = w[1]; data[pop] = int(w[2]); data[area] = int(w[3])
        counties[w[0]] = data
print(counties['F-03'])
"""
"""
from numpy import cos
def forward(f,x,h):
    return (f(x+h)-f(x))/h

print(f"{forward(lambda x: cos(x), 0, 0.001):.4f}")
"""

"""
def f(x,y):
    cal = []
    for i in range(len(y)):
        if y[i] > 0:
             cal.append(3*x**2+y[i]+3*x*y[i])
        else:
            cal.append(3*x*y[i]-3*x*y[i])
    return cal
print(f(2, [1,2,3,4,5]))
"""
"""
def log_approx(x,n):
    s = 0
    for k in range(1,n+1):
        s += (-1)**(k+1*)*x**k/k
    return s
"""
"""
def piecewise(x,a,b):
    if x<=a:
        return 0.0
    elif a<x and x<=b:
        return (x-a)/(b-a)
    else:
        return 1.0
print(piecewise(0.5, 0, 1))
"""
"""
from numpy import sin, pi
def f(x,a):
    if 0 <= x-a <= pi:
        return sin(x-a)
    else:
        return 0
def test_f():
    a = 1
    success1 = False
    success2 = False
    success3 = False
    computed_x1 = f(1,a)
    expected_x1 = 0.0

    computed_x2 = f(2,a)
    expected_x2 = sin(1)

    computed_x6 = f(6,a)
    expected_x6 = 0.0
    tol = 1e-6

    if abs(computed_x1-expected_x1) <= tol:
        success1 = True
    if abs(computed_x2-expected_x2) <= tol:
        success2 = True
    if abs(computed_x6-expected_x6) <= tol:
        success3 = True
    assert success1, f"expected {expected_x1} got {computed_x1}"
    assert success2, f"expected {expected_x2} got {computed_x2}"
    assert success3, f"expected {expected_x6} got {computed_x6}"
test_f()
"""
"""
a = [list(range(10)), list(range(1)), list(range(20)), list(range(100))]
def longest(a):
    i_max = []
    for i in range(len(a)):
        if len(i_max) < len(a[i]):
            i_max = a[i]

    return i_max

print(longest(a))
"""
"""
def is_prime(n):
    for i in range(2,n):
        if (n%i) == 0:
            return False
    return True
def primes(n):
    s = []
    for i in range(2,n+1):
        if is_prime(i) == True:
            s.append(i)
    return s
print(primes(20))
"""
"""
word = "car"
def is_palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False
print(is_palindrome(word))
"""
"""
dict = {}
with open("counties.txt") as infile:
    for line in infile:
        a =[]
        a = line.split(" ")
        if len(a) == 2:
            print(a)
            dict = {a[0], int(a[1])}

        else:
            str_list = [a[0], a[1], a[2]]
            str = "".join(str_list)
            dict = {str, a[3]}
"""
"""
class F:
    def __init__(self,a,b,c,d):
        self.a = a; self.b = b; self.c = c; self.d = d
    def __call__(self,x):
        self.x = x
        return self.a*x**3 + self.b*x**2 + self.c*x + self.d
    def __str__(self):
        return f"{self.a}*x^3 + {self.b}*x^2 + {self.c}*x + {self.d}"
f = F(0.0,1.0,2.0,0.0)
x = 2.0
print(f(x))

f = F(1.0,2.0,3.0,0.0)
print(f)
"""
"""
import numpy as np
def ralston(f,U0,T,n):
    N = int(T/n)
    u = np.zeros(N)
    t = np.zeros(N)
    u[0] = U0
    for i in range(N):
        k1 = f(u[i], t[i])
        k2 = f(u[i]+2/3*n*k1,t[i]+2/3*n)
        u[i+1] = u[i] + n*(1/4*k1+ 3/4*k2)
        t[i+1] = t[i] + n
    return u,t
"""
"""
class Ralston(ODESolver):
    def advance(self):
        u, f, n, t = self.u, self.f, self.n, self.t
        dt = t[n+1]-t[n]
        k1 = f(u[n], t[n])
        k2 = f(u[n]+2/3*dt*k1,t[n]+2/3*dt)
        u[i+1] = u[n] + dt*(1/4*k1+ 3/4*k2)
        t[i+1] = t[n] + dt
        return u,t
"""

"""
def f(x,y):
    return 4*x**3*y-2*x*y

"""
"""import numpy as np
def midpoint(f,x,h):
    return f(x),(f(x+h)-f(x-h))/(2*h)
print(midpoint(np.cos,0,0.0001))
"""
"""
from numpy import factorial
def cos_approx(x,n):
    s = 0
    for k in range(n+1):
        s += (-1)**k*(x**(2*k))/(factorial(2*k))
"""
"""
constants = {}
with open("test.txt") as f:
    f.readline()
    f.readline()
    for line in f:
        w = line.split()
        name = " ".join(w[:2])
        constants[name] = float(w[2]) , w[3]
print(constants["light speed"])
"""
"""
p = {0:1,2:-2,4:3,5:1}
def poly_eval(p,x):
    s = 0
    for i in p:
        s += p[i]*x**i
    return s
for i in p:
    print(i)
"""
"""
def poly_diff(p):
    s = {}
    for i in p:
        if i != 0:
            s[i-1] = i*p[i]
    return s
"""
"""
class F:
    def __init__(self,a,b,c):
        self.a = a; self.b = b; self.c = c
    def __call__(self,x):
        return self.a*x**2+self.b*x+self.c
f = F(1.0,2.0,0.0)
print(f(2))
"""
"""
def heun3(f,U0,T,n):
    t = np.linspace(0,T,n+1)
    u = np.zeros(t)
    dt = T/n
    u[0] = U0
    for i in range(n):
        k1 = dt*f(u[i],t[i])
        k2 = dt*f(u[i]+1/3*k1,t[i]+1/3*dt)
        k3 = dt*f(u[i]+2/3*k2, t[i]+2/3*dt)
        u[i+1] = u[i] + 1/4*k1 + 3/4*k2
    return u,t

class Heun3(ODESolver):
    u, f, k, t = self.u, self.f, self.k, self.t
    dt = t[k+1] - t[k]
    k1 = dt*f(u[k],t[k])
    k2 = dt*f(u[k]+1/3*k1,t[k]+1/3*dt)
    k3 = dt*f(u[k]+2/3*k2, t[k]+2/3*dt)
    return u[k] + 1/4*k1 + 3/4*k2
"""
"""
def rhs(u,t):
    a = 1.0 ; R = 50
    return a*u*(1-u/R)
from ODESolver import *
solver = Heun3(rhs)
solver.set_initial_condition(0.1)
time = np.linspace(0,20,201)
u,t = solver.solve(time)
"""

def SEIS(S0,E0,p,q,r,T):
    def rhs(u,t):
        S,E,I = u
        dS = -p(t)*S*I+r*I
        dE = p(t)*S*I-q*E
        dI = q*E - r*I
        return[dS,dE,dI]
    U0 = [S0,E0,0]
    solver = Heun3(rhs)
    solver.set_initial_condition(U0)
    t = np.linspace(0,T,10*T+1)
    solver.solve(t)
    return solver.t, solver.u[:,0], solver.u[:,1], solver.u[:,2]
def p(t):
    return 0.0233


t,S,E,I = SEIS(4.0,0.2,p,0.1,0.1,100)
plt.plot(t,S,t,E,t,I)
plt.legend(["S","E","I"])
plt.show()

a = 1
b = 2
c = -2

#def solve(a,b,c):
from math import sqrt
x1 = (-b - sqrt(b**2 - 4*a*c))/(2*a)
x2 = (-b + sqrt(b**2 - 4*a*c))/(2*a)
print(f"{x1:5.2f} {x2:5.2f}")

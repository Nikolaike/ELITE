from math import sqrt
a = 6
b = -5
c = 1
x_1 = (-b+sqrt(b**2-4*a*c))/(2*a)
x_2 = (-b-sqrt(b**2-4*a*c))/(2*a)

print(f"{x_1:3.2f}")
print(f"{x_2:3.2f}")

"""
terminal>python find_roots.py
0.50
0.33
"""

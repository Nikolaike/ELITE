import numpy as np
a = float(input("velg en verdi for a: "))
b = float(input("velg en verdi for b: "))
c = float(input("velg en verdi for c: "))

xp = float((-b + np.sqrt((b**2)-4*a*c))/2*a)
xn = float((-b - np.sqrt((b**2)-4*a*c))/2*a)

print(xp , xn)
"""
Terminal>python .\quadratic_roots_input.py
velg en verdi for a: 1
velg en verdi for b: 0
velg en verdi for c: -1
1.0 -1.0
"""

import sys
import numpy as np

try:
    a = float(sys.argv[1])
except IndexError:
    a = float(input("skriv den manglende verdier: "))
try:
    b = float(sys.argv[2])
except IndexError:
    b = float(input("skriv den manglende verdier: "))
try:
    c = float(sys.argv[3])
except IndexError:
    c = float(input("skriv den manglende verdier: "))




xp = float((-b + np.sqrt((b**2)-4*a*c))/2*a)
xn = float((-b - np.sqrt((b**2)-4*a*c))/2*a)

print(xp , xn)

"""
Terminal> python .\quadratic_roots_error.py
skriv den manglende verdier: 1
skriv den manglende verdier: 0
skriv den manglende verdier: -1
1.0 -1.0
"""

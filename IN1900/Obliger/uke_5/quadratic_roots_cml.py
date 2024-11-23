import sys
import numpy as np

a = float(sys.argv[1])
b = float(sys.argv[2])
c = float(sys.argv[3])


xp = float((-b + np.sqrt((b**2)-4*a*c))/2*a)
xn = float((-b - np.sqrt((b**2)-4*a*c))/2*a)

print(xp , xn)

"""
Terminal> python .\quadratic_roots_cml.py 1 0 -1
1.0 -1.0
"""

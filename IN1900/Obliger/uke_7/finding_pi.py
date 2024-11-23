import numpy as np

x0 = 3.14
print(x0)
for i in range(2):
    pi = x0-np.sin(x0)/np.cos(x0)
    print(f"{pi:.13f}")
    x0 = pi
print(f"{np.pi:.13f}")

"""
Terminal> python .\finding_pi.py
3.14
3.1415926549364
3.1415926535898
3.1415926535898
"""

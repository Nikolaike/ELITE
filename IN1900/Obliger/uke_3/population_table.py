
from math import exp
B = 50000
k = 0.2
C = 9
t = []
N = []
for t1 in range(0,49,4):
    N.append(B/(1+C*exp(-k*t1)))
    t.append(t1)


print("Antall timer:    Populasjon:" )
for t,N in zip(t,N):
    print(f"{t:3.0f}{N:19.0f}")
"""
Terminal> python .\population_table.py
Antall timer:    Populasjon:
  0               5000
  4               9913
  8              17749
 12              27526
 16              36580
 20              42924
 24              46552
 28              48390
 32              49263
 36              49666
 40              49849
 44              49932
 48              49970
"""

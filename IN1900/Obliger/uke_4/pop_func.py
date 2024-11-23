B = 50000
C = 9
k = 0.2

from math import exp
def N(t1,k,B,C):
    population = B/(1+C*exp(-k*t1))
    return population
print("Antall timer:     Populasjon:")
for t1 in range(0,49,4):
    print(f"{t1:3}  {N(t1,k,B,C):18.0f}")


"""
Terminal>python .\pop_func.py
Antall timer:     Populasjon:
  0                5000
  4                9913
  8               17749
 12               27526
 16               36580
 20               42924
 24               46552
 28               48390
 32               49263
 36               49666
 40               49849
 44               49932
 48               49970
"""

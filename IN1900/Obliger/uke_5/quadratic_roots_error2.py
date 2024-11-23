import numpy as np
a = float(input("velg en verdi for a: "))
b = float(input("velg en verdi for b: "))
c = float(input("velg en verdi for c: "))

if (b**2)-4*a*c < 0:
        raise ValueError("kvadratroten blir et negativt tall, velg verdier som ikke gir negativ kvadratrot")
        quit()


xp = float((-b + np.sqrt((b**2)-4*a*c))/2*a)
xn = float((-b - np.sqrt((b**2)-4*a*c))/2*a)




print(xp, xn)
"""
Terminal>python .\quadratic_roots_error2.py
velg en verdi for a: 1
velg en verdi for b: 1
velg en verdi for c: 1
Traceback (most recent call last):
  File "C:\IN1900\Obliger\uke_5\quadratic_roots_error2.py", line 7, in <module>
    raise ValueError("kvadratroten blir et negativt tall, velg verdier som ikke gir negativ kvadratrot")
ValueError: kvadratroten blir et negativt tall, velg verdier som ikke gir negativ kvadratrot
"""

"""
Terminal> python .\quadratic_roots_error2.py
velg en verdi for a: 1
velg en verdi for b: 0
velg en verdi for c: -1
1.0 -1.0
"""

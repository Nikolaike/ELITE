"""
s = 0
M = 3
for i in range(M):
    s += 1/2*k**2
print(s)


Feil 1:
Variabelen k er ikke definert, brukte variabelen "i" istedenfor "k" i linje 3:
"for i in range"

Rettelse:

for k in range(M):


Feil 2:
Det er feil i måten mattestykket er skrevet i koden, det er ikke satt
paranteser der det trengs.

Rettelse:
s += 1/(2*k)**2

Feil 3:
i range(M), skal ikke starte i 0 når k starter i 1, og hvis vi skal ha til og
med 3 må vi ha M+1.

Rettelse:
for k in range(1, M+1)
"""
#riktig kode under
s = 0
M = 3
for k in range(1, M+1):
    s += 1/(2*k)**2
print(s)

"""
Terminal> python .\sum_for.py
0.3402777777777778
"""

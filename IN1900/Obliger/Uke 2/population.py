from math import e
B = 50000
k = 0.2
t = 0
P = 5000 #populasjon når t=0


#Gjør om på funksjonen slik at C står på en side

C = (B/(e**(-k*t)*P))-1


t = 24
N = B/(1+C*e**(-k*t))
print(f"Populasjonen etter 24 timer er: {N:5.0f}")

"""
Terminal>python population.py
Populasjonen etter 24 timer er: 46552
"""

import numpy as np

f = 110 # frekvensen til den første strengen
v = 143 # fart til bølgen
L = [v / (2 * f)] # Lengden gitarhalsen 
for i in range(1, 7):
    f = 110 * 1.0595**i
    L.append(v / (2 * f)) # Posisjonen til hver streng
    # print((L[i-1] - L[i]) * 1000) # forskjell i mm mellom hvert fret
    print((L[i-1] - L[i]) / L[i-1]) # prosentvis forskjell mellom hvert fret

# for i in L: print(i)
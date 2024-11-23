import numpy as np
import matplotlib.pyplot as plt

N = 3000 #Antall oscillatorer
k0 = 1e-5 #Fjærstivhet start
kL = 10 #Fjærstivhet slutt

k = np.linspace(k0, kL, N)

rho0 = 2500 #Massetetthet start
rhoL = 2000 #Massetetthet slutt
rho = np.linspace(rho0, rhoL, N)

t = np.linspace(0, 2*np.pi, N)

k_log = np.logspace(np.log10(k0), np.log10(kL), N)

B = np.linspace(0.1e-3, 0.3e-3, N) #Bredde
T = np.linspace(0.3e-3, 0.1e-3, N) #Tykkelse
L = np.linspace(0, 30e-3, N) #Lengde
dL = 30e-3/N #Del lendge

V = B*T*dL
mx = V * rho

omega = np.sqrt(k/mx) 
omega_log = np.sqrt(k_log/mx)

plt.plot(L, omega, label="Lineær frekvens")
plt.plot(L, omega_log, label="Logaritmisk frekvens")
plt.xlabel("Lengde [m]")
plt.ylabel("Vinkelfrekvens [rad/s]")
plt.legend()
plt.show()

omega_f = 261.63*2*np.pi
omega_f2 = 277.18*2*np.pi

b = 1e-7

A = (1/mx)/np.sqrt((omega_log**2 - omega_f**2)**2 + (b/mx * omega_f)**2)
A2 = (1/mx)/np.sqrt((omega_log**2 - omega_f2**2)**2 + (b/mx * omega_f2)**2)

plt.plot(L, A, label = "261.63 Hz")
plt.plot(L, A2, label = "277.18 Hz")
plt.xlabel("Lengde [m]")
plt.ylabel("Amplitude [m]")
plt.xlim(0.009, 0.015)
plt.legend()
plt.show()

E1 = A**2
E2 = A2**2

f1 = omega_f/(2*np.pi)
f2 = omega_f2/(2*np.pi)
bw = f2 - f1
midt_frekvens = (f2 + f1) / 2
Q_faktor = midt_frekvens / bw
print(Q_faktor)


E1_max = max(E1) * np.ones(N) / 2
E2_max = max(E1) * np.ones(N) / 2


f_log = omega_log / (2*np.pi)
plt.subplot(1,2,1)
plt.plot(f_log, E1, label = "261.64 Hz")
plt.plot(f_log, E1_max)
plt.xlabel("Frekvens [Hz]")
plt.ylabel("Energi [J]")
plt.xlim(0, 500)
plt.legend()

plt.subplot(1,2,2)
plt.plot(f_log, E2, label="277.18 Hz")
plt.plot(f_log, E2_max)

plt.xlabel("Frekvens [Hz]")
plt.ylabel("Energi [J]")
plt.xlim(0, 500)
plt.show()



fall_tid = Q_faktor / (midt_frekvens * 2 * np.pi)
print(fall_tid)
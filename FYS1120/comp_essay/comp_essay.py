import numpy as np
import matplotlib.pyplot as plt


q = 1.6e-19 #ladning til proton
m = 1.67e-27 # masse til proton
# V = spennning mellom platene, det er denne vi vil å finne
d = 90e-6 #avstanden mellom platene i akseleratoren
c = 299792458 #lysets hastighet

def E(voltage):
    return(voltage/d)

B = np.array([0.0, 0.0, 1.5]) #magnetisk felt i z retning, 1.5T. Skal jeg forandre på denne?
r_cyclotron = 0.05 #radius på 5 cm


w = q*np.linalg.norm(B)/m

t = 0 #start tid
dt = 5e-12 #tidssteg, kan være vi må øke denne til 5 pico sekund.
max_velocity = 138519832

def cyclotron(E):
    particle_pos = np.array([0.0, 0.0, 0.0]) #posisjon til protonet i utgangspunktet
    particle_v = np.array([0.0, 0.0, 0.0]) #start hastigheter
    vel_list = []
    particle_pos_x = [particle_pos[0]]
    particle_pos_y = [particle_pos[1]]
    t = 0
    ke = 0
    while (np.linalg.norm(particle_pos) < r_cyclotron): #and ke < 100: #loop så lenge protonet er inne i akseleratoren

        Fnet = np.array([0.0, 0.0, 0.0]) #kraftvektor på partikkelen her

        if np.absolute(particle_pos[0]) < d/2: #hvis partikkelen er mellom de to D - ene beregner vi den elektriske kraften
            Fnet[0] = q*E*np.cos(w*t)
            Fnet += q*np.cross(particle_v, B)
        else: #hvis partikkelen ikke er innen for det elektriske feltet virker bare den magnetiske kraften
            Fnet = q*np.cross(particle_v, B)

        vel_list.append(np.linalg.norm(particle_v))
        particle_v = particle_v + Fnet*dt/m #oppdaterer hastigheten
        particle_pos = particle_pos + particle_v*dt #bruker hastighet til å oppdatere posisjon.
        particle_pos_x = np.append(particle_pos_x, particle_pos[0])
        particle_pos_y = np.append(particle_pos_y, particle_pos[1])
        t = t + dt
        ke = 0.5 * m * np.linalg.norm(particle_v)**2/(q * 1e6)
        if np.linalg.norm(particle_v) >= c:
            break
    return particle_pos_x, particle_pos_y, particle_v, np.linalg.norm(particle_v), np.linalg.norm(particle_pos)


pos_x, pos_y, vel, v, vel_list = cyclotron(E(5e4))

# t = np.linspace(0, t, len(vel_list))


plt.plot(pos_x, pos_y)
plt.show()

r_cyclotron = 1#radius på 5 cm
d = 0.02
dt = 1e-10



w = q*np.linalg.norm(B)/m

def voltage_test_cyclotron(target_ke_MeV):
    voltage = np.linspace(1e4, 1e7, 10000)  # Spenningsintervall vi ser på
    for V in voltage:
        pos_x, pos_y, _, v, r = cyclotron(E(V))
        # Sjekker den siste verdien av kinetisk energi i listen
        ke_MeV = 0.5 * m * v**2/(q * 1e6)
        if abs(ke_MeV - target_ke_MeV) < 3:  # Finner den spenningen som gir nærmest treff
            return V, ke_MeV, pos_x, pos_y, r
    print("No suitable voltage found within the given range.")
    return None, None, None, None, None

V, E_0, pos_x, pos_y, r = voltage_test_cyclotron(100)
if V is not None:
    print(f"Suitable voltage: {V} V")
    print(f"Proton energy: {E_0} MeV")
    print(r)
    plt.figure(figsize=(12, 12))
    plt.plot(pos_x, pos_y)
    plt.show()

# Konstanter
q = 1.6e-19  # Ladning til proton (Coulomb)
m = 1.67e-27  # Masse til proton (kg)

# Parametere for linak
V = 50000  # Spenningsforskjell i hvert hulrom (Volt)
d = 0.03  # Lengden av hvert hulrom (m)
n_hulrom = 50  # Antall hulrom

def linak_simulasjon(V, d, n_hulrom):
    # Initialbetingelser
    particle_pos = 0.0  # Startposisjon
    particle_v = 0.0  # Starthastighet (vi gir den en liten initial hastighet senere)
    particle_energy = []

    # Tidsparametere
    dt = 1e-11  # Tidssteg (s)

    # Simulerer akselerasjon i linak
    for hulrom in range(n_hulrom):
        # Vi antar at partikkelen får en initial hastighet i det første hulrommet
        if hulrom == 0:
            particle_v = np.sqrt(2 * q * V / m)

        # Beregner tiden det tar å passere gjennom et hulrom
        t_hulrom = d / particle_v
        n_steps = int(t_hulrom / dt)

        for step in range(n_steps):
            # Akselerasjon i hvert hulrom
            particle_v += q * V / m * dt / d
            # Oppdaterer posisjon
            particle_pos += particle_v * dt
            # Beregner og lagrer kinetisk energi
            kinetic_energy = 0.5 * m * particle_v**2/(q * 1e6)
            particle_energy.append(kinetic_energy)

            # Stopper simuleringen hvis partikkelen når opp til nær lysets hastighet
            if particle_v >=  c:
                break

        # Stopper hele simuleringen hvis partikkelen når opp til nær lysets hastighet
        if particle_v >= c:
            break

    return particle_energy, particle_v

# Kjører simuleringen
# particle_energy, particle_v = linak_simulasjon(V, d, n_hulrom)
# # Plotter resultatene
# plt.plot(particle_energy)
# plt.xlabel('Tid (arbitrær enhet)')
# plt.ylabel('Kinetisk energi (MeV)')
# plt.title('Kinetisk energi til en partikkel i en linak')
# plt.show()




# Mål for kinetisk energi i MeV
target_ke_MeV = 13  # 100 MeV
d = 0.075  # Lengden av hvert hulrom (m)
n_hulrom = 25  # Antall hulrom


def voltage_test_linak(target_ke_MeV, d, n_hulrom):
    voltage = np.linspace(1e4, 1e6, 10000)  # Spenningsintervall vi ser på
    for V in voltage:
        particle_energy, _ = linak_simulasjon(V, d, n_hulrom)
        # Sjekker den siste verdien av kinetisk energi i listen
        if particle_energy:
            ke_MeV = particle_energy[-1]
            if abs(ke_MeV - target_ke_MeV) < 1:  # Finner den spenningen som gir nærmest treff
                return V, ke_MeV, particle_energy
    print("No suitable voltage found within the given range.")
    return None, None, None


# Kjører testen
# V, E_0, particle_energy = voltage_test_linak(target_ke_MeV, d, n_hulrom)
# if V is not None:
#     print(f"Suitable voltage: {V} V")
#     print(f"Proton energy: {E_0} MeV")
#     plt.plot(particle_energy)
#     plt.xlabel('Tid (arbitrær enhet)')
#     plt.ylabel('Kinetisk energi (MeV)')
#     plt.title('Kinetisk energi til en partikkel i en linak')
#     plt.show()
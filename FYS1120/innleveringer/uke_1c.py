import numpy as np
import matplotlib.pyplot as plt
a = 5
def efield(r,q0,r0):
    # Setter 1 / (2*pi*epsilon_0) = 1 
    r0 = np.array([0,r0[1]])
    r = np.array([0,r[1]])
    R = r-r0
    Rnorm = np.linalg.norm(R)
    return q0*R/Rnorm**3

def efield2(r,q0,r0):
    # Setter 1 / (2*pi*epsilon_0) = 1 
    r0 = np.array([r0[0],0])
    r = np.array([r[0],0])
    R = r-r0
    Rnorm = np.linalg.norm(R)
    return q0*R/Rnorm**3


r0 = np.array([0,0]) # Posisjon til ladning
r1 = np.array([0,0]) # Posisjon til ladning
q0 = 1.0 # Ladningen til en ladning
q1 = -1.0 # Ladningen til en ladning

Lx = 10
Ly = 10
N = 20

x = np.linspace(-Lx,Lx,N)
y = np.linspace(-Ly,Ly,N)
rx,ry = np.meshgrid(x,y)


Ex = np.zeros((N,N))
Ey = np.zeros((N,N))

# Regner ut feltet
for i in range(len(rx.flat)):
    r = np.array([rx.flat[i],ry.flat[i]])
    Ex.flat[i],Ey.flat[i] = efield(r,q0,r0) + efield2(r,q1,r1)# Regner ut størrelsen av feltet

Emag = np.sqrt(Ex**2 + Ey**2)
# Regner ut enhetsvektorer i feltets retning
nEx = Ex / Emag
nEy = Ey / Emag
# Visualiserer
plt.quiver(rx,ry,nEx,nEy,np.log10(Emag))
plt.colorbar()
plt.axis("equal")
plt.title("Elektrisk felt oppgave c")
plt.savefig("plot_1c.png")
plt.show()

# terminal> y .\uke_1c.py
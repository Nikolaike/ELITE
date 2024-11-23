import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dodfelles=pd.read_csv("https://www.uio.no/studier/emner/matnat/math/STK1100/data/doedelighet.txt",sep="\t")
alder=dodfelles["alder"].values
menn=dodfelles["menn"].values
kvinner=dodfelles["kvinner"].values
qx = menn/1000
qy = kvinner/1000

Fx=1-np.cumprod(1-qx)   
Fy=1-np.cumprod(1-qy) 
plt.step(alder, Fx, label="Menn")
plt.step(alder, Fy, label="Kvinner")
plt.title("Kummulativ fordelingsfunksjon")
plt.legend()
plt.show()

tmpx=np.zeros(107)
tmpy=np.zeros(107)
tmpx[1:107] = Fx[0:106]
tmpy[1:107] = Fy[0:106]

px=Fx-tmpx
py=Fy-tmpy


plt.title("Punktsannsynlighet")
plt.step(alder,px,label="Menn")
plt.step(alder,py,label="Kvinner")

plt.xlabel("Alder")
plt.ylabel("p(x)") 
plt.legend()
plt.show()
hx=(alder-0)*(alder>=0)
EhX0=sum(hx*px)
print(f"Forventet levealder ved fodsel for menn er, {EhX0:.0f} er")

hx=(alder-30)*(alder>=30)
EhX30=sum(hx*px)
print(f"Forventet gjenstaaende levealder for menn naar de er 30, er {EhX30:.0f} aar")

hx=(alder-50)*(alder>=50)
EhX50=sum(hx*px)
print(f"Forventet gjenstaaende levealder for menn naar de er 50 er, {EhX50:.0f} aar")

hx=(alder-80)*(alder>=80)
EhX80=sum(hx*px)
print(f"Forventet gjenstaaende levealder for menn naar de er 80 er, {EhX80:.0f} aar")

hy = (alder-0)*(alder>=0)
EhY0 = sum(hy*py)
print(f"Forventet levealder ved fodsel for kvinner er {EhY0:.0f} aar")

hy=(alder-30)*(alder>=30)
EhX30=sum(hy*py)
print(f"Forventet gjenstaaende levealder for kvinner naar de er 30, er {EhX30:.0f} aar")

hy=(alder-50)*(alder>=50)
EhX50=sum(hy*py)
print(f"Forventet gjenstaaende levealder for kvinner naar de er 50 er, {EhX50:.0f} aar")

hy=(alder-80)*(alder>=80)
EhX80=sum(hy*py)
print(f"Forventet gjenstende levealder for kvinner naar de er 80 er, {EhX80:.0f} aar")

EhX = np.zeros(107)
EhY = np.zeros(107)
for i in alder:
    EhX[i] = sum(px*(alder-i)*(alder>=i))
    EhY[i] = sum(py*(alder-i)*(alder>=i))
plt.title("Forventet gjenstaaende levealder")
plt.step(alder,EhX,label="Menn")
plt.step(alder,EhY,label="Kvinner")
plt.legend()
plt.show()


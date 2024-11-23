import numpy as np
import matplotlib.pyplot as plt
g = 9.81
R = 1
m = 1
tmax = 20
dt = 0.001


tMax = 20
theta0 = 0
dtheta0 = 0.01

n = int(tMax/dt)
t = np.zeros(n)
theta = np.zeros(n)
dtheta = np.zeros(n)
N = np.zeros(n)

dtheta[0] = dtheta0
N[0] = 1

i=0
"""
while N[i]>0 and i<n-1:
    ddtheta = g/R*np.sin(theta[i])
    t[i+1] = t[i] + dt
    dtheta[i+1] = dtheta[i]+ ddtheta*dt
    theta[i+1] = theta[i] + dtheta[i+1]*dt
    N[i+1] = m*g*np.cos(theta[i+1])-m*dtheta[i+1]**2*R
    i = i+1"""
for i in range(n):
    ddtheta = g/R*np.sin(theta[i])
    t[i+1] = t[i] + dt
    dtheta[i+1] = dtheta[i]+ ddtheta*dt
    theta[i+1] = theta[i] + dtheta[i+1]*dt
    if theta[i]*180/np.pi >= 48.2:
        break
print(f"{180/np.pi*theta[i]} grader. cos(theta) = {np.cos(theta[i])}")

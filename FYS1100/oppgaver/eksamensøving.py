import numpy as np
import matplotlib.pyplot as plt

g = 9.81
l = 1
b = 0.5
m = 3

tMax = 10
dt = 0.001

n = int(tMax/dt)
dtheta = np.zeros(n)
theta = np.zeros(n)
theta[0] = np.pi/2

for i in range(n-1):
    v = l*dtheta[i]
    ddtheta = -g/l*np.sin(theta[i])-b/(m*l)*v
    dtheta[i+1] = dtheta[i] + ddtheta*dt
    theta[i+1] = theta[i] + dtheta[i+1]*dt
    if theta[i+1] <=0:
        break
print(v)

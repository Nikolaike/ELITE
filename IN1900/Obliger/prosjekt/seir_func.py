from ODESolver import *

import matplotlib.pyplot as plt
import numpy as np
def SEIR(u,t):
    beta = 0.4; r_ia = 0.1; r_e2=1.25;
    lmbda_1=0.33; lmbda_2=0.5; p_a=0.4; mu=0.2;
    S, E1, E2, I, Ia, R = u
    N = sum(u)
    dS = -beta*S*I/N - r_ia*beta*S*Ia/N - r_e2*beta*S*E2/N
    dE1 = beta*S*I/N + r_ia*beta*S*Ia/N + r_e2*beta*S*E2/N - lmbda_1*E1
    dE2 = lmbda_1*(1-p_a)*E1 - lmbda_2*E2
    dI = lmbda_2*E2 - mu*I
    dIa = lmbda_1*p_a*E1 - mu*Ia
    dR = mu*(I + Ia)
    return [dS, dE1, dE2, dI, dIa, dR]

def test_SEIR():
    success = False
    calculated = SEIR([1,1,1,1,1,1],0)
    expected = [-0.156666666666, -0.1733333333333, -0.302, 0.3, -0.068, 0.4]
    for i in range(len(calculated)):
        if abs(calculated[i]-expected[i])<= 1e-10:
            success = True
        else:
            assert success, f"expected {expected} got {calculated}"
    assert success, f"expected {expected} got {calculated}"
test_SEIR()

def solve_SEIR(T,dt,S_0,E2_0):
    solver = ForwardEuler(SEIR)
    solver.set_initial_condition([S_0,0,E2_0,0,0,0])
    DT = int(T/dt)
    time_points = np.linspace(0,T,DT+1)
    u,t = solver.solve(time_points)
    return u,t
def plot_SEIR(u,t):
    S = []; I = []; Ia = []; R = []
    for i in range(len(u)):

        S.append(u[i][0])
        I.append(u[i][3])
        Ia.append(u[i][4])
        R.append(u[i][5])
    plt.plot(t,S, label = "S")
    plt.plot(t,I, label = "I")
    plt.plot(t,Ia, label = "Ia")
    plt.plot(t,R, label = "R")
    plt.legend()
    plt.show()

plot_SEIR(solve_SEIR(150,1,5e6,100)[0],solve_SEIR(150,1,5e6,100)[1])


"""
Terminal>py .\seir_func.py
"""

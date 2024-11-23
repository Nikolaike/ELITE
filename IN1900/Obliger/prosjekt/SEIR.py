from ODESolver import *
import matplotlib.pyplot as plt
import numpy as np

class ProblemSEIR:
    def __init__(self,beta,r_ia=0.1,r_e2=1.25,lmbda_1=0.33,lmbda_2=0.5,p_a=0.4,mu=0.2):
        self.r_ia = r_ia
        self.r_e2 = r_e2
        self.lmbda_1 = lmbda_1
        self.lmbda_2 = lmbda_2
        self.p_a = p_a
        self.mu = mu
        if isinstance(beta, (float, int)):
            self.beta = lambda t: beta
        elif callable(beta):
            self.beta = beta
    def set_initial_condition(self,S_0,E2_0):
        self.S_0 = S_0; self.E2_0 = E2_0
        self.U0 = [S_0,0,E2_0,0,0,0]
    def get_population(self):
        return self.S_0 + self.E2_0
    def __call__(self,u,t):
        r_ia = self.r_ia; r_e2=self.r_e2;
        lmbda_1=self.lmbda_1; lmbda_2=self.lmbda_2; p_a=self.p_a; mu=self.mu;
        S, E1, E2, I, Ia, R = u
        N = sum(u)
        dS = -self.beta(t)*S*I/N - r_ia*self.beta(t)*S*Ia/N - r_e2*self.beta(t)*S*E2/N
        dE1 = self.beta(t)*S*I/N + r_ia*self.beta(t)*S*Ia/N + r_e2*self.beta(t)*S*E2/N - lmbda_1*E1
        dE2 = lmbda_1*(1-p_a)*E1 - lmbda_2*E2
        dI = lmbda_2*E2 - mu*I
        dIa = lmbda_1*p_a*E1 - mu*Ia
        dR = mu*(I + Ia)
        return [dS, dE1, dE2, dI, dIa, dR]
def test_ProblmeSEIR():
    success1 = False
    success2 = False
    test = ProblemSEIR(0.4)
    test.set_initial_condition(5e7, 200)
    population_test = test.get_population()
    population_expected = 5e7+200
    if abs(population_test-population_expected)<= 1e-10:
        success1 = True
        """ tester både om get_population og set_initial_condition fordi hvis testen er sann må
        begge funke, siden set_initial_condition blir brukt i get_population"""
    call_calculated = test([2,2,2,2,2,2],0)
    call_expected = [-0.31333333333333335, -0.3466666666666667, -0.604, 0.6, -0.136, 0.8]
    for i in range(len(call_calculated)):
        if abs(call_calculated[i]-call_expected[i])<= 1e-10:
            success2 = True
        else:
            assert success2, f"expected {call_expected} got {call_calculated}"
    assert success1, f"expected {population_expected} got {population_test}"


test_ProblmeSEIR()

class SolverSEIR:
    def __init__(self, problem,T,dt):
        self.problem = problem
        self.T = T
        self.dt = dt
    def solve(self,method=ForwardEuler):
        solver = method(self.problem)
        solver.set_initial_condition(self.problem.U0)
        DT = int(self.T/self.dt)
        time_points = np.linspace(0,self.T, DT)
        u,t = solver.solve(time_points)
        self.u = u; self.t = t

    def plot(self,states):
        list = ["S","E1","E2","I","Ia","R"]
        u = self.u ; t = self.t
        for i in range(len(states)):
            l = []
            for n in range(len(u)):
                l.append(u[n][list.index(states[i])])
            plt.plot(t,l,label=f"{states[i]}")
            plt.legend()
        plt.show()

if __name__ == "__main__":
    test_ProblmeSEIR()
    S_0 = 5e6
    E2_0 = 100
    problem = ProblemSEIR(beta=0.4)
    problem.set_initial_condition(S_0,E2_0)
    solver = SolverSEIR(problem,T=150,dt=1.0)
    solver.solve()
    solver.plot(["S","I","Ia","R"])

from SEIR import *
from ODESolver import *
def outbreak_Norway(beta,num_days,dt):
    S_0 = 5e6
    E2_0 = 100
    problem = ProblemSEIR(beta)
    problem.set_initial_condition(S_0,E2_0)
    solver = SolverSEIR(problem,num_days,dt)
    solver.solve()
    solver.plot(["I","Ia"])
    I = [i[3] for i in solver.u]
    print(f"Det høyeste antallet smittede er {int(max(I))} og hvis {int(max(I)*0.05)} trenger ventilatorer vil {int(max(I)*0.05-700)} ikke ha ventilatorer")
outbreak_Norway(0.33,150,1)


if __name__ == "__main__":
    def beta(t):
        if t <= 30: return 0.33
        else: return 0.083
    outbreak_Norway(beta, 150,1)

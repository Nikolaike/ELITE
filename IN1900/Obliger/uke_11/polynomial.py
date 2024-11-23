class Quadratic:
    def __init__(self, coe):
        self.coe = coe
    def __call__(self,x):
        s = 0
        for i in range(len(self.coe)):
            s+= self.coe[i]*x**(len(self.coe)-(i+1))
        return s
    def __str__(self):
        return f"{self.coe}"
q = Quadratic([1,3,2])
print(q)
print(q(1))
print(q(2))

class cubic(Quadratic):
    def __init__(self,coe):
        self.coe = coe
    def derivative(self):
        return Quadratic([3*coe[0],2*coe[1],coe[2]])
c = cubic([1,3,2,4])
print(c)
print(c(1))
print(c(2))
"""
Terminal> py .\polynomial.py
[1, 3, 2]
6
12
[1, 3, 2, 4]
10
28
"""

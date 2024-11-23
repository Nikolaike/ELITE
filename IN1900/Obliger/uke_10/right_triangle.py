import numpy as np
import matplotlib.pyplot as plt
#a)
class RightTriangle:
    def __init__(self, a, b):
        if a < 0 or b < 0:
            raise ValueError
        self.a = a
        self.b = b
        self.c = np.sqrt(a**2+b**2)
    def __str__(self):
        return f"Hypotenusen er {self.c:.2f}"
    def plot_triangle(self):
        x = [0,self.a, 0,0]
        y = [0,0,self.b,0]
        plt.plot(x,y)
        plt.axis("equal")
        plt.show()

#b)
triangle1 = RightTriangle(1,1)
triangle2 = RightTriangle(3,4)
print(triangle1)
print(triangle2)
#c)
def test_RightTriangle():
    success = False
    try:
        triangle3 = RightTriangle(1,-1)
    except ValueError:
        success = True
    assert success
test_RightTriangle()
#d)
triangle2.plot_triangle()


"""
Terminal>py .\right_triangle.py
Hypotenusen er 1.41
Hypotenusen er 5.00
"""

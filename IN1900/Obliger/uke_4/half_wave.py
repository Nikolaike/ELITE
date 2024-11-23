from math import sin, pi
def f(x):
    if sin(x) > 0:
        return sin(x)
    else:
        return 0

def test_f():
    expected1 = 1
    computed1 = f(pi/2)
    expected2 = 0
    computed2 = f((3*pi)/2)
    tol = 1E-14
    success1 = abs(expected1 - computed1) < tol
    success2 = abs(expected2 - computed2) < tol
    msg1 = f"computed={computed1} != {expected1}(expected)"
    msg2 = f"computed={computed2} != {expected2}(expected)"
    assert success1, msg1
    assert success2, msg2
test_f()
"""
Terminal> python .\half_wave.py

Vil ikke få output siden funksjonen er riktig for de verdiene


sin((3*pi)/2) = -1, men siden vi har at sin(x) bare skal være positivt og hvis
den er negativt eller 0, så blir den 0 så tester da bare for positive verdier
og 0
"""

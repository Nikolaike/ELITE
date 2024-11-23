# a)
import numpy as np
def mean(x_list):
    x = 0
    for i in x_list:
        x += i
    return x/len(x_list)
#b)
def test_mean():
    x_list = [0.699, 0.703, 0.698, 0.688, 0.701]
    expected = np.mean(x_list)
    computed = mean(x_list)
    tol = 1E-14
    success = abs(expected - computed) < tol
    msg = f"computed={computed} != {expected}(expected)"
    assert success, msg
test_mean()
#c)
def standard_deviation(x_list):
    mean1 = mean(x_list)
    x = 0
    for i in x_list:
        x += (i-mean1)**2
    return(np.sqrt(x / (len(x_list))))
#d)
def test_standard_deviation():
    x_list = [0.699, 0.703, 0.698, 0.688, 0.701]
    expected = np.std(x_list)
    computed = standard_deviation(x_list)
    tol = 1E-14
    success = abs(expected - computed) < tol
    msg = f"computed={computed} != {expected}(expected)"
    assert success, msg
test_standard_deviation()

"""
Terminal> python .\statistics.py
ingen output siden begge funksjonene funker

"""

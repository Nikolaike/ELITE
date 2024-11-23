def x(n):
    if n > 1:
        return x(n-1) + x(n-2)
    return n
for i in range(1, 16):
    print(x(i))

"""
Terminal>python .\fibonacci.py
1
1
2
3
5
8
13
21
34
55
89
144
233
377
610
"""

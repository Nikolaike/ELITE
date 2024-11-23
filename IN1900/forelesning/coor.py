a = 0
b = 48
n = 10

#a) Bruke for-løkke:
x = []
h = (b-a)/n
for i in range(n+1):
    x.append(a + i*h)
print(x)

#b) bruke list comprehension:
h = (b-a)/n

x = [a + i*h for i in range(n+1)]
print(x)

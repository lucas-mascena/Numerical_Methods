from math import sin, pi
f = lambda x:  x*sin(x)
a = float(input('a = '))
b = 2*pi
n = int(input('n = '))
h = (b-a)/n
S = 0
for i in range(n+1):
    S += f(a + i*h)
    S += f(i*h)
S = S - f(n*h)
Integral = 0.5*h*S
print(Integral)

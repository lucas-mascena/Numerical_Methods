from math import log, e, exp

f = lambda x: x - (e**x - 4*x**2 )/(e**x - 8*x)
tol = 0.01
x0 = float(input('Input initial value!= 0: '))

for i in range(1,30):
    xn = f(x0)
    if abs(xn-x0)<tol:
        break
        print("Root: ", xn)
    x0 = xn
print("root = ", xn)
print("Number of iterations: ", i)

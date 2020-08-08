from math import cos, pi, exp

f0 = lambda x: cos((pi*(x+1))/8)+0.2*x-0.8
f1 = lambda x: 4*x**2-exp(x)
f1_  = lambda x: 8*x-exp(x)
f2 = lambda x: x**3-2*x**2-4*x+3
f3 = lambda x: x**3+4.0001*x**2+4.002*x+1.101
fneeded = [f0,f1,f1_,f2,f3]
e = int(input("Input number [0;4] of the function needed: "))
f = fneeded[e]

x1 = float(input("Input x1: "))
x2 = float(input("Input x2: "))

if (f(x1)*f(x2)<0):
    print("A raiz está no intervalo.")
elif (f(x1)*f(x2)==0):
    print("Pelo menos um dos valores é raiz de f(x)")
else:
    print("A raiz NÃO está no intervalo.")
    


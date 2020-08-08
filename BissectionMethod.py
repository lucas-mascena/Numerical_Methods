from math import log, e, exp
f = lambda x: exp(x)-4*x**2
x1 = float(input('Input x1 (>0): '))
x2 = float(input('Input x2 (>0): '))
#tol = 0.0001

for i in range(1,3):
    y1 = f(x1)
    y2 = f(x2)
    if y1*y2<0:
        x0 = (x1+x2)/2
        y0 = f(x0)
##    if abs(y0)<tol:
##        break
##        print("Root: ", x0)
    if y1*y0>0:
        x1 = x0
    elif y1*y0==0:
        break
        print(y1,"or", y0, "(or both) is (are) a root(s).")
    else:
        x2 = x0
print("root = ", x0)
print("Number of iterations: ", i)
            
        

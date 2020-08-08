'''
Interpolation Methods in Scipy
'''
'''
x = [0,20,40,60,80,100]
y = [26.0,48.6,61.6,71.2,74.8,75.2]
from scipy.interpolate import interp1d, lagrange
#f = interp1d(x,y, 'quadratic')
f = interp1d(x,y, 'cubic')
print(f(50))
'''
'''
Lagrange Method
'''
'''
L = lagrange(x, y)
print(L)
print(L(40))
'''
#################################################
'''
Curve Fitting Functions in Scipy
'''
# Linear Regression:
'''
from scipy.stats import linregress
x = [3,4,5,6,7,8]
y = [0,7,17,26,35,45]
L = linregress(x,y)
print(L)
print(L, slope)
print(L, intercept)
print('y = (%.2f) + (%.2f)x'%(L.intercept, L.slope))
a,b = curve_fit(f,x,y)
'''
# Curve Fitting
from scipy.optimize import curve_fit
x = [3,4,5,6,7,8]
y = [0,7,17,26,35,45]
def f2(x,a0,a1,a2):
    return a0 + a1*x + a2 * x**2
def f3(x,a0,a1,a2,a3):
    return a0 + a1*x + a2 * x**2 + a3 * x**3
a,b = curve_fit(f3, x, y)
print(a)
a,_ = curve_fit(f3,x,y)
print(a)


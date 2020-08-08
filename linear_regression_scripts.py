'''
For-loop method to search for the parameters
a and b of a straight line equation.
'''
#data points and constants:
x = [3,4,5,6,7,8]
y = [0,7,17,26,35,45]
n = len(x)
#initial value of summation variables:
sumx = sumxy = sumx2 = sumy = 0 
for i in range(n):
    sumx += x[i] 
    sumy += y[i]
    sumx2 += x[i]**2
    sumxy += x[i]*y[i]
xm = sumx/n
ym = sumy/n
#Calculates a and b:
a = (ym*sumx2 - xm*sumxy)/(sumx2 - n*xm**2)
b = (sumxy-xm*sumy)/(sumx2 - n*xm**2)
#Results:
print('The straight line equation:')
print('y = (%.3f) + (%.3f)x' % (a,b))
'''
Numpy library based method to search for parameters
a and b of a straight line equation.
'''
a = b = 0
#import numpy as np
from numpy import array, sum, mean
#arrays and constants:
x = array([3,4,5,6,7,8], float)
y = array([0,7,17,26,35,45], float)
n = len(x)
#Calculates a and b parameters:
a = (mean(y)*sum(x**2) - mean(x)*sum(x*y))/(sum(x**2)-(n*mean(x)**2))
b = (sum(x*y) - (mean(x)*sum(y)))/(sum(x**2) - (n*mean(x)**2))
#Results:
print('The straight line equation:')
print('y = (%.3f) + (%.3f)x' % (a,b))


'''
Linear Interpolation Method
'''
'''
time = [0,20,40,60,80,100]
temp = [26.0,48.6,61.6,71.2,74.8,75.2]
#y = lambda xp, x1, x2, y1, y2: y1+((y2-y1)/(x2-x1))*(xp-x1)
#y(50,40,60,61.6,71.2)
def y(xp, x, y):
    for i, xi in enumerate(x):
        if xp < xi:
            return y[i-1]+((y[i]-y[i-1])/(x[i]-x[i-1]))*(xp-x[i-1])
        else:
            print('Given x-value is out of range.')
temp50 = y(50, time, temp)
print('The temperature = ', temp50)
'''
'''
Lagrange's Method:
'''
x=[0,20,40,60,80,100]
y=[26.0,48.6,61.6,71.2,74.8,75.2]
m = len(x) #length of x list (or array)
xp = float(input('Enter x: '))
yp = 0
for i in range(m):
    L = 1
    for j in range(m):
        if j != i:
            L *= (xp-x[j])/(x[i]-x[j])
    yp += y[i]*L
print('For x = %.1f, y = %.1f' % (xp,yp))

    

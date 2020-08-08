import numpy as np
from math import exp
import matplotlib.pyplot as plt
'''
Solução do item 1:
'''

#Constantes e precisão(e):
t1 = 1021416  
ni = 800000
v = 50000
tol = 1e-6

# Função que define o número de habitantes (n), em função de lambda (l):
n = lambda l: ni*exp(l*t1)+(v*(l**-1)*(exp(l*t1)-1))


#Implementação do método da Bissecção:
l1 = -10000000
l2 = -10000000000

n1 = n(l1)
n2 = n(l2)
n0 = -1

for i in range(100):
    if n1*n2<0:
        l0 = (l1+l2)/2
        n0 = n(l0)
        if n1*n0>0:
            l1 = l0
        else:
            l2 = l0
    else:
        break
        print('Raiz não está no intervalo.')

'''
# Implementação do método de Newton:
for i in range(1,30):
    ln = n(l0)
    if abs(ln-l0)<tol:
        break
        print("Root: ", ln)
    l0 = ln
print("root = ", ln)
print("Number of iterations: ", i)
'''
#Solução do item 2:
'''
A = np.arran([[32,8 ,8, 0, 0 ,0 ,0 ,0 ,0,0],[4, 25,-3 ,6, 0, 0, 0, 10, 0 ,0],[4,-3, 30, 8, 0, 2 ,0,-9 ,0 ,0],[ 0, 3, 4, 23.5, 4,-1, 0, 0 ,0 ,0],[0, 0, 0, 8 ,17 ,3, 2,-1 ,0 ,0],[
0, 0, 2,-2, 3 ,15 ,1,-3 ,3 ,0],[0 ,0, 0, 0 ,2 ,1 ,21,-4,-7 ,0],[0 ,10,-9, 0,-1,-3,-4, 52,-1 ,4],[0 ,0 ,0 ,0 ,0 ,3,-7,-1 ,14 ,0],[0 ,0 ,0 ,0 ,0 ,0 ,0 ,4 ,0 ,24]], float)
'''

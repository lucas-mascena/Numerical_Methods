import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

#Dados:
#Referentes à tabela 1:
tabela1x = np.arange(1,21)
tabela1y = np.array([9, 16, 21, 25, 33, 48, 61, 75, 91, 27, 148, 175, 244,375,
450, 62, 674, 860, 1100, 1331 ], float)

#Referentes à tabela 2:
tabela2x = np.arange(21,41)
tabela2y = np.array([1696, 1995, 2314, 2606, 3024, 3523, 4032, 5387,
6507, 7560, 8078, 8911, 10328, 10869, 12210, 13197, 13832, 14393,
14967,15729], float)

#Versões linearizadas de y, para as tabelas 1 e 2, respectivamente:
tabela1Log = np.array([2.19722, 2.77259, 3.04452, 3.21888, 3.49651,
3.8712, 4.11087, 4.31749, 4.51086, 4.84419, 4.99721, 5.16479, 5.49717,
5.92693, 6.10925, 6.3315, 6.51323, 6.75693, 7.00307, 7.19369], float)
tabela2Log = np.array([7.43603, 7.5984, 7.74673, 7.86557, 8.01434,
8.16707, 8.30202, 8.59174, 8.78063, 8.93063, 8.9969, 9.09504, 9.24261,
9.29367, 9.41001, 9.48774, 9.53474, 9.5745, 9.6136, 9.66326], float)
'''
#Implementando o MMQ p/ um polinômio de grau 1:
#C/ dados da tabela 1:
m = len(tabela1x)
n = 1
A = np.zeros((n+1,n+1))
B = np.zeros(n+1)
a = np.zeros(n+1)
for  row in range(n+1):
    for col in range(n+1):
       if row == 0 and col == 0:
           A[row,col] = m
           continue
       A[row, col] = np.sum(tabela1x**(row+col))
    B[row] = np.sum(tabela1x**row * tabela1Log)
a = np.linalg.solve(A, B)
print('Para tabela 1 : ')
print('f(x) =  %.3f'%a[0])
for i in range(1, n+1):
    print(' %+.3f x^%d' % (a[i],i))
    
#Para Tabela 2:
m = len(tabela2x)
n = 1
A = np.zeros((n+1,n+1))
B = np.zeros(n+1)
a = np.zeros(n+1)
for  row in range(n+1):
    for col in range(n+1):
       if row == 0 and col == 0:
           A[row,col] = m
           continue
       A[row, col] = np.sum(tabela2x**(row+col))
    B[row] = np.sum(tabela2x**row * tabela2Log)
a = np.linalg.solve(A, B)
print('Para tabela 2 : ')
print('f(x) =  %.3f'%a[0])
for i in range(1, n+1):
    print(' %+.3f x^%d' % (a[i],i))
'''

#Define uma função polinomial de grau 1:
def f(x,a0,a1):
    return a0 + a1*x

#Retorna uma função de ajuste de acorodo com os dados:
a,_ = curve_fit(f, tabela1x, tabela1Log)

#print('Equação p/ tabela 1:')
#print('y = (%.3f) + (%.3f)x'%(a[0],a[1]))
c,_ = curve_fit(f, tabela2x, tabela2Log)
#print('Equação p/ tabela 2:')
#print('y = (%.3f) + (%.3f)x' % (c[0],c[1]))
'''
#Plotando gráfico para (reta 1 x reta 2):
plt.plot(tabela1x, f(tabela1x, *a), 'r-',
label='reta 1: %5.2f + %5.2f x' % tuple(a))
plt.plot(tabela2x, f(tabela2x, *a), 'b-',
label='reta 2: %5.2f + %5.2f x' % tuple(c))
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
'''


#Obtendo os coeficientes das curvas exponenciais:

#P/ curva 1:
c1 = np.exp(a[0])
c2 = np.exp(a[1])

#P/ curva 2:
c3 = np.exp(c[0])
c4 = np.exp(c[1])

#Definindo os intervalos e funções :
x1 = np.arange(21)
x2 = np.arange(21, 41)
y1 = c1*(c2**x1)
y2 = c3*(c4**x2)

#Plotando curvas:
plt.plot(x1,y1, 'r-',
label='curva 1: %5.2f.%5.2f^x' %(c1,c2))
plt.plot(x2, y2, 'b-',
label='curva 2: %5.2f.%5.2f^x' %(c3,c4))
plt.scatter(tabela1x,tabela1y, color="green",s=10)
plt.scatter(tabela2x,tabela2y, color="green",s=10)
plt.title('Curvas de Ajuste')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()


import math
import numpy as np

print("Введите количество уравнений: ")
n = int(input())
k=1
#sum=0
b=[]
x=[]
xn=[0 for i in range(n)]
print("Введите матрицу А: ")
a = [list(map(float, input().split())) for i in range(n)]
print("Введите вектор b: ") 
for i in range(n):
  b.append(float(input()))
for i in range(n): 
 for j in range(n):
  print(a[i][ j],"*x" ,j , end='')
  if j < len(a[i]) - 1:
   print(" + ",end='')
 print(" = ",b[i])
print('Введите точность: ')
eps = float(input())
print('Введите начальное приближение: ')
for i in range(n):
  x.append(float(input()))
  xn[i]=x[i]
while True:
  norma=0
  for i in range(n):
    sum=0
    for j in range(n):
      if (i!=j):
        sum+=a[i][j]*xn[j]
    x[i]=(b[i]-sum)/a[i][i]
    if (math.fabs(x[i]-xn[i]) > norma):
        norma=math.fabs(x[i]-xn[i])
  print('Кол-во итераций: ', k)
  for i in range(n):
    print("x[", i+1, "]=", round(x[i],7))
    xn[i]=x[i]
  k=k+1
  if (norma <= eps):
    break
temp = np.zeros((4, 1))
r = np.zeros((4, 1))
print('Вектор невязки:')
for i in range(len(a)):
    temp[i] = 0
    for j in range(len(a)):
        temp[i] += x[j] * a[i][j]
    r[i] = temp[i] - b[i]
    print('r[', i + 1, '] =', "%.12f" % (r[i]), end = '\n')
 

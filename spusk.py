import math
import numpy as np

print("Введите количество уравнений: ")
n = int(input());
k=1
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
r = [0 for i in range(n)]
r1 = []
while True:
  norma=0
  for i in range (n):
    d=0
    for j in range(n):
      d+=a[i][j]*xn[j]
    r[i]=d-b[i]   
  r1 = np.dot(a, r)
  
  for i in range(n):
    sum=0
    p=0
    l=0
    for j in range(n):
      sum+=a[i][j]*xn[j]
    p=np.dot(r,r)
    l=np.dot(r,r1)
    x[i]=(b[i]-sum+(l/p)*xn[i])*p/l
    
  for i in range(n):
    v=0
    for j in range(n):
      v+=a[i][j]*xn[j]
    norma+=(v-b[i])**2
  print('Кол-во итераций: ', k)
  print('Параметр t равен: ', round(p/l, 15))
  for i in range(n):
    print("x[", i+1, "]=", round(x[i],7))
    xn[i]=x[i]
  k=k+1
  if (math.sqrt(norma) <= eps):
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
 

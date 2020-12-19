import math
def Kvadr(a, b, n):
 
 #x=[0 for i in range(n)]
 for i in range(n):
   for j in range(n):
     if (A[i][j] != A[j][i]):
       print("Матрица не симметричная")
       return 0
 x=[0 for i in range(n)]
 y=[0 for i in range(n)]
 U=[]
 for i in range(n):
    U.append([0] * n)

 for i in range(n):
    t = 0
    for k in range(i):
        t = t + U[k][i] * U[k][i]
    if ((A[i][i]-t)<0):
        print("Матрица не положительно определенная")
        return 0
    U[i][i] = math.sqrt(A[i][i] - t)
    if (U[i][i]==0):
    	print("Матрица не положительно определенная")
    	return 0
    for j in range(i,n,1):
        t = 0
        for k in range(i):
             t = t + U[k][i] * U[k][j]
        U[i][j] = (A[i][j] - t) / U[i][i]
 for i in range(n):
    for j in range(n):
        print(U[i][j], " ", end='')
    print()
 for i in range(n):
    t = 0
    for k in range(i):
        t = t + U[k][i] * y[k]
    y[i] = (b[i] - t) / U[i][i]
 for i in range(n - 1, -1, -1):
    t = 0
    for k in range(i+1, n, 1):
        t = t + U[i][k] * x[k]
    x[i] = (y[i] - t) / U[i][i]
 for i in range(n):
    print("x", i, "= ", x[i])
 return x

print("Введите количество уравнений: ")
n = int(input());

b=[]
print("Введите матрицу А: ")
A = [list(map(int, input().split())) for i in range(n)]
print("Введите вектор b: ") 
for i in range(n):
  b.append(int(input()))
for i in range(n): 
 for j in range(n):
  print(A[i][ j],"*x" ,j , end='')
  if j < n - 1:
   print(" + ",end='')
 print(" = ",b[i])
Kvadr(A, b, n)
 

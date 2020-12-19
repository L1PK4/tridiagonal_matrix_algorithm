import math
import numpy as np
def Kvadr(a, b, n):
	"""
	
	"""
	x=[0 for i in range(n)]
	y=[0 for i in range(n)]
	s=[]
	u=[]
	ut=[]
	a1=[]
	for i in range(n):
		s.append([0] * n)
	for i in range(n):
		u.append([0] * n)
	for i in range(n):
		ut.append([0] * n)
	for i in range(n-1):
		a1.append([0]  * (n-1))

	for i in range(n):
		sum=0
		for k in range(2):
			sum=sum+u[k][i]*u[k][i]
		if ((a[i][i]-sum)<0):
			print("Матрица не положительно определенная")
			return 0
		u[i][i]=math.sqrt(a[i][i]-sum)
		if (u[i][i]==0):
			print("Матрица не положительно определенная")
			return 0
		for j in range(i+1,n,1):
			sum=0
			for  k in range(i):
				sum = sum + u[k][i] * u[k][j]
			u[i][j]=(a[i][j]-sum)/u[i][i]
	for i in range(n):
		for j in range(n):
			ut[j][i]=u[i][j]
	for i in range(n):
		for j in range(n):
			print(u[i][j], ' ', end='')
		print('')

	y[0]=b[0]/ut[0][0]
	for i in range(n):
		sum=0
		for j in range(i):
			sum=sum+ut[i][j]*y[j]
		y[i]=(b[i]-sum)/ut[i][i]
	print("Получили ответ: ")
	x[n-1]=y[n-1]/u[n-1][n-1]
	print("x[", n-1, "]=", x[i])
	for i in range(n-2, -1, -1):
		sum=0
		for j in range(n-1, i, -1):
			sum=sum+u[i][j]*x[j]
		x[i]=(y[i]-sum)/u[i][i]
		print("x[", i, "]=", x[i])
	temp = np.zeros((4, 1))
	r = np.zeros((4, 1))
	print('Вектор невязки:')
	for i in range(len(a)):
		temp[i] = 0
		for j in range(len(a)):
			temp[i] += x[j] * a[i][j]
		r[i] = temp[i] - b[i]
		print('r[', i + 1, '] =', "%.12f" % (r[i]), end = '\n')
	return x


print("Введите количество уравнений: ")
n = int(input())

b=[]
print("Введите матрицу А: ")
a = [list(map(int, input().split())) for i in range(n)]
print("Введите вектор b: ") 
for i in range(n):
  b.append(float(input()))
for i in range(n): 
 for j in range(n):
  print(a[i][ j],"*x" ,j , end='')
  if j < len(a[i]) - 1:
   print(" + ",end='')
 print(" = ",b[i])
l = True
for i in range(n):
	for j in range(n):
		if a[i][j]!=a[j][i]:
			l = False
if l==False:
	print("Матрица не симметричная")
else:
	Kvadr(a, b, n)
 

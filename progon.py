print("Введите количество уравнений: ")
n1 = int(input());
b=[]
x = [0 for i in range(n1)]
print("Введите матрицу А: ")
a = [list(map(int, input().split())) for i in range(n1)]
print("Введите вектор b: ") 
for i in range(n1):
  b.append(int(input()))
for i in range(n1): 
 for j in range(len(a[i])):
  print(a[i][ j],"*x" ,j , end='')
  if j < len(a[i]) - 1:
   print(" + ",end='')
 print(" = ",b[i])

n=n1-1
eps = [0 for i in range(n)]
et = [0 for i in range(n1)]
eps[0]=-a[0][1]/a[0][0]
et[0]=b[0]/a[0][0]
 
for i in range(n):
    z=a[i][i]+a[i][i-1]*eps[i-1]
    eps[i]=-a[i][i+1]/z
    et[i]=(b[i]-a[i][i-1]*et[i-1])/z

x[n]=(b[n]-a[n][n-1]*et[n-1])/(a[n][n]+a[n][n-1]*eps[n-1])
et[n] = x[n]

for i in range(n1):
  for j in range(n1):
    if i == j:
      print(1, ' ', end='')
      if i != n:
        print(eps[i], ' ', end='')
    else:
      print(0, ' ', end='')
  print(et[i])

for i in range(n-1, -1, -1):
  x[i]=eps[i]*x[i+1]+et[i]
 
print("Получили ответ: ")
for i in range(n1): 
  print("x", i, "=", x[i])

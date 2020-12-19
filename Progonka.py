def Progonka(a, b, n):
    y = [0 for i in range(n+2)]
    x = [0 for i in range(n+2)]
    for i in range(2, n-1, 1):
        for j in range(n+2):
            b[i] = a[i][j]*b[i-1]+a[i+1][j]*b[i]+a[i][j+1]*b[i+1]
    for i in range(n-1):
        for j in range(n+2):
             x[i+1]=a[i][j]/b[i]
    for i in range(n-1):
        k = 0
        for j in range(n+2):
            if k<n:
                y[i]=

print("Введите количество уравнений: ")
n = int(input());

b=[]
print("Введите матрицу А: ")
a = [list(map(int, input().split())) for i in range(n)]
print("Введите вектор b: ") 
for i in range(n):
  b.append(int(input()))
for i in range(n): 
 for j in range(len(a[i])):
  m = len(a[i])
  print(a[i][ j],"*x",j , end='')
  if j < (len(a[i]) - 1):
   print(" + ",end='')
 print(" = ",b[i])
for i in range(n):
    for j in range(len(a[i])):
        if (len(a[i])==n+2):
            Progonka(a, b, n)
        else:
            print("Матрица не трехдиагональная")
            break

import numpy as np
def Gauss(a, b, n, m): 
  eps = 0.00001  #точность
  x = [0 for i in range(n)]
  k = 0
  if n > m:
    u = m
  else:
    u = n
  while k < u:
    #Поиск строки с максимальным a[i, k]
    max = abs(a[k][k])
    ind = k
    for i in range(k+1, u, 1):
      if abs(a[i][k]) > max:
        max = abs(a[i][k])
        ind = i
    # Перестановка строк
    if max < eps: 
      #нет ненулевых диагональных элементов
        for i in range(n): 
          for j in range(m):
            print(a[i][j], ' ', end='')
          print(b[i])
        print('')
        for i in range(np.linalg.matrix_rank(a), n, 1):
          if (b[i] != 0):
            print("Нет решений")
            return 0         
        print("Решений бесконечно много")
        return 0
    for j in range(0, m, 1): 
      t = a[k][j];
      a[k][j] = a[ind][j];
      a[ind][j] = t;
    t = b[k];
    b[k] = b[ind];
    b[ind] = t;
    
    #Приводим к треугольному виду
    for i in range(k, n, 1): 
      t = a[i][k]
      if abs(t) < eps:
          continue #нулевой коэффициент пропустить
      for j in range(0, m, 1): 
        a[i][j] = a[i][j] / t
      b[i] = b[i] / t;
      if i == k:
          continue 
      for j in range(0, m, 1):
        a[i][ j] = a[i][ j] - a[k][ j]
      b[i] = b[i] - b[k]
    k=k+1

  for i in range(n):
    for j in range(m):
      print(a[i][j], ' ', end='')
    print('')
    
  #обратная подстановка
  for k in range(u-1, -1, -1):
    x[k] = b[k]
    for i in range(0, k, 1):
      b[i] = b[i] - a[i][k] * x[k]
  print("Получили ответ: ")
  for i in range(m): 
    print("x",i, "=", x[i])
  return x

print("Введите количество уравнений: ")
n = int(input());

b=[]
print("Введите матрицу А: ")
a = [list(map(float, input().split())) for i in range(n)]
print("Введите вектор b: ") 
for i in range(n):
  b.append(float(input()))
for i in range(n): 
 for j in range(len(a[i])):
  m = len(a[i])
  print(a[i][ j],"*x" ,j , end='')
  if j < len(a[i]) - 1:
   print(" + ",end='')
 print(" = ",b[i])
Gauss(a, b, n, m)

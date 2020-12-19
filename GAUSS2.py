def Gauss(a, b, n): 
  eps = 0.00001  #точность
  x = [0 for i in range(n)]
  k = 0
  while k < n:
    #Поиск строки с максимальным a[i, k]
    max = abs(a[k][k])
    ind = k
    for i in range(k+1, n, 1):
      if abs(a[i][k]) > max:
        max = abs(a[i][k])
        ind = i
    # Перестановка строк
    if max < eps: 
      #нет ненулевых диагональных элементов
      print("Решений бесконечно много")
      return 0
    for j in range(0, n, 1): 
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
      for j in range(n, i-1, -1): 
        a[i][j] = a[i][j] / t
      b[i] = b[i] / t;
      if i == k:
          continue 
      for j in range(i+1, n, 1):
        t = a
        a[i][ j] = a[i][ j] - a[k][ j]
      b[i] = b[i] - b[k]
    k=k+1
    
  #обратная подстановка
  for k in range(n-1, -1, -1):
    x[k] = b[k]
    for i in range(0, k, 1):
      b[i] = b[i] - a[i][k] * x[k]
  print("Получили ответ: ")
  for i in range(n): 
    print("x",i, "=", x[i])
  return x

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
  print(a[i][ j],"*x" ,j , end='')
  if j < len(a[i]) - 1:
   print(" + ",end='')
 print(" = ",b[i])
Gauss(a, b, n)

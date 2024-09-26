import numpy as np
n = int(input())
m = int(input())
mass = np.zeros((n, m))
k = 1
p = 0
while p < (n + 1) / 2:
    if k <= n * m:
        for i in range(p, m - p):
            mass[p][i] = k
            k += 1
    if k <= n * m:
        for i in range(p + 1, n - p):
            mass[i][m - p - 1] = k
            k += 1
    if k <= n * m:
        for i in range(m - p - 2, p - 1, -1):
            mass[n - p - 1][i] = k
            k += 1
    if k <= n * m:
        for i in range(n - p - 2, p, -1):
            mass[i][p] = k
            k += 1
    p += 1
print(mass) #промежуточный результат
for i in range(0,n):
    for j in range(0,m):
        mass[i][j]*=i
print (mass)
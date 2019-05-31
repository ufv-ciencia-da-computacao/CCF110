from math import radians
soma = 0
x = radians(float(input()))
for i in range(15):
  fat = 1
  for j in range(1, (2*i+1)+1):
    fat *= j
  soma += (((-1)**i)*(x**(2*i+1))) / fat
print(soma)
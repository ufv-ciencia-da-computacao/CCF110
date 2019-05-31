controlaN = N = int(input())
numPrimos = 0
j = 1
while j < controlaN+1:
  cont = 0
  for k in range(1, j+1):
    if j % k == 0:
      cont += 1
    if cont > 2:
      break
  if cont == 2:
    print(j)
  else:
    controlaN += 1
  j += 1
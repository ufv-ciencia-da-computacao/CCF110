from math import ceil
rg = 20
vetor = [int(input()) for i in range(rg)] 
for i in range(ceil(rg/2)):
  aux = vetor[i]
  vetor[i] = vetor[rg-1-i]
  vetor[rg-1-i] = aux
print(*vetor)

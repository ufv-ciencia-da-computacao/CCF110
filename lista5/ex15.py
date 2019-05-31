fator = 2
n = int(input())
vetor = []
aux = []
while n > 1:
  while n % fator == 0:
    n /= fator
    if len(vetor) > 0:
      for i in vetor:
        if (fator*i) not in vetor:
          aux.append(fator*i)
      vetor.extend(aux)
      aux = []
    else:
      vetor.append(fator)
  fator += 1
vetor.sort()
print(vetor)

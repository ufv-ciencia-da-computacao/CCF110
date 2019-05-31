list = [['Brasil', 'Italia', [10,9]], ['Brasil', 'Espanha', [5,7]], ['Italia', 'Espanha', [7,8]]]
somaFaltas = 0

for i in range(len(list)):
  somaFaltas += sum(list[i][len(list[i])-1])
print(somaFaltas)

paises = {}

for i in range(len(list)):
  for j in range(len(list[i])-1):
    if list[i][j] not in paises:
      paises[list[i][j]] = list[i][len(list[i])-1][j]
    else:
      paises[list[i][j]] += list[i][len(list[i])-1][j]

minVal = min(paises.values())
resMin = [k for k, v in paises.items() if v == minVal]
print('O(s) time(s) com menor numero de faltas:', *resMin)
maxVal = max(paises.values())
resMax = [k for k, v in paises.items() if v == maxVal]
print('O(s) time(s) com maior numero de faltas:', *resMax)

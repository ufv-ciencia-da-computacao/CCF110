nome = input()
notaAntiga = float(input())
notaNova = float(input())

nomesTransc=[]
notasTransc=[]

with open('ex4.txt', 'r') as f:
  nomeFile = f.readline()
  notasArrFile = list(map(float, f.readline().split()))
  if nome == nomeFile[:len(nomeFile)-1]:
    for i in range(len(notasArrFile)):
      if notasArrFile[i] == notaAntiga:
        notasArrFile[i] = notaNova
  notasTransc.append(notasArrFile)
  nomesTransc.append(nomeFile)

with open('ex4.txt', 'w') as f:
  for i in range(len(nomesTransc)):
    f.write(nomesTransc[i])
    for j in range(len(notasTransc[i])):  
      f.write(str(notasTransc[i][j]) + ' ')


        
      
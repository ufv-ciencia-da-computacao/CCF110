nome = input()
notaAntiga = float(input())
notaNova = float(input())

nomesTransc=[]
notasTransc=[]

with open('ex4.txt', 'r') as f:
  nomeFile = f.readline()
  notasArrFile = list(map(float, f.readline().split()))
  while nomeFile != '' and notasArrFile != '':
    if nome == nomeFile[:len(nomeFile)-1]:
      for i in range(len(notasArrFile)):
        if notasArrFile[i] == notaAntiga:
          notasArrFile[i] = notaNova
    notasTransc.append(notasArrFile)
    nomesTransc.append(nomeFile)
    nomeFile = f.readline()
    notasArrFile = list(map(float, f.readline().split()))

with open('ex4.txt', 'w') as f:
  for i in range(len(nomesTransc)):
    f.write(nomesTransc[i])
    for j in range(len(notasTransc[i])): 
      if j == len(notasTansc[i]-1):
        f.write(str(notasTransc[i][j])+'\n')
      else:
        f.write(str(notasTransc[i][j])+' ')


        
      

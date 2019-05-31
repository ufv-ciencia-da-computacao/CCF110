qtdTermos = int(input())
serie1 = 1
serie2 = 4
while qtdTermos > 0:
  if qtdTermos % 3 == 0 or qtdTermos > 3:
    print(serie1, serie2, serie2, end=" ")
    qtdTermos -= 3
    serie1 += 1
    serie2 += 1
  elif qtdTermos % 3 == 2:
    print(serie1, serie2, end=" ")
    qtdTermos -=2
    serie1 +=1 
  elif qtdTermos % 3 == 1:
    print(serie1, end=" ")
    qtdTermos -= 1
    serie1 += 1 
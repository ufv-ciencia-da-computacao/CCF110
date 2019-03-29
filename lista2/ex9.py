numImpar = 0
numPar = 0

for i in range(0,200):
    numUsuario = int(input())
    if numUsuario % 2 == 0:
        numPar+=1
    else:
        numImpar+=1
print("Quantidade de numero impar: {0}".format(numImpar))
print("Quantidade de numero par: {0}".format(numPar))
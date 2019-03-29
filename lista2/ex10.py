import math as m
qtdTermos = 0
denominador = 2
serie = 0

while qtdTermos < 51:
    denominador += 1
    if denominador % 2 != 0:
        if qtdTermos + 1 % 2 != 0:
            serie += -1/denominador ** 3
            qtdTermos += 1
        else:
            serie += +1/denominador ** 3
            qtdTermos += 1
serie += 1
pi = (serie * 32) ** (1./3)
print(pi)
qtdTermos = 0
denominador = 10
numerador = 480
serie = 0

while qtdTermos < 30:
    if qtdTermos + 1 == 0:
        serie += -numerador/denominador
    else:
        serie += numerador/denominador
    qtdTermos += 1
    numerador -= 5
    denominador += 1
print(serie)
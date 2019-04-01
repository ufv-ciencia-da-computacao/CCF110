denominador = 10
numerador = 480
serie = 0

for i in range (30):
    serie += ((-1)**(i))*(numerador/denominador)
    numerador -= 5
    denominador += 1
print(serie)
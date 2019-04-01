serie = 1
for i in range(3, 54):
    if i == 3:
        denominador = i
    elif denominador % 2 == 0:
        denominador += 3
    else:
        denominador += 2
    serie += ((-1)**(i))*(1/(denominador ** 3))
pi = (serie * 32) ** (1./3)
print(pi)
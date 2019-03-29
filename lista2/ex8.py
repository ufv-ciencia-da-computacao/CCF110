maior = menor = num = float(input())
for i in range(0,999):
    num = float(input())
    if num > maior:
        maior = num
    if num < menor:
        menor = num
print("Maior número: {0}".format(maior))
print("Menor número: {0}".format(menor))

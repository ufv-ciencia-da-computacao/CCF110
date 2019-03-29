import sys

divisor = int(input())
dividendo = int(input())
if divisor == 0:
    print("Divisao nao permitida")
    sys.exit()
quociente = dividendo // divisor
resto = dividendo % divisor
print("Quociente: ", quociente)
print("Resto: ", resto)
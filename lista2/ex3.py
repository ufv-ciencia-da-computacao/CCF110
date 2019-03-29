num = int(input())
semana = ["Segunda", "Terça", "Quarta", 
    "Quinta", "Sexta", "Sábado", "Domingo"]
if num >= 1 and num <= 7:
    print(semana[num-1])
else:
    print("Dia da semana invalido")
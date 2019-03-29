idade = int(input())
if idade < 16:
    print("Voce nao e eleitor")
elif idade < 18 and idade >= 16:
    print("Eleitor facultativo")
else:
    print("Eleitor Obrigatorio")
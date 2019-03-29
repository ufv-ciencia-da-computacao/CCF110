idade = int(input())
peso = float(input())

if idade > 12:
    if peso >= 60:
        print("Dose: {0} Gotas".format(1000/25))
    else:
        print("Dose: {0} Gotas".format(875/25))
else:
    if peso >= 5 and peso < 9:
        print("Dose: {0} Gotas".format(125/25))
    elif peso >= 9 and peso < 16:
        print("Dose: {0} Gotas".format(250/25))
    elif peso >= 16 and peso < 24:
        print("Dose: {0} Gotas".format(275/25))
    elif peso >= 24 and peso < 30:
        print("Dose: {0} Gotas".format(500/25))
    else: 
        print("Dose: {0} Gotas".format(750/25))
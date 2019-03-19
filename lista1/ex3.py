velocidadeMedia  = int(input())
tempo            = float(input())
distancia        = tempo * velocidadeMedia
combustivelGasto = distancia/12
print("Distancia: {0:.2f}km\nCombustivel Gasto: {1:.2f}l".format(distancia, combustivelGasto))
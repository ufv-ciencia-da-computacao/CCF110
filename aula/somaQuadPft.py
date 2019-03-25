maxInterval = int(input("Digite o delimitador do intervalo: "))

intervalo = []

quadPftList = [4, 9, 16, 25, 49]
count = 0

for i in range(maxInterval):
    intervalo.append(i) 

intervalo = list(reversed(intervalo))

for numQuadPft in quadPftList:
    for numIntervalo in intervalo:
        if numQuadPft - numIntervalo > 0 and numQuadPft - numIntervalo <= intervalo[0]:
            count = count + 1

print("Existem {0} pares que somados formam num quadrados perfeitos".format(count))
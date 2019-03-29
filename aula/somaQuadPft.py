# My solution to discover which sum pair is perfect square number
# Time: (n.w) where n is the length of intervalo list and w is the length of quadPftList
 
maxInterval = int(input("Digite o delimitador do intervalo: "))

quadPftList = [4, 9, 16, 25, 36, 49]
intervalo = []

count = 0

for i in range(maxInterval):
    intervalo.append(i) 

intervalo = list(reversed(intervalo))

for numQuadPft in quadPftList:
    for numIntervalo in intervalo:
        if numQuadPft - numIntervalo > 0 and numQuadPft - numIntervalo < intervalo[0]:
            count = count + 1

print("Existem {0} pares que somados formam num quadrados perfeitos".format(count/2))
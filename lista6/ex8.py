id = int(input())
vetorId = []
vetorTotPag = []
while id >= 0:
  vetorId.append(id)
  vetorTotPag.append(float(input()))
  id = int(input())
sum = 0
for x in vetorTotPag:
  sum += x
print(sum)
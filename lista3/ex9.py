qtdNum = int(input())
maior = 0
for i in range(qtdNum):
  num = float(input())
  if i == 0:
    maior = num
  if num > maior:
    maior = num
print(num)
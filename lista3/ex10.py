mediaFeminino = 0
qtdMulheres = 0
mediaTurma = 0
maior = menor = 0
for i in range(50):
  altura = float(input())
  codigo = int(input())
  while codigo != 1 and codigo != 2:
    print("Codigo Invalido")
    codigo = int(input("1-masculino/2-feminino"))
  if i == 0:
    maior = menor = altura
  if altura > maior:
    maior = altura
  if altura < menor:
    menor = altura
  if codigo == 2:
    mediaFeminino = altura
    qtdMulheres += 1
  mediaTurma += altura
print("Media de altura das mulheres: {}".format(mediaFeminino/qtdMulheres))
print("Media de altura da turma: {}".format(mediaTurma/50))
print("Maior altura da turma: {}".format(maior))
print("Menor altura da turma: {}".format(menor))
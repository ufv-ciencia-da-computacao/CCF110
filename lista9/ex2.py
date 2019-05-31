import random

nome = ['Arthur', 'Caio', 'Danielle']
sobrenome = ['Souza', 'Henrique', 'Araujo']
altura = [1.65, 1.70, 1.50]

with open('alunos.txt', 'a+') as f:
  for i in range(len(nome)):
    data = 'Nome: ' + nome[i] + ' ' + sobrenome[i] + '\nIdade: ' + str(random.randint(1,100)) + '\n' + 'Altura: ' + str(altura[i]) + '\n'
    f.write(data)

import random

nome = ['Arthur', 'Caio', 'Danielle']
sobrenome = ['Souza', 'Henrique', 'Araujo']

with open('alunos.txt', 'a+') as f:
  for i in range(len(nome)):
    data = 'Nome: ' + nome[i] + ' ' + sobrenome[i] + '\nIdade: ' + str(random.randint(1,100)) + '\n'
    f.write(data)

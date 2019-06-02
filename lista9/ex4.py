file1 = input()
file2 = input()
mat = {}

with open(file1, 'r') as f, open(file2, 'r') as g:
  notas = g.readlines()
  nomes = f.readlines() 
  for i in range(len(nomes)):
    mat[nomes[i][:len(nomes[i])]] = notas[i][:len(notas[i])]
with open('ex4.txt', 'w') as f:
  for k, v in mat.items():
    f.write(k)
    for x in v:
      f.write(x)
    f.write('\n')

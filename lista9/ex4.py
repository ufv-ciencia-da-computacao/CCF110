file1 = input()
file2 = input()
mat = {}

with open(file1, 'r') as f, open(file2, 'r') as g:
  notas = list(g.readline().split(' '))
  mat[f.readline()] = notas

with open('ex4.txt', 'w') as f:
  for k, v in mat.items():
    f.write(k)
    f.write('\n')
    for x in v:
      f.write(x + ' ')
    f.write('\n')

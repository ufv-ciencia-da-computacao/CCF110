mat = [[int(input()) for i in range(3)] for i in range(3)]

for i in range(3):
  for j in range(3):
    print("{} ".format(mat[i][j]), end='')
  print()

print()

# switching secondary with first diagonal
j = 2
for i in range(3):
  aux = mat[i][j]
  mat[i][j] = mat[i][i]
  mat[i][i] = aux
  j -= 1 

for i in range(3):
  for j in range(3):
    print("{} ".format(mat[i][j]), end='')
  print()

print()
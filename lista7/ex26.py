lin = int(input())
col = int(input())
mat = [[int(input()) for i in range(col)] for j in range(lin)]
matT = [[0 for i in range(lin)] for j in range(col)]
for i in range(col):
  for j in range(lin):
    matT[i][j] = mat[j][i]

print()
for i in range(col):
  for j in range(lin):
    print("{} ".format(matT[i][j]), end='')
  print()

print()
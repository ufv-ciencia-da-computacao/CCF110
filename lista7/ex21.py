mat = [[int(input()) for i in range(3)] for j in range(3)]

# 0 degree
for i in range(3):
  for j in range(3):
    print("{} ".format(mat[i][j]), end='')
  print()

print()

# 90 degree
for i in range(3):
  for j in range(2, -1, -1):
    print("{} ".format(mat[j][i]), end='')
  print()

print()

# 180 degree
for i in range(2, -1, -1):
  for j in range(2, -1, -1):
    print("{} ".format(mat[i][j]), end='')
  print()

print()

# 270 degree
for i in range(2, -1, -1):
  for j in range(3):
    print("{} ".format(mat[j][i]), end='')
  print()

print()

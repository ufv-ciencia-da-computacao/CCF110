def hasInverse(det):
  return True if det != 0 else False

def det(mat, tam):
  detPrim = detSec = 1
  for i in range(tam):
    for j in range(tam):
      if i == j:
        detPrim *= mat[i][j]
      if i + j == tam - 1:
        detSec *= mat[i][j]
  if tam > 1:
    return detPrim - detSec
  else:
    return detPrim

def cofat(mat, tam, ai, aj):
  vet = []
  matAux = []

  for i in range(tam):
    if i != ai:
      for j in range(tam):
        if j != aj:
          vet.append(mat[i][j])
      if len(vet) > 0:
        matAux.append(vet)
  return (-1)**(ai+aj) * det(matAux, tam-1)

def matCofat(mat, tam):
  matCofat = [[0 for i in range(tam)] for j in range(tam)]
  for i in range(tam):
    for j in range(tam):
      matCofat[i][j] = cofat(mat, tam, i, j)
  return matCofat
    

def transpose(mat, tam):
  matT = [[0 for i in range(tam)] for j in range(tam)]
  for i in range(tam):
    for j in range(tam):
      matT[i][j] = mat[j][i]
  return matT

def inverseMatrix(mat, tam, det):
  matInverse = [[0 for i in range(tam)] for j in range(tam)]
  for i in range(tam):
    for j in range(tam):
      matInverse[i][j] = (1/det) * mat[i][j]
  return matInverse

tam = 2
mat = [[int(input()) for i in range(tam)] for j in range(tam)]
if hasInverse(det(mat, tam)):
  matInverse = inverseMatrix(transpose(matCofat(mat, tam), tam), tam, det(mat, tam))  
  for i in range(tam):
    for j in range(tam):
      print("{} ".format(matInverse[i][j]), end='')
    print()
else:
  print("Nao Admite Inversa")
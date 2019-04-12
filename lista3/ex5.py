idadeDias = int(input())
anos = idadeDias // 365
idadeDias -= anos * 365
meses = idadeDias // 30
idadeDias -= meses * 30
print("{} anos, {} meses, {} dias".format(anos, meses, idadeDias))
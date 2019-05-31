ipValido = []
ipInvalido = []

with open('ip.txt', 'r') as f:
  for line in f:
    ip = list(map(int, line.split('.')))
    if ip[0] < 1 or ip[0] > 255:
      ipInvalido.append(".".join(map(str,ip)))
    elif ip[1] < 0 or ip[1] > 255 and ip[2] < 0 or ip[2] > 255 and ip[3] < 0 or ip[3] > 255:
      ipInvalido.append(".".join(map(str, ip)))
    else:
      ipValido.append(".".join(map(str, ip))) 
with open('ipValido.txt', 'w') as f:
  for x in ipValido:
    f.write(x+'\n')
with open('ipInvalido.txt', 'w') as f:
  for x in ipInvalido:
    f.write(x+'\n')

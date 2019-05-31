file1 = input()
file2 = input()

with open(file1, 'r') as f, open(file2, 'w') as g:
  for line in f:
    if line[:2] != '//':
      g.write(line)
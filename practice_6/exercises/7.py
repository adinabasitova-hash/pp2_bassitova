import shutil

with open('a.txt', 'w') as f:
  f.write('aaa')

with open('b.txt', 'w') as f:
  f.write('bbb')

shutil.copy('a.txt', 'b.txt')
with open('b.txt', 'r') as f:
    print(f.read())   # aaa
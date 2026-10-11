with open('sample.txt', 'a') as f:
  f.write('more text\n')
  f.write('even more text\n')

with open('sample.txt', 'r') as f:
    print(f.read())
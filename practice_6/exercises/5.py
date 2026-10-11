items = ['apple', 'banana', 'cherry']

with open('list.txt', 'w') as f:
  for item in items:
    f.write(item + '\n')
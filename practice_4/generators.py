def my_generator(n):
  for x in range(n+1):
    yield x * x

for value in my_generator(5):
  print(value)

  #2
n = int(input())
def my_generator(n):
  for x in range(n+1):
    if x % 2 == 0:
      yield x

for value in my_generator(n):
  print(value)

  #3
def my_generator(n):
  for x in range(n+1):
    if x % 3 == 0 and x % 4 == 0:
      yield x

for value in my_generator(18):
   print(value)

   #4
def squares(a, b):
  for x in range(a, b+1):
    yield x ** 2

for value in squares(3, 7):
  print(value)

  #5
def my_generator(n):
  for x in range(n, -1, -1):
    yield x

for value in my_generator(5):
  print(value)



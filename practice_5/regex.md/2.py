import re

string = input()
m = re.fullmatch(r'ab{2,3}', string)

if(m):
  print('Match')
else:
  print('No match')
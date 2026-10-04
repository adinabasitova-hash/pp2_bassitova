import re
string = input()
m = re.fullmatch(r'ab*', string)

if(m):
  print('Match')
else:
  print('No match')
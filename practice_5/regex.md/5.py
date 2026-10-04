import re 
string = input()

m = re.fullmatch(r'a(.+)b', string)

if(m):
  print('Match')
else:
  print('No match')
import re
string = input()

m = re.findall(r'[A-Z][a-z]+', string)
print(m)
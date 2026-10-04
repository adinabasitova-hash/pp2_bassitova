import re
string = input()

m = re.findall(r'[a-z]+_',string)
print(m)
import re
string = input()

m = re.sub(r'\s|,|\.', ':', string)
print(m)
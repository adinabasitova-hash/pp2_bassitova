import re 
string = input()

m = re.sub(r'_([a-z])', lambda m: m.group(1).upper(), string)

print(m)
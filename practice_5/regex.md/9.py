import re
string = input()

m = re.sub(r'([A-Z])', r' \1', string)

print(m.strip())
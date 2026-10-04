import re
string = input()

m = re.sub(r'([A-Z])', r'_\1', string).lower()

print(m.lstrip('_'))
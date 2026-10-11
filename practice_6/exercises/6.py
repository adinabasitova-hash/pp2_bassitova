import string
from pathlib import Path

Path('letters').mkdir(exist_ok = True)
for letter in string.ascii_uppercase:
  Path(f'letters/{letter}.txt').touch()
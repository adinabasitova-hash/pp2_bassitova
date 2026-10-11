import os, shutil
from pathlib import Path
os.makedirs("world/country/city", exist_ok=True)

for name in os.listdir('world'):
  print(name) 

Path('world/country/a.txt').write_text('aaaaaa')
Path('world/country/b.log').write_text('bbbbbb')
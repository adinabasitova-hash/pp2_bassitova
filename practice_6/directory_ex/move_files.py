from pathlib import Path
import os,shutil

for f in Path('world').rglob('*.txt'):
  print(f)

os.makedirs('world/backup', exist_ok=True)
shutil.copy('world/country/a.txt', 'world/backup/a.txt')
shutil.move('world/country/b.log', 'world/backup/b.log')
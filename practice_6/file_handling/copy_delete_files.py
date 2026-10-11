import shutil, os
from pathlib import Path
Path('backup').mkdir(exist_ok = True)
shutil.copy('sample.txt', 'backup/sample_backup.txt')

try:
   os.remove('sample.txt')
except FileNotFoundError:
   print('the file is already deleted')
   
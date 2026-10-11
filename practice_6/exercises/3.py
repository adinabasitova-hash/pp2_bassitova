import os

path = '../file_handling/write_files.py'

if os.path.exists(path):
  print('The path exists')
  print('File name: ',os.path.basename(path))
  print('Folder: ', os.path.dirname)
else:
  print('No such path')
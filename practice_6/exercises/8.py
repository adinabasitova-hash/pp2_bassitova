import os
path = 'sample.txt'

if os.path.exists(path):
  if os.path.isfile(path):
    if os.access(path, os.W_OK):
      os.remove(path)
      print('file is deleted')
    else:
      print('cannot be deleted')
  else:
    print('this is not a file')
else:
  print('there is no such path')

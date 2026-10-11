import os

path = '.'
dirs = []
files = []

for name in os.listdir(path):
  full_path = os.path.join(path, name)
  if os.path.isdir(full_path):
    dirs.append(name)
  elif os.path.isfile(full_path):
    files.append(name)

print('Папки: ', dirs)
print('Файлы: ', files)
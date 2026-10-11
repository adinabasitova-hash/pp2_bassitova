import json
with open('sample-data.json') as f:
  data = json.load(f)

print('Interface Status')
print('='*60)

print('{:50} {:20} {:10} {:10}'.format('DN', 'Description', 'Speed','MTU'))

print('{} {} {} {}'.format('-'*50, '-'*20, '-'*10, '-'*10))

for item in data['imdata']:
  attrs = item["l1PhysIf"]["attributes"]
  dn = attrs['dn']
  dscr = attrs['descr']
  speed = attrs['speed']
  mtu = attrs['mtu']

print('{:50} {:20} {:10} {:10}'.format(dn, dscr, speed, mtu))
  
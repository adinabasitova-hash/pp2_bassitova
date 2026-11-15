import psycopg2
from config import load_config
import json
import csv


def complete():
  config = load_config()
  with psycopg2.connect(**config) as con:
    with con.cursor() as cur:
      with open('schema.sql') as commands:
        cur.execute(commands.read())

      with open('procedures.sql') as p:
        cur.execute(p.read())
      con.commit()

def filter_groups(cur):
  category = input('Search by category: ').strip()
  cur.execute('''
  SELECT p.id, p.first_name, p.last_name, p.email, groups.name,
         STRING_AGG(ph.phone || COALESCE(' (' || ph.type || ')', ''), ', ')  
  FROM phonebook p
  JOIN groups ON groups.id = p.group_id
  LEFT JOIN phones ph ON ph.contact_id = p.id
  WHERE groups.name ILIKE %s
  GROUP BY p.id, groups.name                                           
  ''', (category,))
  rows = cur.fetchall()
  if not rows:
    print('No contacts in this group')
  else:
    for id, name, sur, mail, gr, tels in rows:
      print(f'{gr} | {id}. {name} {sur or ''} - {tels or "-"} || {mail or "-"}')  

def search_by_mail(cur):
  email = input('Search by the part of mail: ').strip()
  cur.execute('''
    SELECT p.id, p.first_name, p.last_name, p.email, groups.name,
           STRING_AGG(ph.phone || COALESCE(' (' || ph.type || ')', ''), ', ')  
    FROM phonebook p
    LEFT JOIN groups ON groups.id = p.group_id
    LEFT JOIN phones ph ON ph.contact_id = p.id
    WHERE p.email ILIKE %s
    GROUP BY p.id, groups.name                                             
  ''', (f'%{email}%',))
  rows = cur.fetchall()
  if not rows:
    print('No contact with this email was found')
  else:
    for id, name, sur, mail, gr, tels in rows:
      print(f'{gr or "-"} | {id}. {name} {sur or ''} - {tels or "-"} || {mail}')  

def sort_output(cur):
  print('\n1.Sort by name\n2.Sort by birthday\n3.Sort by date added')
  choice = input('Your choice: ').strip()
  if choice == '1':
    cur.execute("""
      SELECT p.id, p.first_name, p.last_name, p.email, groups.name,
             STRING_AGG(ph.phone || COALESCE(' (' || ph.type || ')', ''), ', ')
      FROM phonebook p
      LEFT JOIN groups ON groups.id = p.group_id
      LEFT JOIN phones ph ON ph.contact_id = p.id
      GROUP BY p.id, groups.name
      ORDER BY p.first_name, p.last_name;
      """)
    rows = cur.fetchall()
    if not rows:
      print('No contacts found')
    else:
      for id, name, sur, mail, gr, tels in rows:
        print(f'{gr or "-"} | {id}. {name} {sur or ''} - {tels or "-"} || {mail or "-"}')
  elif choice == '2':
    cur.execute("""
      SELECT p.id, p.first_name, p.last_name, p.email, groups.name,
             STRING_AGG(ph.phone || COALESCE(' (' || ph.type || ')', ''), ', '),
             p.birthday
      FROM phonebook p
      LEFT JOIN groups ON groups.id = p.group_id
      LEFT JOIN phones ph ON ph.contact_id = p.id
      GROUP BY p.id, groups.name
      ORDER BY EXTRACT(MONTH FROM p.birthday), EXTRACT(DAY FROM p.birthday); 
      """)
    rows = cur.fetchall()
    if not rows:
      print('No contacts found')
    else:
      for id, name, sur, mail, gr, tels, bd in rows:
        print(f'{bd or "-"} | {gr or "-"} | {id}. {name} {sur or ''} - {tels or "-"} || {mail or "-"}')
  elif choice == '3':
    cur.execute("""
      SELECT p.id, p.first_name, p.last_name, p.email, groups.name,
             STRING_AGG(ph.phone || COALESCE(' (' || ph.type || ')', ''), ', '),
             p.date_added
      FROM phonebook p
      LEFT JOIN groups ON groups.id = p.group_id
      LEFT JOIN phones ph ON ph.contact_id = p.id
      GROUP BY p.id, groups.name
      ORDER BY p.date_added, p.id;
      """)
    rows = cur.fetchall()
    if not rows:
      print('No contacts found')
    else:
      for id, name, sur, mail, gr, tels, da in rows:
        print(f'{da} | {gr or "-"} | {id}. {name} {sur or ''} - {tels or "-"} || {mail or "-"}')
  else:
    print('No such option')



def switch(cur):
  lim = int(input('How many contacts per page: ').strip())
  page = int(input('Page number: ').strip())

  while True:
    off = (page - 1) * lim
    cur.execute('SELECT * FROM query_pagination(%s, %s)', (lim, off))
    rows = cur.fetchall()

    print('Page: ', page)
    if not rows:
      print('No contacts found')
    else:
      for id, name, surname, email, group_name, phone in rows:
        print(f'{id} | {group_name or "-"} | {name} {surname or ""} - {phone or "-"} || {email or "-"}')

    print('\n1.Next page\n2.Previous page\n3.Quit')
    choice = input('Your choice: ').strip()

    if choice == '1':
      if len(rows) < lim:
        print('This is the last page')
      else:
        page += 1
    elif choice == '2':
      if page == 1:
        print('This is the first page')
      else:
        page -= 1
    elif choice == '3':
      break
    else:
      print('No such option')


def export_json(cur):
  cur.execute('''
    SELECT p.id, p.first_name, p.last_name, p.email, p.birthday, groups.name
    FROM phonebook p
    LEFT JOIN groups ON groups.id = p.group_id
    ORDER BY p.id
  ''')
  rows = cur.fetchall()
  contacts = []
  for c_id, name, surname, email, bd, group in rows:
    cur.execute('SELECT phone, type FROM phones WHERE contact_id = %s',(c_id,))
    phones = []
    for phone, ptype in cur.fetchall():
      phones.append({'phone':phone, 'type':ptype})

    contacts.append({
      'first_name': name,
      'last_name': surname,
      'email': email,
      'birthday':bd,
      'group' : group,
      'phones': phones
    })

  with open('contacts.json', 'w') as f:
    json.dump(contacts, f, indent=2, default=str)
  print('Saved to contacts.json')

def import_json(cur):
  filename = input('JSON file name: ').strip()
  with open(filename) as f:
    contacts = json.load(f)

  for c in contacts:
    name = c.get('first_name')
    cur.execute('SELECT id FROM phonebook WHERE first_name = %s', (name,))
    found = cur.fetchone()

    if found:
      answer = input(f'{name} already exists. skip / overwrite: ').strip().lower()
      if answer != 'overwrite':
        print(f'{name} skipped')
        continue
      c_id = found[0]
      cur.execute('''
        UPDATE phonebook SET last_name = %s, email = %s, birthday = %s
        WHERE id = %s
      ''',(c.get('last_name'), c.get('email'), c.get('birthday'), c_id,))
      cur.execute('DELETE FROM phones WHERE contact_id = %s', (c_id,))
    else:
      cur.execute('''
        INSERT INTO phonebook(first_name, last_name, email, birthday)
        VALUES(%s, %s, %s, %s) RETURNING id
      ''',(name, c.get('last_name'), c.get('email'), c.get('birthday')))
      c_id = cur.fetchone()[0]

    for ph in c.get('phones', []):
      cur.execute('INSERT INTO phones(contact_id, phone, type) VALUES (%s,%s,%s)', (c_id, ph.get('phone'), ph.get('type')))
    if c.get('group'):
      cur.execute('CALL move_to_group(%s,%s)',(name, c['group']))
  cur.connection.commit()
  print('Import finished')
      
def add_phone_menu(cur):
  name = input('Contact first name: ').strip()
  phone = input('Phone: ').strip()
  ptype = input('Type (home/work/mobile): ').strip()
  cur.execute('CALL add_phone(%s, %s, %s)', (name, phone, ptype))
  cur.connection.commit()
  print('Phone added')

def move_to_group_menu(cur):
  name = input('Contact first name: ').strip()
  group = input('Group: ').strip()
  cur.execute('CALL move_to_group(%s, %s)', (name, group))
  cur.connection.commit()
  print('Contact moved')

def search_all(cur):
  q = input('Search: ').strip()
  cur.execute('SELECT * FROM search_contacts(%s)', (q,))
  rows = cur.fetchall()
  if not rows:
    print('Nothing found')
  else:
    for c_id, name, surname, email, group_name, phone in rows:
      print(f'{c_id} | {group_name or "-"} | {name} {surname or ""} - {phone or "-"} || {email or "-"}')

def import_csv(cur):
  with open('contacts.csv', newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
      cur.execute('SELECT id FROM phonebook WHERE first_name = %s', (row['first_name'],))
      found = cur.fetchone()
      if found:
        c_id = found[0]
        cur.execute(
          'UPDATE phonebook SET last_name = %s, email = %s, birthday = %s WHERE id = %s',
          (row['last_name'] or None, row['email'] or None, row['birthday'] or None, c_id))
      else:
        cur.execute('''
          INSERT INTO phonebook (first_name, last_name, email, birthday)
          VALUES (%s, %s, %s, %s) RETURNING id
        ''', (row['first_name'], row['last_name'] or None,
              row['email'] or None, row['birthday'] or None))
        c_id = cur.fetchone()[0]

      if row['phone']:
        cur.execute('SELECT 1 FROM phones WHERE phone = %s', (row['phone'],))
        if cur.fetchone() is None:
          cur.execute('INSERT INTO phones (contact_id, phone, type) VALUES (%s, %s, %s)',
                      (c_id, row['phone'], row['type'] or None))
        else:
          cur.execute('UPDATE phones SET type = %s WHERE phone = %s',
                      (row['type'] or None, row['phone']))

      if row['group']:
        cur.execute('CALL move_to_group(%s, %s)', (row['first_name'], row['group']))
  cur.connection.commit()
  print('CSV import finished')
if __name__ == '__main__':
  config = load_config()
  with psycopg2.connect(**config) as con:
    with con.cursor() as cur:
      while True:
        print('\n1.Filter by group\n2.Search by email\n3.Sort\n4.Display pages'
              '\n5.Export JSON\n6.Import JSON\n7.Add phone\n8.Move to group'
              '\n9.Search contact by part\n10.Import CSV\n0.Exit')
        choice = input('Your choice: ').strip()
        try:
          if choice == '1':
            filter_groups(cur)
          elif choice == '2':
            search_by_mail(cur)
          elif choice == '3':
            sort_output(cur)
          elif choice == '4':
            switch(cur)
          elif choice == '5':
            export_json(cur)
          elif choice == '6':
            import_json(cur)
          elif choice == '7':
            add_phone_menu(cur)
          elif choice == '8':
            move_to_group_menu(cur)
          elif choice == '9':
            search_all(cur)
          elif choice == '10':
            import_csv(cur)
          elif choice == '0':
            break
          else:
            print('No such option')
        except psycopg2.Error as e:
          print('Database error:', e.pgerror or e)
          con.rollback()
import psycopg2
from config import load_config

def query_contacts():
  print('1 - show all')
  print('2 - search by name')
  print('3 - search by phone number')
  print('4 - show contacts with last name')
  choice = input('Your choice: ').strip()

  if choice == '1':
    sql = "SELECT * FROM phonebook"
    params = ()
  elif choice == '2':
    name = input('Name: ').strip()
    sql = 'SELECT * FROM phonebook WHERE first_name ILIKE %s'
    params = (f'%{name}%',)
  elif choice == '3':
    prefix = input("Phone number: ").strip()
    sql = 'SELECT * FROM phonebook WHERE phone like %s'
    params = (f'{prefix}%',)
  elif choice == '4':
    sql = 'SELECT * FROM phonebook WHERE last_name IS NOT NULL'
    params = ()
  else:
    print('No such option')
    return

  config = load_config()
  with psycopg2.connect(**config) as con:
    with con.cursor() as cur:
      cur.execute(sql, params)
      rows = cur.fetchall()

  if not rows:
    print("Nothing was found")
    return
  for id_, first_name, last_name, phone in rows:
    print(f'{id_}. {first_name} {last_name or ''} - {phone}')

if __name__ == '__main__':
  query_contacts()
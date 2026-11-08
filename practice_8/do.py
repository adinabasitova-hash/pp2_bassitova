import psycopg2
from config import load_config

def search_contacts(cur):
  pattern = input('Enter part of name,surname or phone: ')
  cur.execute('SELECT * FROM get_contact_by_pattern(%s)',(pattern,))
  rows = cur.fetchall()

  if not rows:
    print('Nothing was found')
    return
  for id, name,sur,tel in rows:
    print(f"{id}. {name} {sur or ''} - {tel}")

def add_one(cur,con):
  name = input('Enter first name: ').strip()
  sur = input('Enter last name or skip: ').strip() or None
  tel = input('Enter the phone number: ').strip()

  cur.execute('CALL add_new_contact(%s,%s,%s)', (name, tel, sur))
  con.commit()
  print('Done')

def add_many(cur,con):
  names = [n.strip() for n in input('Names (comma separated): ').split(',')]
  surnames = [s.strip() or None for s in input('Surnames (comma separated): ').split(',')]
  phones = [p.strip() for p in input('Phone nums (comma separated): ').split(',')]

  cur.execute('CALL add_many_contacts(%s, %s, %s)',(names, phones, surnames))
  bad = cur.fetchone()[0]
  con.commit()

  if bad:
    print('Not added(wrong number)')
    for item in bad:
      print(' ', item)
  else:
    print('All contacts added')

def show_page(cur):
  lim = int(input('How many contacts per page: ').strip())
  page = int(input('Page number: ').strip())
  off = (page - 1) * lim

  cur.execute('SELECT * FROM query_pagination(%s,%s)',(lim, off))
  rows = cur.fetchall()
  if not rows:
    print('This page is empty')
    return
  for id, name, surname, phone in rows:
    print(f"{id}. {name} {surname or ''} - {phone}")

def delete(cur,con):
  dlt = input('Input name or phone number of the contact you want to delete: ')
  cur.execute("CALL delete_contact(%s)", (dlt,))
  con.commit()
  print('Done')

def main():
  config = load_config()
  with psycopg2.connect(**config) as con:
    with con.cursor() as cur:
      with open('functions.sql') as f:
        cur.execute(f.read())
      with open('procedures.sql') as p:
        cur.execute(p.read())
      con.commit()

      while True:
        print('\n1. Search  2. Add/update  3. Add many  4. Page  5. Delete  0. Exit')
        choice = input('Choose: ').strip()

        try:
          if choice == '1':
            search_contacts(cur)
          elif choice == '2':
            add_one(cur, con)
          elif choice == '3':
            add_many(cur, con)
          elif choice == '4':
            show_page(cur)
          elif choice == '5':
            delete(cur, con)
          elif choice == '0':
            break
          else:
            print('No such option')
        except (psycopg2.Error, ValueError) as e:
          con.rollback()
          print('Error:', e)
if __name__ == '__main__':
  main()
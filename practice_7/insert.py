import csv
import psycopg2
from config import load_config

def insert_from_csv(filename):
  sql = """
      INSERT INTO phonebook (first_name,last_name,phone) VALUES(%s,%s,%s)
      ON CONFLICT (phone) DO NOTHING
      """
  config = load_config()
  with psycopg2.connect(**config) as con:
    with con.cursor() as cur:
      with open(filename, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
          cur.execute(sql, (
            row['first_name'],
            row['last_name'] or None,
            row['phone'],
          ))

def insert_from_console():
  first_name = input('First name*: ').strip()
  last_name = input('Last name: ').strip()
  phone = input('Phone*: ').strip()

  if not first_name or not phone:
    print('Enter first name and phone correctly')
    return

  sql = """
      INSERT INTO phonebook (first_name, last_name, phone)VALUES(%s,%s,%s)
      ON CONFLICT(phone) DO NOTHING
      """
  config = load_config()
  with psycopg2.connect(**config) as con:
    with con.cursor() as cur:
      cur.execute(sql, (first_name, last_name or None, phone))
      if cur.rowcount == 0:
        print('The contact with this number alredy exists')
      else:
        print('The contact was added')
if __name__ == '__main__':
  print('1 - load from csv')
  print('2 - add from console')
  choice = input('Your choice: ').strip()

  if choice == '1':
    insert_from_csv("contacts.csv")
  elif choice == '2':
    insert_from_console()
  else:
    print('No such option')

import psycopg2
from config import load_config

def update_contact():
  phone = input("Phone number of the contact to change: ").strip()
  print('1 - Change the name')
  print('2 - Change the number')
  choice = input('Your choice: ').strip()

  if choice == '1':
    new_value = input('New name: ').strip()
    sql = "UPDATE phonebook SET first_name = %s WHERE phone = %s"
  elif choice == '2':
    new_value = input('New phone number: ').strip()
    sql = "UPDATE phonebook SET phone = %s WHERE phone = %s"
  else:
    print('No such option')
    return

  config = load_config()
  try:
    with psycopg2.connect(**config) as con:
      with con.cursor() as cur:
        cur.execute(sql, (new_value, phone))
        if cur.rowcount == 0:
          print('The contact with this phone number is not found')
        else:
          print('The contact was updated')
  except psycopg2.errors.UniqueViloation:
    print('The phone number is already taken by another contact')

if __name__ == '__main__':
  update_contact()
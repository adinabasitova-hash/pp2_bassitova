import psycopg2
from config import load_config

def delete_contact():
  f_name = input('Enter the first name of contact you want to delete: ').strip()
  sql = 'DELETE FROM phonebook WHERE first_name = %s'

  rows_deleted = 0
  config = load_config()

  try:
    with psycopg2.connect(**config) as con:
      with con.cursor() as cur:
        cur.execute(sql, (f_name,))
        rows_deleted = cur.rowcount
  except (Exception, psycopg2.DatabaseError) as error:
    print(error)

  if rows_deleted == 0:
    print("Contact not found")
  else:
    print('Contact deleted')
  return rows_deleted


if __name__ == '__main__':
  delete_contact()

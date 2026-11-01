import psycopg2
from config import load_config

def create_table():
  sql = (
    """
    CREATE TABLE phonebook_r(
      id SERIAL PRIMARY KEY,
      first_name VARCHAR(50) NOT NULL,
      last_name VARCHAR(50),
      phone VARCHAR(20) NOT NULL UNIQUE
    );
"""
  )
  try:
    config = load_config()
    with psycopg2.connect(**config) as conn:
      with conn.cursor() as cur:
          cur.execute(sql)
  except (psycopg2.DatabaseError, Exception) as error:
    print(error)

if __name__ == '__main__':
  create_table()
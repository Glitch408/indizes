from sqlite3 import connect
from faker import Faker

fake = Faker()

connection = connect("Kunden.db")
cursor = connection.cursor()


#ONLY FOR TESTING
cursor.execute("DROP TABLE IF EXISTS personen;")
#DELETE AFTERWARD!!!!

cursor.execute("""
CREATE TABLE IF NOT EXISTS personen (
  id INTEGER PRIMARY KEY,
  vorname TEXT,
  nachname TEXT
);
""")

for i in range(5):
  fullname = (fake.name()).split()
  firstname = fullname[0]
  lastname = fullname[(len(fullname))-1]
  cursor.execute(f"""
  INSERT INTO personen VALUES ('{i}', '{firstname}', '{lastname}');
  """) 


connection.close()
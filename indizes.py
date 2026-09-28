from sqlite3 import connect
from faker import Faker
fake = Faker()

for x in range(5):
  fullname = (fake.name()).split()
  firstname = fullname[0]
  lastname = fullname[(len(fullname))-1]
  print(f"{x}, {firstname}, {lastname}")  
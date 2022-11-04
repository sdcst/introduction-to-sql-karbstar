#!python
import sqlite3
"""
Create a program that will store the database for a veterinary
Each record needs to have the following information:
id unique integer identifier
pet name
pet species (cat, bird, dog, etc)
pet breed (persian, beagle, canary, etc)
owner name
owner phone number
owner email
owner balance (amount owing)
date of first visit

create a program that will allow the user to:
insert a new record into the database and save it automatically
retrieve a record by their id and display all of the information
retrieve a record by the email and display all of the information
retrieve a record by phone number and display all of the information

You will need to create the table yourself. Consider what data types you will
need to use.
"""
file = 'dbasev.db'
connection = sqlite3.connect(file)
print(connection)

cursor = connection.cursor()
query = """
create table if not exists customers (
    id integer primary key autoincrement,
    name tinytext,
    email tinytext,
    pet name tinytext,
    pet species tinytext,
    pet breed tinytext,
    owner phone number int,
    owner email tinytext,
    owner balance int
    );
"""
cursor.execute(query)
print('vet database accsested what will you do\nadd new record 1, acses record 2:')
input('')

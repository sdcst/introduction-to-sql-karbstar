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
    petname tinytext,
    petspecies tinytext,
    petbreed tinytext,
    ownerphonenumber int,
    ownerbalance int
    );
"""

cursor.execute(query)
"""
data = [
    ['Joe Mantenga','joe@sdss.ca','prim','dog','moredog',6049439998,56743],
    ['Hanna Montana','miley@cyrus.com','gity','cat','morecat',6049519698,0],
    ['Amanda Huggenkis','cool1@gmail.com','fungui','lizzard','lessliz',6047939795,45]
    ]
for i in data:
    query = f"insert into customers (name,email,petname,petspecies,petbreed,ownerphonenumber,ownerbalance) values ('{i[0]}','{i[1]}','{i[2]}','{i[3]}','{i[4]}',{i[5]},{i[6]});"
    print(query)
    cursor.execute(query)
connection.commit()
query = "select * from customers"
cursor.execute(query)
result = cursor.fetchall()
print(result)
for i in result:
    print(i)
"""
print('vet database accsested what will you do\nacses record 1, add new record 2:')
go=input('')
cog=True
while cog==True:
    if go=='1':
        col=True
        while col==True:
            print('how do you want to: look by email 1, look by id 2, look by phone number 3')
            fi=input('')
            if fi=='1':
                em=input('enter email:')
                query = f"select * from customers where email = '{em}'"
                cursor.execute(query)
                result = cursor.fetchall()
                print(result)
            if fi=='2':
                i=input('enter id:')
                query = f"select * from customers where id = {i}"
                cursor.execute(query)
                result = cursor.fetchall()
                print(result)
            if fi=='3':
                pn=input('enter phone number:')
                query = f"select * from customers where ownerphonenumber = {pn}"
                cursor.execute(query)
                result = cursor.fetchall()
                print(result)
            cof=True
            while cof==True:
                y=input('continue to acses records(y/n)')
                if y=='n':
                    cof=False
                    col=False
                if y=='y':
                    cof=False
                elif y!='n':
                    print('enter valid number')

    #"""
    if go=='2':
        col=True
        while col==True:
            p1=input('full name:')
            p2=input('email:')
            p3=input('pet name:')
            p4=input('pet species:')
            p5=input('pet breed:')
            p6=input('phone number:')
            p7=input('balance:')
            mix=[p1,p2,p3,p4,p5,p6,p7]
            query = f"insert into customers (name,email,petname,petspecies,petbreed,ownerphonenumber,ownerbalance) values ('{mix[0]}','{mix[1]}','{mix[2]}','{mix[3]}','{mix[4]}',{mix[5]},{mix[6]});"
            cursor.execute(query)
            connection.commit()
            cof=True
            while cof==True:
                y=input('continue to acses records(y/n)')
                if y=='n':
                    cof=False
                    col=False
                if y=='y':
                    cof=False
                elif y!='n':
                    print('enter valid number')
    elif go!='1':
        print('enter valid number')
    cof=True
    while cof==True:
        y=input('continue to use records(y/n)')
        if y=='n':
            cof=False
            cog=False
        if y=='y':
            cof=False
        elif y!='n':
            print('enter valid number')
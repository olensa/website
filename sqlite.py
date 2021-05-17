import sqlite3

#connect to a created db or create a new db (if it was not created) 
#connection = sqlite3.connect('customers.db')

#create cursor which will tell your db what to do
#cursor = connection.cursor()


#Query database. Return all records
def show_all():
    #connect to database and create cursor
    connection = sqlite3.connect('projects.db')
    cursor = connection.cursor()

    cursor.execute("SELECT rowid, * FROM projects")
    items = cursor.fetchall()

    for item in items:
        print (item)

    connection.commit()
    connection.close()

#add new record to the table
def add_link(link):
    connection = sqlite3.connect('projects.db')
    cursor = connection.cursor()
    cursor.execute("INSERT INTO projects VALUES (?)", (link))
    connection.commit()
    connection.close()

#add many records to the table
def add_many(links):
    connection = sqlite3.connect('projects.db')
    cursor = connection.cursor()
    cursor.executemany("INSERT INTO projects VALUES (?,?,?)", (links))
    connection.commit()
    connection.close()

#delete record from the table
def delete_one(id):
    connection = sqlite3.connect('projects.db')
    cursor = connection.cursor()
    cursor.execute("DELETE FROM projects WHERE rowid = (?)", id)

    connection.commit()
    connection.close()

def email_lookup(email):
    connection = sqlite3.connect('customers.db')
    cursor = connection.cursor()
    cursor.execute("SELECT rowid,* FROM customers WHERE email = (?)", (email,))
    items = cursor.fetchall()

    for item in items:
        print (item)
    connection.commit()
    connection.close()
#_____________________________________________________________________________________
# Delete Records
#cursor.execute("DELETE from customers WHERE rowid = 6")
#_____________________________________________________________________________________
# Query the Database - ORDER BY 
#cursor.execute("SELECT rowid, * from customers ORDER BY rowid") #ascending by default
#cursor.execute("SELECT rowid, * from customers ORDER BY rowid DESC") #descending
#cursor.execute("SELECT rowid, * from customers ORDER BY last_name DESC")
#_____________________________________________________________________________________
#Query The Database - AND/OR
#cursor.execute("SELECT rowid, * from customers WHERE last_name LIKE 'Br%' AND rowid = 3")
#cursor.execute("SELECT rowid, * from customers WHERE last_name LIKE 'Br%' OR rowid = 3")
#cursor.execute("SELECT rowid, * from customers WHERE last_name LIKE 'Br%' AND rowid = 3")

# Limiting Records
#cursor.execute("SELECT rowid, * FROM customers ORDER BY rowid DESC LIMIT 2")
#_____________________________________________________________________________________
# Delete a Table(Drop)
#cursor.execute("DROP TABLE customers")
#connection.commit()

#_____________________________________________________________________________________ 
# Update Records
#cursor.execute(""" UPDATE customers SET first_name = 'John'
                #WHERE rowid = 1
    #""")
#_____________________________________________________________________________________
# Query the Database: * stands for everything
#rowid stands for primary id
#cursor.execute("SELECT rowid, * FROM customers")tg_bot
#cursor.execute("SELECT * FROM customers WHERE last_name = 'Elder'")
#cursor.execute("SELECT * FROM customers WHERE email LIKE '%codemy.com'")
#cursor.execute("SELECT * FROM customers")
#_____________________________________________________________________________________
#cursor.fetchone() - first item
#cursor.fetchmany(3)  -first (#) items
#print(cursor.fetchall())
#print(cursor.fetchmany(3))
#print(cursor.fetchone()[0])

#items = cursor.fetchall()
#for item in items:
    #print (item)



#print("NAME " + "\t\t\tEMAIL")
#print ('--------' + '\t\t--------')
#for item in items:
    #print (item[0]+ " " + item[1] + " \t\t " + item[2])

#_____________________________________________________________________________________
#create multiple records:
many_customers =[
                    ('wes', 'Brown', 'wes@brown.com'),
                    ('Steph','Hearth', 'steph@hearth.com'), 
                    ('dan','pat','dan@pat.com')
                ]
#_____________________________________________________________________________________
# ? - placeholders
#insert multiple records 
#cursor.executemany("INSERT INTO customers VALUES (?,?,?)", many_customers)

#_____________________________________________________________________________________
#insert a single record
#cursor.execute("INSERT INTO customers VALUES ('Mary', 'Brown', 'mary@codemy.com')")

#_____________________________________________________________________________________
#create a table
#cursor.execute("""CREATE TABLE customers (
        #first_name text,
        #last_name text,
        #email text
    #)""")
#
#Datatypes:
    #NULL - exist/doesn't exist
    #INTEGER - numbers 10
    #REAL - decimal 10.5
    #TEXT - 'strings'
    #BLOB - images etc(media)
#print('executed succesfully')

#Commit our command
#connection.commit()

#Close the connection
#connection.close()'a','b','brenda@sm.com'
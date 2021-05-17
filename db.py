import sqlite3

#connect to a created db or create a new db (if it was not created) 
connection = sqlite3.connect('projects.db')

#create cursor which will tell your db what to do
cursor = connection.cursor()

#create a table
cursor.execute("""CREATE TABLE links (
        Link text
)""")




connection.commit()
connection.close()
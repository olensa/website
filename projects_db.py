import sqlite3
import logging

my_links = ['olensa.ga', 'olensa.ga/spock', 'olensa.ga/contact']
link = 'olensa.ga'

def add_link(link):
    connection = sqlite3.connect('projects.db')
    cursor = connection.cursor()
    cursor.execute("SELECT rowid, * FROM links")

    cursor.execute('SELECT rowid FROM links WHERE Link = ?', (link,))
    list = cursor.fetchall()
    if len(list) == 0:
        cursor.execute("INSERT INTO links VALUES (?)", (link,))    
    else:
        logging.warning ('Component already exists %s'%link)



    
    connection.commit()
    connection.close()

def show_all():
    #connect to database and create cursor
    connection = sqlite3.connect('projects.db')
    cursor = connection.cursor()

    cursor.execute("SELECT rowid, * FROM links")
    items = cursor.fetchall()

    for item in items:
        print (item)

    connection.commit()
    connection.close()


def add_many(links):
    connection = sqlite3.connect('projects.db')
    cursor = connection.cursor()
    cursor.execute("SELECT Link FROM links")

    for item in links:
        add_link(item)
            

add_link(link)
add_many(my_links)
show_all()

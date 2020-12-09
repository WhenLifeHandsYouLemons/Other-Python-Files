"""
For IGCSE Computer Science course
"""

import sqlite3

def open_database(filename):
    connection = sqlite3.connect( filename )
    connection.row_factory = sqlite3.Row
    return connection

def read_database(connection, sql):
    cursor = connection.cursor()
    cursor.execute(sql)
    result = [ dict(row) for row in cursor.fetchall() ]
    return result

def write_database(connection, sql):
    cursor = connection.cursor()
    rows_affected = cursor.execute(sql).rowcount
    connection.commit()
    return rows_affected

def close_database(connection):
    connection.close()

db = open_database('C:/Users/2005s/Documents/Databases/First database.db')

write_database(db, """INSERT INTO people (first_name, date_of_birth)
VALUES ('Sad', '14/10/2004');""")

results = read_database(db, "SELECT date_of_birth FROM people;")

print(results)

#for person in results:
#    print(f"{person['first_name']} has email address {person['email_address']}")

close_database(db)
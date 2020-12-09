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

# Open the database
db = open_database('C:/Users/2005s/Documents/Databases/First database.db')

# Write to the database
write_database(db, """INSERT INTO people (first_name, last_name)
VALUES ('Sad', 'Man');""")

# Read the database
results = read_database(db, "SELECT * FROM people;")

# Print out all the results
print(results)

# Print out selected results in a readable way
for person in results:
    print(f"{person['first_name']} has email address {person['email_address']}")

# Close the database to use in other programs
close_database(db)

import sqlite3

connection = sqlite3.connect('cocoa.db')
cursor = connection.cursor()

cursor.execute("SELECT * FROM farm_records")
records = cursor.fetchall()
for record in records:
    print(record)

connection.close()
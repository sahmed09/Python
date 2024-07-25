import mysql.connector
from datetime import datetime

my_db = mysql.connector.connect(
    host='localhost',
    user='shihab',
    password='root',
    database='test_database'
)

my_cursor = my_db.cursor()

sql = "INSERT INTO Person (name, age, created, gender) VALUES (%s, %s, %s, %s)"
val = ('Ahmed', 25, datetime.now(), 'M')
my_cursor.execute(sql, val)
my_db.commit()

print(my_cursor.rowcount, "record inserted.")
print("1 record inserted, ID:", my_cursor.lastrowid)  # Get Inserted ID

# Insert Multiple Rows
sql = "INSERT INTO Person (name, age, created, gender) VALUES (%s, %s, %s, %s)"
val = [
    ('Shihab', 25, datetime.now(), 'M'),
    ('Ahmed', 24, datetime.now(), 'M'),
    ('Ananna', 23, datetime.now(), 'F'),
    ('Samia', 22, datetime.now(), 'F'),
    ('Kiron', 25, datetime.now(), 'M')
]
my_cursor.executemany(sql, val)
my_db.commit()

print(my_cursor.rowcount, "record inserted.")

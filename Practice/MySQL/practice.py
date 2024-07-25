import mysql.connector

my_db = mysql.connector.connect(
    host='localhost',
    user='shihab',
    password='root',
    database='test_database'
)

my_cursor = my_db.cursor()

my_cursor.execute('SELECT * FROM Person')

for x in my_cursor:
    print(x)

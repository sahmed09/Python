import mysql.connector

my_db = mysql.connector.connect(
    host='localhost',
    user='shihab',
    password='root',
    database='test_database'
)

my_cursor = my_db.cursor()

# Limit the Result
my_cursor.execute("SELECT * FROM Person LIMIT 2")
result = my_cursor.fetchall()
for x in result:
    print(x)
print()

# Start From Another Position
my_cursor.execute("SELECT * FROM Person LIMIT 2 OFFSET 1")
result = my_cursor.fetchall()
for x in result:
    print(x)

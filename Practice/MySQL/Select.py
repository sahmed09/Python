import mysql.connector

my_db = mysql.connector.connect(
    host='localhost',
    user='shihab',
    password='root',
    database='test_database'
)

my_cursor = my_db.cursor()

my_cursor.execute('SELECT * FROM Person')
# my_cursor.execute("SELECT PersonID, Name FROM Person where gender='M' ORDER BY PersonID DESC")

result = my_cursor.fetchall()  # fetches all rows from the last executed statement.

for x in result:
    print(x)
# print(my_cursor.fetchall())

# Selecting Columns:
my_cursor.execute("SELECT PersonID, Name FROM Person")
result = my_cursor.fetchall()
for x in result:
    print(x)

# fetchone() Method:
my_cursor.execute('SELECT * FROM Person')
result = my_cursor.fetchone()
print(result)

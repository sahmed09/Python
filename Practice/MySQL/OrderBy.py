import mysql.connector

my_db = mysql.connector.connect(
    host='localhost',
    user='shihab',
    password='root',
    database='test_database'
)

my_cursor = my_db.cursor()

sql = "SELECT * FROM Person ORDER BY PersonID"
my_cursor.execute(sql)  # Default ASC

result = my_cursor.fetchall()
for x in result:
    print(x)
print()

# ORDER BY DESC
sql = "SELECT * FROM Person ORDER BY PersonID DESC"
my_cursor.execute(sql)

result = my_cursor.fetchall()
for x in result:
    print(x)

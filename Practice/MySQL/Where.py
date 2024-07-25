import mysql.connector

my_db = mysql.connector.connect(
    host='localhost',
    user='shihab',
    password='root',
    database='test_database'
)

my_cursor = my_db.cursor()

sql = "SELECT PersonID, Name FROM Person where gender='M' ORDER BY PersonID DESC"
my_cursor.execute(sql)

result = my_cursor.fetchall()
for x in result:
    print(x)
print()

# Wildcard Characters
sql = "SELECT * FROM Person where name LIKE 'shi%'"
my_cursor.execute(sql)
result = my_cursor.fetchall()
for x in result:
    print(x)
print()

# Prevent SQL Injection
# Escape query values by using the placeholder %s method:
sql = "SELECT * FROM Person where name = %s"
name = ("Shihab", )
my_cursor.execute(sql, name)
result = my_cursor.fetchall()
for x in result:
    print(x)

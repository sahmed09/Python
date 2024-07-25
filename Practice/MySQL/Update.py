import mysql.connector

my_db = mysql.connector.connect(
    host='localhost',
    user='shihab',
    password='root',
    database='test_database'
)

my_cursor = my_db.cursor()

sql = "Update Person SET name = 'Shila' WHERE name = 'Shina'"
my_cursor.execute(sql)
my_db.commit()
print(my_cursor.rowcount, "record(s) affected")

# Prevent SQL Injection
# Escape values by using the placeholder %s method:
sql = "Update Person SET name = %s WHERE name = %s"
name = ('Shina', 'Shila')
my_cursor.execute(sql, name)
my_db.commit()
print(my_cursor.rowcount, "record(s) affected")

my_cursor.execute('SELECT * FROM Person')
result = my_cursor.fetchall()  # fetches all rows from the last executed statement.
for x in result:
    print(x)

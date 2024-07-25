import mysql.connector

my_db = mysql.connector.connect(
    host='localhost',
    user='shihab',
    password='root',
    database='test_database'
)

my_cursor = my_db.cursor()

sql = "DELETE FROM Person where name = 'Shina'"
my_cursor.execute(sql)
my_db.commit()
print(my_cursor.rowcount, "record(s) deleted")

# Prevent SQL Injection
# Escape values by using the placeholder %s method:
sql = "DELETE FROM Person where name = %s"
name = ('Shina', )
my_cursor.execute(sql, name)
my_db.commit()
print(my_cursor.rowcount, "record(s) deleted")

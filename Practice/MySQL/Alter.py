import mysql.connector

my_db = mysql.connector.connect(
    host='localhost',
    user='shihab',
    password='root',
    database='test_database'
)

my_cursor = my_db.cursor()

# Add New Column
# my_cursor.execute("ALTER TABLE Person ADD COLUMN Address VARCHAR(255) NOT NULL")

# Change Column Name
# my_cursor.execute("ALTER TABLE Person CHANGE first_name Name VARCHAR(255)")

my_cursor.execute("DESCRIBE Person")
print(my_cursor.fetchall())

import mysql.connector

my_db = mysql.connector.connect(
    host='localhost',
    user='shihab',
    password='root',
)

my_cursor = my_db.cursor()

my_cursor.execute("CREATE DATABASE test_database")

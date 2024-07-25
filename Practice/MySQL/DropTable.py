import mysql.connector  # pip install mysql-connector-python

my_db = mysql.connector.connect(
    host='localhost',
    user='shihab',
    password='root',
    database='test_database'
)

my_cursor = my_db.cursor()

sql = "DROP TABLE person"
my_cursor.execute(sql)

# Drop Only if Exist
sql = "DROP TABLE IF EXISTS person"
my_cursor.execute(sql)

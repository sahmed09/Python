import mysql.connector

my_db = mysql.connector.connect(
    host='localhost',
    user='shihab',
    password='root',
    database='test_database'
)

my_cursor = my_db.cursor()

my_cursor.execute('''
    CREATE TABLE PERSON(
        personID int PRIMARY KEY NOT NULL AUTO_INCREMENT,
        name VARCHAR(255) NOT NULL,
        age smallint UNSIGNED NOT NULL,
        created datetime NOT NULL,
        gender ENUM('M', 'F', 'O') NOT NULL
    );
''')

my_cursor.execute('DESCRIBE Person')
for x in my_cursor:
    print(x)

my_cursor.execute('SHOW TABLES')
for x in my_cursor:
    print(x)

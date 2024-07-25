import mysql.connector

my_db = mysql.connector.connect(
    host='localhost',
    user='shihab',
    password='root',
    database='test_database'
)

my_cursor = my_db.cursor()

users = [('John', 154), ('Peter', 154), ('Amy', 155), ('Hannah', 134), ('Michael', 132)]
products = [(154, 'Chocolate'), (155, 'Lemons'), (156, 'Vanilla')]

# Q1 = "CREATE TABLE Buyer (ID int PRIMARY KEY AUTO_INCREMENT, name VARCHAR(255), fav int);"
# Q2 = "CREATE TABLE Products (id int PRIMARY KEY, name VARCHAR(255));"
# my_cursor.execute(Q1)
# my_cursor.execute(Q2)

# sql = "INSERT INTO Products (id, name) VALUES (%s, %s)"
# my_cursor.executemany(sql, products)
# my_db.commit()
# print(my_cursor.rowcount, "record inserted.")

# INNER JOIN
# The INNER JOIN keyword selects records that have matching values in both tables.
sql = "SELECT buyer.name AS buyers, Products.name AS favourite FROM Buyer " \
      "INNER JOIN Products ON Buyer.fav = products.id"
my_cursor.execute(sql)
result = my_cursor.fetchall()
for x in result:
    print(x)
print()

# LEFT JOIN
# The LEFT JOIN keyword returns all records from the left table (table1), and the matching records from the right table
# (table2).
sql = "SELECT buyer.name AS buyers, Products.name AS favourite FROM Buyer " \
      "LEFT JOIN Products ON Buyer.fav = products.id"
my_cursor.execute(sql)
result = my_cursor.fetchall()
for x in result:
    print(x)
print()

# RIGHT JOIN
# The RIGHT JOIN keyword returns all records from the right table (table2), and the matching records from the left
# table (table1).
sql = "SELECT buyer.name AS buyers, Products.name AS favourite FROM Buyer " \
      "RIGHT JOIN Products ON Buyer.fav = products.id"
my_cursor.execute(sql)
result = my_cursor.fetchall()
for x in result:
    print(x)
print()

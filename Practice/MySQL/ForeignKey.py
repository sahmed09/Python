import mysql.connector

my_db = mysql.connector.connect(
    host='localhost',
    user='shihab',
    password='root',
    database='test_database'
)

users = [('shihab', 'shihab123'),
         ('Ahmed', 'Ahmed123'),
         ('Shian', 'Shian123')]

user_scores = [(45, 100),
               (30, 200),
               (46, 124)]

my_cursor = my_db.cursor()

# Creating Table
Q1 = "CREATE TABLE Users (ID int PRIMARY KEY AUTO_INCREMENT, name VARCHAR(255), password VARCHAR(255));"
Q2 = "CREATE TABLE Scores (userID int PRIMARY KEY, FOREIGN KEY(userID) REFERENCES Users(ID), game1 int DEFAULT 0, " \
     "game2 int DEFAULT 0);"

my_cursor.execute(Q1)
my_cursor.execute(Q2)

my_cursor.execute('SHOW TABLES')
for x in my_cursor:
    print(x)

# my_cursor.executemany("INSERT INTO Users (name, password) VALUES (%s, %s)", users)

# Inserting Data
Q3 = "INSERT INTO Users (name, password) VALUES (%s, %s)"
Q4 = "INSERT INTO Scores (userID, game1, game2) VALUES (%s, %s, %s)"

for x, user in enumerate(users):
    my_cursor.execute(Q3, user)
    last_id = my_cursor.lastrowid
    my_cursor.execute(Q4, (last_id,) + user_scores[x])
my_db.commit()

my_cursor.execute("SELECT * FROM Users")
for x in my_cursor:
    print(x)
print()

my_cursor.execute("SELECT * FROM Scores")
for x in my_cursor:
    print(x)

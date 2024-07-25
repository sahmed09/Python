import sqlite3

# conn = sqlite3.connect('emaildb.sqlite')
# cur = conn.cursor()  # send sql command through cursor and get response through same cursor
#
# cur.execute('DROP TABLE IF EXISTS Counts')
#
# cur.execute('''CREATE TABLE Counts (email TEXT, count INTEGER)''')
#
# fname = input('Enter file name: ')
# if len(fname) < 1:
#     fname = 'mbox-short.txt'
# fh = open(fname)
# for line in fh:
#     if not line.startswith('From: '):
#         continue
#     pieces = line.split()
#     email = pieces[1]
#
#     cur.execute('SELECT count FROM Counts WHERE email = ? ', (email,))  # ? make sure to not allow sql injection
#     row = cur.fetchone()
#     if row is None:
#         cur.execute('''INSERT INTO Counts (email, count) VALUES (?, 1)''', (email,))
#     else:
#         cur.execute('UPDATE Counts SET count = count + 1 WHERE email = ?', (email,))
#     conn.commit()
#
# # https://www.sqlite.org/lang_select.html
# sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'
#
# for row in cur.execute(sqlstr):
#     print(str(row[0]), row[1])
# cur.close()


"""COUNTING EMAIL WITH ORGANIZATIONS DOMAIN NAME
This application will read the mailbox data (mbox.txt) count up the number email messages per organization 
(i.e. domain name of the email address) using a database with the following schema to maintain the counts:
CREATE TABLE Counts (org TEXT, count INTEGER)"""

conn = sqlite3.connect('organizeemaildb.sqlite')
cur = conn.cursor()  # send sql command through cursor and get response through same cursor

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('''CREATE TABLE Counts (org TEXT, count INTEGER)''')

fname = input('Enter file name: ')
if len(fname) < 1:
    fname = 'mbox.txt'
fh = open(fname)
lis = []
for line in fh:
    if not line.startswith('From: '):
        continue
    pieces = line.split()
    email = pieces[1]
    dom = email.find('@')
    org = email[dom+1:len(email)]

    cur.execute('SELECT count FROM Counts WHERE org = ? ', (org,))  # ? make sure to not allow sql injection
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count) VALUES (?, 1)''', (org,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?', (org,))
conn.commit()

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])
cur.close()

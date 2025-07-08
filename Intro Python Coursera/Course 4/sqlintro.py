import sqlite3

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')
cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)
''')

fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: '): continue
    prepieces = line.split()
    pieces = prepieces[1].split('@')
    email = pieces[1]
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (email,))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count)
                VALUES (?, 1)''', (email,))        
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',
                    (email,))
        print(cur.execute('SELECT org, count FROM Counts WHERE org = ? ', (email,)).fetchone())
        

conn.commit()

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

print('\n\n')
print(cur.execute(sqlstr).fetchone())
print(cur.fetchone())
print(cur.fetchone())
print('\n\n')

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()
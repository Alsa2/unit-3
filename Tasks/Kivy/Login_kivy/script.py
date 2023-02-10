import sqlite3

# Create a database in RAM
conn = sqlite3.connect('Database.db')

# Get a cursor object
c = conn.cursor()

# Create table if not created
c.execute('''CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY,
    email TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
    username TEXT NOT NULL UNIQUE
)''')
# Insert a row of data

#c.execute("INSERT INTO users VALUES (1, 'bob@gmail.com', 'bob', 'bob')")

# Save (commit) the changes
#conn.commit()

# print all the rows
for row in c.execute('SELECT * FROM users'):
    print(row)


conn.close()

import sqlite3

class db_handler:
    def __init__(self):
        self.conn = sqlite3.connect('Database.db')
        self.c = self.conn.cursor()
        self.c.execute('''CREATE TABLE IF NOT EXISTS words(
            id INTEGER PRIMARY KEY,
            word TEXT NOT NULL,
            lenght INT NOT NULL
        )''')
        self.conn.commit()
        self.conn.close()
    def insert(self, word, lenght):
        self.conn = sqlite3.connect('Database.db')
        self.c = self.conn.cursor()
        self.c.execute("INSERT INTO words VALUES (NULL, ?, ?)", (word, lenght))
        self.conn.commit()
        self.conn.close()

    def average_length(self):
        self.conn = sqlite3.connect('Database.db')
        self.c = self.conn.cursor()
        self.c.execute("SELECT AVG(lenght) FROM words")
        data = self.c.fetchone()
        self.conn.close()
        return data

haiku = """Code flows like a stream
Algorithms guide its way
In silence, if solves"""

db = db_handler()

for word in haiku.split():
    db.insert(word, len(word))

print("DB average : ",  str(db.average_length()))

# Get python average length of words in a string

lenghts = [len(word) for word in haiku.split()]
print("Python average : ",  sum(lenghts) / len(lenghts))




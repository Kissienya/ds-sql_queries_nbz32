import sqlite3
#connect to a database
conn = sqlite3.connect('demo.db')
cursor = conn.cursor()

# enable foreign key constraints
cursor.execute('PRAGMA foreign_keys = ON')

cursor.execute('DROP TABLE IF EXISTS orders')
cursor.execute('DROP TABLE IF EXISTS users')


#create users table
cursor.execute("""
    CREATE TABLE users (
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               age INTEGER,
               email TEXT
               )
""")

#create orders table with foreign key
cursor.execute("""
    CREATE TABLE orders (
               order_id INTEGER PRIMARY KEY,
               user_id INTEGER,
               product TEXT NOT NULL,
               amount INTEGER,
               FOREIGN KEY (user_id) REFERENCES users(id)
               )
""")

#insert data
# cursor.execute("INSERT INT0 users (id,name,age,email) VALUES (?,?,?,?)",(1,'Shem',25,'shemgmail.com'))
users_data = [
    (1,'Anthony',25,'anthony@gmail.com'),
    (2,'Winnie',16,'winnie@gmail.com'),
    (3,'Gerald',25,'gerald@gmail.com'),
    (4,'Keith',25,'keith@gmail.com')
]
cursor.executemany("INSERT INTO users (id,name,age,email) VALUES (?,?,?,?)", users_data)

conn.commit()

cursor.execute("SELECT * FROM users ")
print(cursor.fetchall())


conn.close()
#can you create a new table based on this, suppose you want to export and perform further analysis?
#Try and do a right join & full outer join.
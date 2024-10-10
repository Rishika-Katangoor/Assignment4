import sqlite3
conn = sqlite3.connect('notnull.db')
cursor = conn.cursor()
# Here we are creating table for users and inserting values into users table
cursor.execute('''CREATE TABLE users (user_id INTEGER PRIMARY KEY,username TEXT NOT NULL,email TEXT NOT NULL);''')
cursor.execute('INSERT INTO users (user_id, username, email) VALUES (1, "Alice", "alice@example.com");')
cursor.execute('INSERT INTO users (user_id, username, email) VALUES (2, "Bob", "bob@example.com");')
# Here we are trying to insert a user with a NULL username
try:
    cursor.execute('INSERT INTO users (user_id, username, email) VALUES (3, NULL, "charlie@example.com");')
except sqlite3.IntegrityError as e:
    print("Error:", e)  
# Here we are trying to insert a user with a NULL email
try:
    cursor.execute('INSERT INTO users (user_id, username, email) VALUES (4, "Charlie", NULL);')
except sqlite3.IntegrityError as e:
    print("Error:", e) 
print("\n Current data in the users table:")
cursor.execute('SELECT * FROM users')
for row in cursor.fetchall():
    print(row)
# committing to changes and closing the connection
conn.commit()
conn.close()
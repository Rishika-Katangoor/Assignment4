import sqlite3
conn = sqlite3.connect('uniqueconstrain.db')
cursor = conn.cursor()
# Here we are creating table for users and inserting values into the table
cursor.execute('''CREATE TABLE users ( user_id INTEGER PRIMARY KEY, user_name TEXT NOT NULL, email TEXT NOT NULL UNIQUE); ''')
cursor.execute('''INSERT INTO users (user_id, user_name, email) VALUES (1, 'Lekha', 'Lekha@example.com');''')
cursor.execute('''INSERT INTO users (user_id, user_name, email) VALUES (2, 'Sarath', 'Sarath@example.com');''')
# Here we are selecting records from users
cursor.execute('''select *from users;''')
print(cursor.fetchall())

# Here we are trying to insert a user with the same email (Error Condition)
cursor.execute('''INSERT INTO users (user_id, user_name, email) VALUES (3, 'Lalith', 'Sarath@example.com');''')  
# committing to changes and closing the connection
conn.commit()
conn.close()
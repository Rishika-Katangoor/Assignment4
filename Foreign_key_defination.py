import sqlite3
conn = sqlite3.connect('foreignkeydefinition.db')
cursor = conn.cursor()
# Here we are creating a table for authors
cursor.execute('''
    CREATE TABLE authors (
        author_id INTEGER PRIMARY KEY,
        author_name TEXT NOT NULL);''')
# Here we are creating table for books
cursor.execute('''
    CREATE TABLE books (
        book_id INTEGER PRIMARY KEY,
        book_title TEXT NOT NULL,
        author_id INTEGER,
        FOREIGN KEY (author_id) REFERENCES authors(author_id));''')
# Here we are inserting values into authors table
cursor.executemany('''
    INSERT INTO authors (author_id, author_name) 
    VALUES (?, ?);''', [
    (1, 'Kiran Desai'),
    (2, 'Arundhati Roy'),
    (3, 'R.K Narayan')])
# Here we are selecting records from authors table
cursor.execute("Select *from authors")
print("\n Author Table \n")
rows = cursor.fetchall()
for row in rows:
    print(row) 
# Here we are inserting values into books table
cursor.executemany('''
    INSERT INTO books (book_id, book_title, author_id) 
    VALUES (?, ?, ?);''', [
    (1, 'The Inheritance of loss', 1),           
    (2, 'The God of Small Things', 2),      
    (3, 'Malgudi Days', 3)])
# Here we are selecting records from books table and printing the output
cursor.execute("Select *from books")
print("\n Books Table \n")
rows = cursor.fetchall()
for row in rows:
    print(row) 
# committing the changes and closing the connection   
conn.commit()
conn.close()
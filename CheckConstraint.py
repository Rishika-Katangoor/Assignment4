import sqlite3
conn = sqlite3.connect('checkconstraint.db')
cursor = conn.cursor()
# Here we are creating products table and inserting values into products table
cursor.execute('''CREATE TABLE products ( product_id INTEGER PRIMARY KEY, product_name TEXT NOT NULL, price REAL NOT NULL CHECK (price > 0));''')

cursor.execute(''' INSERT INTO products (product_id, product_name, price) VALUES (1, 'Laptop', 999.99);''')
cursor.execute('''INSERT INTO products (product_id, product_name, price) VALUES (2, 'Smartwatch', 0.1);''')
# Here we are selecting records from products table
cursor.execute('''select *from products''')
print(cursor.fetchall())

# Trying to insert price =  Zero to raise a error condition
cursor.execute('''INSERT INTO products (product_id, product_name, price) VALUES (2, 'Smartwatch', 0);''')
# Committing to changes and closing the connection
conn.commit()
conn.close()
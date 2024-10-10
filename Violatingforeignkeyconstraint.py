import sqlite3
conn = sqlite3.connect('violatingforeignkeyconstraint.db')
cursor = conn.cursor()

# Enabling foreign key constrain
cursor.execute('PRAGMA foreign_keys = ON;')
# Here we are creating customers and orders table, Inserting values into customers table and selecting records from customers
cursor.execute('''CREATE TABLE customers (customer_id INTEGER PRIMARY KEY, customer_name TEXT NOT NULL);''')
cursor.execute('''CREATE TABLE orders ( order_id INTEGER PRIMARY KEY, customer_id INTEGER, order_date TEXT, FOREIGN KEY (customer_id) REFERENCES customers(customer_id));''')
cursor.execute(''' INSERT INTO customers (customer_id, customer_name) VALUES (1, 'Lalith');''')
cursor.execute('''INSERT INTO customers (customer_id, customer_name) VALUES (2, 'Sarath');''')
cursor.execute('''select *from customers;''')
print(cursor.fetchall())
# Here we are inserting values into orders table and selecting records from orders table
cursor.execute('''INSERT INTO orders (order_id, customer_id, order_date) VALUES (1, 5, '2024-10-09');''')  
cursor.execute('''select *from orders;''')
print(cursor.fetchall())
# committing to changes and closing the connection 
conn.commit()
conn.close()
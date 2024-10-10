import sqlite3
connection = sqlite3.connect('CustomerOrders.db')
cursor = connection.cursor()
# Here we are creating customers table
cursor.execute('''CREATE TABLE IF NOT EXISTS customers ( customer_id INTEGER PRIMARY KEY,customer_name TEXT NOT NULL);''')
# Here we are creating table for orders
cursor.execute('''CREATE TABLE IF NOT EXISTS orders ( order_id INTEGER PRIMARY KEY,customer_id INTEGER,
               product_name TEXT NOT NULL,FOREIGN KEY (customer_id) REFERENCES customers(customer_id));''')
# Here we are inserting records into customer table 
cursor.executemany('''INSERT INTO customers (customer_id, customer_name) VALUES (?, ?);''', [
    (1, 'Lekha'),
    (2, 'Sarath'),
    (3, 'Bharath'),
    (4, 'Lalith'),
    (5, 'Anu')
])
# Here we are selecting the records from customers table
cursor.execute("Select *from customers")
print("\n Customers Table\n")
rows = cursor.fetchall()
for row in rows:
    print(row)
# Here we are inserting records into the orders table
cursor.executemany('''
    INSERT INTO orders (order_id, customer_id, product_name) VALUES (?, ?, ?);''', [
    (101, 1, 'Laptop'),
    (102, 2, 'Smartwatch'),
    (103, 1, 'Headphones'),
    (104, 3, 'Tablet'),
    (105, 4, 'Smartphone'),
    (106, 5, 'Camera'),
    (107, 3, 'Analogwatch'),
    (108, 2, 'BluetoothHeadset')
])
# Here we are selecting the records from orders table
cursor.execute("Select *from orders")
print("\n Orders Table \n")
rows = cursor.fetchall()
for row in rows:
    print(row)

# Here we are performing inner join between customer and order table
cursor.execute('''SELECT customers.customer_name, orders.product_name FROM customers 
               INNER JOIN orders ON customers.customer_id = orders.customer_id;''')
print("\n Inner Join \n")
rows = cursor.fetchall()
for row in rows:
    print(row)
connection.commit()
connection.close()
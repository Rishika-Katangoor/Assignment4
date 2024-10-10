import sqlite3
conn = sqlite3.connect('multiplejoin.db')
cursor = conn.cursor()
# Here we are creating table for customers
cursor.execute('''
    CREATE TABLE customers (
        customer_id INTEGER PRIMARY KEY,
        customer_name TEXT NOT NULL
    );
''')
# Here we are creating table for products
cursor.execute('''
    CREATE TABLE products (
        product_id INTEGER PRIMARY KEY,
        product_name TEXT NOT NULL
    );
''')
# Here we are creating a table for orders
cursor.execute('''
    CREATE TABLE orders (
        order_id INTEGER PRIMARY KEY,
        customer_id INTEGER,
        product_id INTEGER,
        order_date TEXT NOT NULL,
        FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
        FOREIGN KEY (product_id) REFERENCES products(product_id)
    );
''')
# Here we are inserting values into the customers table
cursor.executemany('''
    INSERT INTO customers (customer_id, customer_name) 
    VALUES (?, ?);
''', [
    (1, 'Lekha'),
    (2, 'Sarath'),
    (3, 'Bharath')
])
# Here we are selecting values from the customers table
cursor.execute("Select *from customers")
print("\n Customers Table \n")
rows = cursor.fetchall()
for row in rows:
    print(row) 
# Here we are inserting values into products table
cursor.executemany('''
    INSERT INTO products (product_id, product_name) 
    VALUES (?, ?);
''', [
    (1, 'Laptop'),
    (2, 'Smartwatch'),
    (3, 'Tablet'),
    (4, 'Camera')
])
# Here we are selecting records from products table
cursor.execute("Select *from products")
print("\n Products Table \n")
rows = cursor.fetchall()
for row in rows:
    print(row) 
# Here we are inserting values into the orders table
cursor.executemany('''
    INSERT INTO orders (order_id, customer_id, product_id, order_date) 
    VALUES (?, ?, ?, ?);
''', [
    (101, 1, 1, '2024-01-15'),  
    (102, 1, 2, '2024-01-20'), 
    (103, 2, 3, '2024-02-05'), 
    (104, 3, 4, '2024-02-10'), 
])
# Here we are selecting values from orders table
cursor.execute("Select *from orders")
print("\n Orders Table \n")
rows = cursor.fetchall()
for row in rows:
    print(row) 
# Here we are performing multiple join
cursor.execute('''
    SELECT customers.customer_name, products.product_name, orders.order_date
    FROM orders
    JOIN customers ON orders.customer_id = customers.customer_id
    JOIN products ON orders.product_id = products.product_id;
''')

rows = cursor.fetchall()
# printing the output
print("Customer Name  | Product Name  | Order Date")
print("-------------------------------------------")
for row in rows:
    customer_name = row[0]
    product_name = row[1]
    order_date = row[2]
    print(f"{customer_name:<14} | {product_name:<12} | {order_date}")
# committing to changes and closing the connection
conn.commit()
conn.close()
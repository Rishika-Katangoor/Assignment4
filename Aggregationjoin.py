import sqlite3
conn = sqlite3.connect('Joinwithaggregationjoin.db')
cursor = conn.cursor()
# Here we are creating a table for cusromers
cursor.execute('''
    CREATE TABLE IF NOT EXISTS customers (
        customer_id INTEGER PRIMARY KEY,
        customer_name TEXT NOT NULL
    );
''')
# Here we are creating a table for orders
cursor.execute('''
    CREATE TABLE IF NOT EXISTS orders (
        order_id INTEGER PRIMARY KEY,
        customer_id INTEGER,
        product_id INTEGER NOT NULL,
        FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
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
# Here we are selecting values from customers table
cursor.execute("Select *from customers")
print("\n Customers Table\n")
rows = cursor.fetchall()
for row in rows:
    print(row) 
# Here we are inserting values into the orders table
cursor.executemany('''
    INSERT INTO orders (order_id, customer_id, product_id) 
    VALUES (?, ?, ?);
''', [
    (101, 1, 1),  
    (102, 1, 2),  
    (103, 2, 1), 
    (104, 2, 3),  
    (105, 3, 2),  
    (106, 3, 4)  
])
# Here we are selecting records from the orders table
cursor.execute("Select *from orders")
print("\n Orders Table \n")
rows = cursor.fetchall()
for row in rows:
    print(row) 
# Here we are performing join with aggregation
cursor.execute('''
    SELECT customers.customer_name, COUNT(orders.product_id) AS total_products_ordered
    FROM customers
    JOIN orders ON customers.customer_id = orders.customer_id
    GROUP BY customers.customer_name;
''')

rows = cursor.fetchall()
# Here we are printing the output
print("\n Customer Name | Total Products Ordered")
print("--------------------------------------")
for row in rows:
    customer_name = row[0]
    total_products_ordered = row[1]
    print(f"{customer_name:<13} | {total_products_ordered}")
# Committing the changes and closing the connection
conn.commit()
conn.close()
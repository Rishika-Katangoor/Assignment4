import sqlite3
conn = sqlite3.connect('naturaljoin.db')
cursor = conn.cursor()
# Here we are creating a table for customers
cursor.execute('''
    CREATE TABLE customers (
        customer_id INTEGER PRIMARY KEY,
        customer_name TEXT NOT NULL
    );
''')
# Here we are creating a table for orders
cursor.execute('''
    CREATE TABLE orders (
        order_id INTEGER PRIMARY KEY,
        customer_id INTEGER,
        order_date TEXT NOT NULL,
        FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
    );
''')
# Here we are inserting the values into the customers table
cursor.executemany('''
    INSERT INTO customers (customer_id, customer_name) 
    VALUES (?, ?);
''', [
    (1, 'Lekha'),
    (2, 'Sarath'),
    (3, 'Bharath')
])
# Here we are selecting the values from the customers table
cursor.execute("Select *from customers")
print("\n Customers Table\n")
rows = cursor.fetchall()
for row in rows:
    print(row) 
# Here we are inserting values into the orders table
cursor.executemany('''
    INSERT INTO orders (order_id, customer_id, order_date) 
    VALUES (?, ?, ?);
''', [
    (101, 1, '2024-09-15'),  
    (102, 2, '2024-10-20'),  
    (103, 1, '2024-08-05'),  
    (104, 3, '2024-03-10')   
])
# Here we are selecting values from the orders table
cursor.execute("Select *from orders")
print("\n Orders Table \n")
rows = cursor.fetchall()
for row in rows:
    print(row) 

cursor.execute('''
    SELECT * 
    FROM customers
    NATURAL JOIN orders;
''')
# Here we are performing Natural Join
print("\n Natural Join \n")
rows = cursor.fetchall()
print("Customer Name | Order ID | Order Date")
print("-------------------------------------")
for row in rows:
    customer_name = row[1]  
    order_id = row[2]       
    order_date = row[3]    
    print(f"{customer_name:<14} | {order_id:<8} | {order_date}")

conn.commit()
conn.close()
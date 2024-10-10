import sqlite3
conn = sqlite3.connect('products_customers_crossjoin.db')
cursor = conn.cursor()
# Here we are creating a table for products
cursor.execute('''
    CREATE TABLE products (
        product_id INTEGER PRIMARY KEY,
        product_name TEXT NOT NULL);''')
# Here we are creating a table for customers
cursor.execute('''
    CREATE TABLE customers (
        customer_id INTEGER PRIMARY KEY,
        customer_name TEXT NOT NULL);''')
# Here we are inersting values into the products table
cursor.executemany('''
    INSERT INTO products (product_id, product_name) 
    VALUES (?, ?);
''', [
    (1, 'Laptop'),
    (2, 'Smartwatch'),
    (3, 'Tablet'),
    (4, 'Camera')
])
# Here we are selecting the values from the products table
cursor.execute("Select *from products")
print("\n Products Table\n")
rows = cursor.fetchall()
for row in rows:
    print(row) 
# Here we are inserting the values into the customers table
cursor.executemany('''
    INSERT INTO customers (customer_id, customer_name) 
    VALUES (?, ?);
''', [
    (1, 'Lekha'),
    (2, 'Sarath'),
    (3, 'Bharath'),
    (4, 'Lalith')
])
cursor.execute("Select *from customers")
print("\n Customers Table\n")
rows = cursor.fetchall()
for row in rows:
    print(row) 
cursor.execute('''
    SELECT products.product_name, customers.customer_name
    FROM products
    CROSS JOIN customers;
''')
print("Cross Join \n")
rows = cursor.fetchall()
print("Product Name  | Customer Name")
print("-----------------------------")
for row in rows:
    product_name = row[0]
    customer_name = row[1]
    print(f"{product_name:<12} | {customer_name}")

conn.commit()
conn.close()
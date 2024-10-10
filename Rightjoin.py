import sqlite3
conn = sqlite3.connect('productsuppliers_Rightjoin.db')
cursor = conn.cursor()
# Creating prodcuts table
cursor.execute('''
    CREATE TABLE products (
        product_id INTEGER PRIMARY KEY,
        product_name TEXT NOT NULL
    );
''')
# Creating the suppliers table
cursor.execute('''
    CREATE TABLE suppliers (
        supplier_id INTEGER PRIMARY KEY,
        supplier_name TEXT NOT NULL
    );
''')
# Creating table for product_suppliers
cursor.execute('''
    CREATE TABLE product_suppliers (
        product_id INTEGER,
        supplier_id INTEGER,
        FOREIGN KEY (product_id) REFERENCES products(product_id),
        FOREIGN KEY (supplier_id) REFERENCES suppliers(supplier_id)
    );
''')
# Here we are inserting values into products table
cursor.executemany('''
    INSERT INTO products (product_id, product_name) 
    VALUES (?, ?);
''', [
    (1, 'Laptop'),
    (2, 'Smartwatch'),
    (3, 'Tablet'),
    (4, 'Camera'),
    (5, 'Smartphone')
])
# Here we are selecting products from products table
cursor.execute("Select *from products")
print("\n Products Table\n")
rows = cursor.fetchall()
for row in rows:
    print(row) 
# Here we are inserting values into supliers table
cursor.executemany('''
    INSERT INTO suppliers (supplier_id, supplier_name) 
    VALUES (?, ?);
''', [
    (1, 'Kyndryl'),
    (2, 'DXC technologies'),
    (3, 'Cognizant')
])
# Here we are selecting supliers from supliers table
cursor.execute("Select *from suppliers")
print("\n Suppliers Table\n")
rows = cursor.fetchall()
for row in rows:
    print(row) 
# Here we are inserting values into product_suppliers table
cursor.executemany('''
    INSERT INTO product_suppliers (product_id, supplier_id) 
    VALUES (?, ?);
''', [
    (1, 1),  
    (2, 1),  
    (3, 2), 
    (4, 3)  
])
# Here we are inserting records into product and suppliers table
cursor.execute("Select *from product_suppliers")
print("\n Suppliers Table\n")
rows = cursor.fetchall()
for row in rows:
    print(row) 

cursor.execute('''
    SELECT products.product_name, suppliers.supplier_name  FROM products
    LEFT JOIN product_suppliers ON products.product_id = product_suppliers.product_id
    LEFT JOIN suppliers ON product_suppliers.supplier_id = suppliers.supplier_id;
''')

rows = cursor.fetchall()
# Here we are performing right join
print("Right Join")
for row in rows:
    print(row)

conn.commit()
conn.close()

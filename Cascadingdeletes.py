import sqlite3
conn = sqlite3.connect('cascadingdeletes.db')
cursor = conn.cursor()
# Here we are enabling foreign key constrain
cursor.execute('PRAGMA foreign_keys = ON;')
# Here we are creating a table for categories
cursor.execute(''' CREATE TABLE categories (
    category_id INTEGER PRIMARY KEY,
    category_name TEXT NOT NULL)''')
# Here we are creating a table for prodcuts
cursor.execute('''CREATE TABLE products (
    product_id INTEGER PRIMARY KEY,
    product_name TEXT NOT NULL,
    category_id INTEGER,
    FOREIGN KEY (category_id) REFERENCES categories(category_id) ON DELETE CASCADE)''')
categories = [(1, 'Electronics'),(2, 'Clothing'),(3, 'Books') ]
# Here we are inserting values into categories table
cursor.executemany('INSERT INTO categories (category_id, category_name) VALUES (?, ?)', categories)
products = [ (1, 'Smartphone', 1), (2, 'Laptop', 1), (3, 'Hoodie', 2), (4, 'Comic', 3)]

# Here we are inserting values into products table
cursor.executemany('INSERT INTO products (product_id, product_name, category_id) VALUES (?, ?, ?)', products)

# Printing the outputs
print("Initial data in categories table:")
cursor.execute('SELECT * FROM categories')
print(cursor.fetchall())

print("\nInitial data in products table:")
cursor.execute('SELECT * FROM products')
print(cursor.fetchall())

cursor.execute('DELETE FROM categories WHERE category_id = 1')

print("\nData in categories table after deleting category_id = 1 (Electronics):")
cursor.execute('SELECT * FROM categories')
print(cursor.fetchall())

print("\nData in products table after deleting category_id = 1 (Electronics):")
cursor.execute('SELECT * FROM products')
print(cursor.fetchall())

# committing to changes and closing the connection
conn.commit()
conn.close()
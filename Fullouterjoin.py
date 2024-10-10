import sqlite3
conn = sqlite3.connect('employees_departments_fullouterjoin.db')
cursor = conn.cursor()
# Here we are creating table for employees
cursor.execute('''
    CREATE TABLE employees (
        employee_id INTEGER PRIMARY KEY,
        employee_name TEXT NOT NULL,
        department_id INTEGER,
        FOREIGN KEY (department_id) REFERENCES departments(department_id)
    );
''')
# Here we are creating table for departments
cursor.execute('''
    CREATE TABLE departments (
        department_id INTEGER PRIMARY KEY,
        department_name TEXT NOT NULL
    );
''')
# Here we are inserting values into departments table
cursor.executemany('''
    INSERT INTO departments (department_id, department_name) 
    VALUES (?, ?);
''', [
    (1, 'Middleware'),
    (2, 'DataBase'),
    (3, 'Networking'),
    (4, 'UNIX')
])
# Here we are selecting values from departments table
cursor.execute("Select *from departments")
print("\n Departments Table\n")
rows = cursor.fetchall()
for row in rows:
    print(row) 
# Here we are inserting values into employees table
cursor.executemany('''
    INSERT INTO employees (employee_id, employee_name, department_id) 
    VALUES (?, ?, ?);
''', [
    (1, 'Lekha', 1),      
    (2, 'Sarath', 2),     
    (3, 'Bharath', None),  
    (4, 'Lalith', 3)      
])
# Here are selecting values from employees table
cursor.execute("Select *from employees")
print("\n Employees Table\n")
rows = cursor.fetchall()
for row in rows:
    print(row) 

cursor.execute('''
    SELECT employees.employee_name, departments.department_name
    FROM employees
    LEFT JOIN departments ON employees.department_id = departments.department_id

    UNION

    SELECT employees.employee_name, departments.department_name
    FROM departments
    LEFT JOIN employees ON employees.department_id = departments.department_id;
''')
# Here we are printing the output of full outer join
print("\n Full Outer Join \n")
rows = cursor.fetchall()
for row in rows:
    print(rows)

conn.commit()
conn.close()
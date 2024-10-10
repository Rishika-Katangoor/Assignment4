import sqlite3
conn = sqlite3.connect('primarykey.db')
cursor = conn.cursor()
# Here we are creating a table for courses
cursor.execute('''CREATE TABLE courses (course_id INTEGER,course_name TEXT NOT NULL,department_id INTEGER,PRIMARY KEY (course_id, department_id));''')
# Here we are inserting values into courses
cursor.execute('''INSERT INTO courses (course_id, course_name, department_id) VALUES (101, 'Database Systems', 1);''')
cursor.execute('''INSERT INTO courses (course_id, course_name, department_id)VALUES (101, 'Database Systems', 2);''')

try:
    cursor.execute('''INSERT INTO courses (course_id, course_name, department_id) VALUES (101, 'Advanced Databases', 1);''')
except sqlite3.IntegrityError as e:
    print("Error:", e) 
# Printing the output
print("\nCurrent data in the courses table:")
cursor.execute('SELECT * FROM courses')
for row in cursor.fetchall():
    print(row)
# committing to changes and closing the connection
conn.commit()
conn.close()
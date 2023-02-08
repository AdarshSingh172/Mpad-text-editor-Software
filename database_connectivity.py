import mysql.connector

conn = mysql.connector.connect(host='localhost', username='root', password='Mithlesh172!', database='new_database')

my_cursor = conn.cursor()

# query = "CREATE DATABASE new_database"
# query  = "SHOW DATABASES"

# my_cursor.execute(query)
# my_cursor.execute("CREATE TABLE student(name VARCHAR(225), age INT)")
# for database_name in my_cursor:
    # print(database_name)
# query = "INSERT INTO student(name, age) VALUES (%s, %s)"
values = [
    ('ADARSH', 23),
    ('NAINA', 22),
    ('TANYA', 21),
    ('VANDNA', 20),
    ('VARTIKA', 19),
    ('ANCHAL', 18),
]

query = "SELECT * FROM student"

my_cursor.execute(query)
print(my_cursor.fetchall())

conn.commit()
conn.close()                                                                                                                                                        
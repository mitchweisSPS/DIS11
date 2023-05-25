import sqlite3

connection = sqlite3.connect('/Users/mitchellweis/PycharmProjects/DIS11/House_points/House_points.db')

with open('schemas/schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO students (student_id, student_firstname, student_lastname, student_email, "
            "student_password, student_year, student_points) VALUES (?, ?, ?, ?, ?, ?, ?)",
            ('24485', 'Mitchell', 'Weis', '24485@stpauls.qld.edu.au', 'Password12345', '11', '0')
            )

connection.commit()
connection.close()

from flask import Flask, render_template, url_for, request, session
import sqlite3

connection = sqlite3.connect('/Users/mitchellweis/PycharmProjects/DIS11/House_points/House_points.db', check_same_thread=False)
cur = connection.cursor()

app = Flask(__name__)
app.config["SECRET_KEY"] = 'myverysecretkey'


def get_db_connection():
    conn = sqlite3.connect('House_points.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/")
def landingpage():
    return render_template('landingpage.html')


@app.route("/index/")
def index():
    return render_template('index.html')


@app.route("/myspace/")
def myspace():
    conn = get_db_connection()
    info = conn.execute('SELECT * FROM students WHERE student_email="'+session['student']+'"').fetchall()
    conn.commit()
    conn.close()
    return render_template('myspace.html', info=info)


@app.route("/stafflounge/", methods=['GET', 'POST'])
def stafflounge():
    if request.method == 'POST':
        connection = sqlite3.connect('/Users/mitchellweis/PycharmProjects/DIS11/House_points/House_points.db', check_same_thread=False)
        cur = connection.cursor()
        student_firstname = request.form['student_firstname']
        student_lastname = request.form['student_lastname']
        student_id = request.form['student_id']
        student_points = request.form['student_points']
        query = 'UPDATE students SET student_points="'+student_points+'" WHERE student_firstname="'+student_firstname+'" AND student_lastname="'+student_lastname+'" AND student_id="'+student_id+'"'
        cur.execute(query)
        connection.commit()
        connection.close()
    return render_template('stafflounge.html')


@app.route("/eventsmanager/", methods=['GET', 'POST'])
def eventsmanager():
    if request.method == 'POST':
        connection = sqlite3.connect('/Users/mitchellweis/PycharmProjects/DIS11/House_points/House_points.db', check_same_thread=False)
        cur = connection.cursor()
        event_id = request.form['event_id']
        event_name = request.form['event_name']
        event_time = request.form['event_time']
        event_date = request.form['event_date']
        event_desc = request.form['event_desc']
        cur.execute("INSERT INTO events (event_id, event_name, event_time, event_date, event_desc) VALUES (?, ?, ?, ?, ?)", (event_id, event_name, event_time, event_date, event_desc))
        connection.commit()
        connection.close()
    return render_template('eventsmanager.html')


@app.route("/house/")
def house():
    conn = get_db_connection()
    students = conn.execute('SELECT * FROM students WHERE house_name="'+session['studenthouse']+'"').fetchall()
    conn.commit()
    conn.close()
    return render_template('house.html', students=students)


@app.route("/tutor/")
def tutor():
    conn = get_db_connection()
    students = conn.execute('SELECT * FROM students WHERE house_name="'+session['staffhouse']+'" AND tutor_group="'+session['stafftutor']+'"').fetchall()
    conn.commit()
    conn.close()
    return render_template('tutor.html', students=students)


@app.route("/events/")
def events():
    conn = get_db_connection()
    events = conn.execute('SELECT * FROM events').fetchall()
    conn.commit()
    conn.close()
    return render_template('events.html', events=events)


@app.route("/leaderboards/")
def leaderboards():
    conn = get_db_connection()
    students = conn.execute('SELECT * FROM students ORDER BY student_points DESC').fetchall()
    conn.commit()
    conn.close()
    return render_template('leaderboards.html', students=students)


@app.route("/register/")
def register():
    return render_template('register.html')


@app.route("/login/")
def login():
    return render_template('login.html')


@app.route("/logout/")
def logout():
    return render_template('logout.html')


@app.route("/stafflogin/", methods=['GET', 'POST'])
def stafflogin():
    if request.method == 'POST':
        connection = sqlite3.connect('/Users/mitchellweis/PycharmProjects/DIS11/House_points/House_points.db', check_same_thread=False)
        cur = connection.cursor()
        staff_email = request.form['staff_email']
        staff_password = request.form['staff_password']
        query = 'SELECT staff_email, staff_password FROM staff WHERE staff_email="'+staff_email+'" AND staff_password="'+staff_password+'"'
        cur.execute(query)
        results = cur.fetchall()

        cur.execute('SELECT house_name FROM staff WHERE staff_email="'+staff_email+'"')
        house_name1 = cur.fetchall()
        house_name = str(house_name1).strip("'[(,)]'")
        session['staffhouse'] = house_name

        cur.execute('SELECT tutor_group FROM staff WHERE staff_email="'+staff_email+'"')
        tutor_group1 = cur.fetchall()
        tutor_group = str(tutor_group1).strip("'[(,)]'")
        session['stafftutor'] = tutor_group

        connection.commit()
        connection.close()

        if len(results) == 0:
            print("Wrong email or Password")
        else:
            session['role'] = "staff"
            return render_template('index.html')

    return render_template('stafflogin.html')


@app.route("/staffregister/", methods=['GET', 'POST'])
def staffregister():
    if request.method == 'POST':
        connection = sqlite3.connect('/Users/mitchellweis/PycharmProjects/DIS11/House_points/House_points.db', check_same_thread=False)
        cur = connection.cursor()
        staff_id = request.form['staff_id']
        staff_firstname = request.form['staff_firstname']
        staff_lastname = request.form['staff_lastname']
        staff_email = request.form['staff_email']
        staff_password = request.form['staff_password']
        house_name = request.form['house_name']
        tutor_group = request.form['tutor_group']
        cur.execute("INSERT INTO staff (staff_id, staff_firstname, staff_lastname, staff_email, staff_password, house_name, tutor_group) VALUES (?, ?, ?, ?, ?, ?, ?)", (staff_id, staff_firstname, staff_lastname, staff_email, staff_password, house_name, tutor_group))
        session['staffhouse'] = house_name
        connection.commit()
        connection.close()
    return render_template('staffregister.html')


@app.route("/studentlogin/", methods=['GET', 'POST'])
def studentlogin():
    if request.method == 'POST':
        connection = sqlite3.connect('/Users/mitchellweis/PycharmProjects/DIS11/House_points/House_points.db', check_same_thread=False)
        cur = connection.cursor()
        student_email = request.form['student_email']
        student_password = request.form['student_password']

        query = 'SELECT student_email, student_password FROM students WHERE student_email="'+student_email+'" AND student_password="'+student_password+'"'
        cur.execute(query)
        results = cur.fetchall()

        cur.execute('SELECT house_name FROM students WHERE student_email="'+student_email+'"')
        house_name1 = cur.fetchall()
        house_name = str(house_name1).strip("'[(,)]'")
        session['studenthouse'] = house_name

        connection.commit()
        connection.close()

        if len(results) == 0:
            print("Wrong email or Password")
        else:
            session['role'] = "student"
            session['student'] = student_email
            return render_template('index.html')

    return render_template('login.html')


@app.route("/studentregister/", methods=['GET', 'POST'])
def studentregister():
    if request.method == 'POST':
        connection = sqlite3.connect('/Users/mitchellweis/PycharmProjects/DIS11/House_points/House_points.db', check_same_thread=False)
        cur = connection.cursor()
        student_email = request.form['student_email']
        student_password = request.form['student_password']

        #query = 'INSERT student_email, student_password FROM students WHERE student_email="'+student_email+'" AND student_password="'+student_password+'"'
        cur.execute("INSERT INTO students (student_email, student_password) VALUES (?, ?)", (student_email, student_password))
        connection.commit()
        connection.close()
    return render_template('register.html')


if __name__ == '__main__':
    host = '127.0.0.1'
    port = 5000
    app.run(host, port, debug=True)

import json

from flask import Flask, render_template, request, session
import requests
import sqlite3

app = Flask(__name__)
app.config["SECRET_KEY"] = 'myverysecretkey'


@app.route("/")
def landingpage():
    return render_template('landingpage.html')


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        connection = sqlite3.connect('/Users/mitchellweis/PycharmProjects/DIS11/Northside_DJ/northsidedj.db', check_same_thread=False)
        cur = connection.cursor()
        username = request.form['username']
        password = request.form['password']
        query = 'SELECT username, password FROM users WHERE username="'+username+'" AND password="'+password+'"'
        cur.execute(query)
        results = cur.fetchall()

        connection.commit()
        connection.close()

        if len(results) == 0:
            print("Wrong email or Password")
        else:
            session['username'] = username
            return render_template('index.html')
    return render_template('login.html')


@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        connection = sqlite3.connect('/Users/mitchellweis/PycharmProjects/DIS11/Northside_DJ/northsidedj.db', check_same_thread=False)
        cur = connection.cursor()
        username = request.form['username']
        password = request.form['password']
        cur.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        connection.commit()
        connection.close()
    return render_template('register.html')


@app.route('/index', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        artist_name = request.form['artist']
        albums = search_songs(artist_name)
        save_albums_to_db(artist_name, albums)
        return render_template('results.html', artist=artist_name, albums=albums)
    return render_template('search.html')


@app.route('/results', methods=['GET', 'POST'])
def results():
    return render_template('results.html')


@app.route('/events', methods=['GET', 'POST'])
def events():
    if request.method == 'POST':
        connection = sqlite3.connect('/Users/mitchellweis/PycharmProjects/DIS11/Northside_DJ/northsidedj.db', check_same_thread=False)
        cur = connection.cursor()
        event_id = request.form['event_id']
        event_name = request.form['event_name']
        event_time = request.form['event_time']
        event_date = request.form['event_date']
        event_dj = request.form['event_dj']
        cur.execute("INSERT INTO events (event_id, event_name, event_time, event_date, event_dj) VALUES (?, ?, ?, ?, ?)", (event_id, event_name, event_time, event_date, event_dj))
        connection.commit()
        connection.close()

    connection = sqlite3.connect('/Users/mitchellweis/PycharmProjects/DIS11/Northside_DJ/northsidedj.db', check_same_thread=False)
    cur = connection.cursor()
    events = cur.execute('SELECT * FROM events').fetchall()
    connection.commit()
    connection.close()
    return render_template('events.html', events=events)


@app.route('/queue', methods=['GET', 'POST'])
def queue():
    return render_template('queue.html')


@app.route("/logout")
def logout():
    return render_template('landingpage.html')


def search_songs(artist_name):
    API_KEY = '523532'
    mydata1 = None
    URL = f'https://theaudiodb.com/api/v1/json/{API_KEY}/searchalbum.php?s={artist_name}'
    response = requests.get(URL)
    source = response.text
    data = json.loads(source)
    a = data['album']
    albums = []
    for item in a:
        albums.append(item['idAlbum'])
    print(albums)
    for album in albums:
        tracks = f'https://theaudiodb.com/api/v1/json/523532/track.php?m={album}'
        response1 = requests.get(tracks)
        #source1 = response1.text
        data1 = response1.json()
        mydata1 = data1['track']
    return mydata1


def save_albums_to_db(artist_name, albums):
    conn = sqlite3.connect('northsidedj.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS albums
                 (artist TEXT, album TEXT)''')

    for album in albums:
        c.execute("INSERT INTO albums VALUES (?,?)", (artist_name, album['strAlbum']))
    conn.commit()
    conn.close()


if __name__ == '__main__':
    app.run(debug=True)

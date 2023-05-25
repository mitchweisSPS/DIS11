from FlaskApp1 import app, db, api
from flask import render_template, request, json, jsonify, Response, redirect, flash, url_for, session
from FlaskApp1.models import User, Course, Enrollment
from FlaskApp1.forms import LoginForm, RegisterForm, NumbersForm, LetterForm, CalcForm, GameForm
from flask_restx import Resource
from FlaskApp1.course_list import course_list
import random

courseData = [{"courseID":"1111","title":"PHP 101","description":"Intro to PHP","credits":3,"term":"Fall, Spring"}, {"courseID":"2222","title":"Java 1","description":"Intro to Java Programming","credits":4,"term":"Spring"}, {"courseID":"3333","title":"Adv PHP 201","description":"Advanced PHP Programming","credits":3,"term":"Fall"}, {"courseID":"4444","title":"Angular 1","description":"Intro to Angular","credits":3,"term":"Fall, Spring"}, {"courseID":"5555","title":"Java 2","description":"Advanced Java Programming","credits":4,"term":"Fall"}]

#####################################

@api.route('/api','/api/')
class GetAndPost(Resource):

    #GET ALL
    def get(self):
        return jsonify(User.objects.all())

    #POST
    def post(self):
        data = api.payload
        user = User(user_id=data['user_id'], email=data['email'], first_name=data['first_name'], last_name=data['last_name'])
        user.set_password(data['password'])
        user.save()
        return jsonify(User.objects(user_id=data['user_id']))

@api.route('/api/<idx>')
class GetUpdateDelete(Resource):

    #GET ONE
    def get(self, idx):
        return jsonify(User.objects(user_id=idx))

    #PUT
    def put(self,idx):
        data = api.payload
        User.objects(user_id=idx).update(**data)
        return jsonify(User.objects(user_id=idx))

    #DELETE
    def delete(self,idx):
        User.objects(user_id=idx).delete()
        return jsonify("User is deleted!")

#####################################

@app.route("/")
@app.route("/index")
@app.route("/home")
def index():
    return render_template("index.html", login=False, index=True)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if session.get('username'):
        return redirect(url_for('index'))

    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        user = User.objects(email=email).first()
        if user and user.get_password(password):
            flash(f"{user.first_name}, you are successfully logged in!", "success")
            session['user_id'] = user.user_id
            session['username'] = user.first_name
            return redirect("/index")
        else:
            flash("Sorry, something went wrong.", "danger")
    return render_template("login.html", title="Login", form=form, login=True)


@app.route("/logout")
def logout():
    session['user_id']=False
    session.pop('username', None)
    return redirect(url_for('index'))


@app.route("/courses/")
@app.route("/courses/<term>")
def courses(term = None):
    if term is None:
        term = "Spring 2022"
    classes = Course.objects.order_by("+courseID")
    return render_template("courses.html", courseData=classes, courses=True, term=term)
    #return render_template("courses.html", courses=True)


@app.route("/register", methods=['POST', 'GET'])
def register():
    if session.get('username'):
        return redirect(url_for('index'))
    form = RegisterForm()
    if form.validate_on_submit():
        user_id = User.objects.count()
        user_id += 1

        email = form.email.data
        password = form.password.data
        first_name = form.first_name.data
        last_name = form.last_name.data

        user = User(user_id=user_id, email=email, first_name=first_name, last_name=last_name)
        user.set_password(password)
        user.save()
        flash("You are successfully registered", "success")
        return redirect(url_for("index"))
    return render_template("register.html", title="Register", form=form, register=True)


@app.route("/enrollment", methods=["GET", "POST"])
def enrollment():
    if session.get('username'):
        return redirect(url_for('login'))

    courseID = request.form.get('courseID')
    courseTitle = request.form.get('title')
    user_id = session.get('user_id')

    if courseID:
        if Enrollment.objects(user_id=user_id, courseID=courseID):
            flash(f"Oops! You are already registered in the course called {courseTitle}!", "danger")
            return redirect(url_for("courses"))
        else:
            Enrollment(user_id=user_id, courseID=courseID).save()
            flash(f"You are enrolled in {courseTitle}!", "success")

    courses = course_list()

    return render_template("enrollment.html", enrollment=True, title="Enrollment", classes=courses)



#@app.route("/api/")
#@app.route("/api/<idx>")
#def api(idx=None):
#   if(idx == None):
#        jdata = courseData
#    else:
#        jdata = courseData[int(idx)]
#
#    return Response(json.dumps(jdata), mimetype="application/json")

@app.route("/user")
def user():
    #User(user_id=1, first_name="Christian", last_name="Hur", email="christian@uta.com", password="abc1234").save()
    #User(user_id=2, first_name="Mary", last_name="Jane", email="mary.jane@uta.com", password="password123").save()
    users = User.objects.all()
    return render_template("user.html", users=users)


@app.route("/numbers")
def numbers():
    form = NumbersForm()
    if form.validate_on_submit():
        number_one = form.number_one.data
        number_two = form.number_two.data

    return render_template("numbers.html", form=form)

@app.route("/calcdf", methods=['GET'])
def calcdf():
    """ Displays the calcdf page accessible at '/calcdf """
    return render_template('calcdf.html')

@app.route("/operation_result/", methods=['POST'])
def operation_result():
    error = None
    result = None
#    form = CalcForm()

    first_input = request.form['Input1']
    second_input = request.form['Input2']
    operation = request.form['operation']
    print(type(first_input))

    try:
        input1 = float(first_input)
        input2 = float(second_input)

        if operation == "+":
            result = input1 + input2
            print(result)

        elif operation == "-":
            result = input1 - input2

        elif operation == "/":
            result = input1 / input2

        elif operation == "*":
            result = input1 * input2

        else:
            operation = "%"
            result = input1 % input2

        return render_template(
            'calcdf.html',
            input1=input1,
            input2=input2,
            operation=operation,
            result=round(result, 2),
            calculation_success=True
            )
    except ZeroDivisionError:
        return render_template(
            'calcdf.html',
            input1=input1,
            input2=input2,
            operation=operation,
            result="Bad Input",
            calculation_success=False,
            error="You cannot divide by Zero"
        )

    except ValueError:
        return render_template(
            'calcdf.html',
            input1=first_input,
            input2=second_input,
            operation=operation,
            result="Bad Input",
            calculation_success=False,
            error="You cannot perform numeric operations with provided input"
        )


@app.route("/letter_count", methods=['GET'])
def letter_count():

    return render_template('letter_count.html')


@app.route("/letter_count_result", methods=['POST'])
def letter_count_result():
    form = LetterForm
    word = request.form['word']

    my_dict = {}
    for letter in word:
        my_dict[letter] = my_dict.get(letter, 0) + 1

    print(f'There are {len(word)} total letters in the word {word}.')
    print(f'There are {len(my_dict)} unique letters in the word {word}.')


    return render_template(
            'letter_count.html',
            word=word,
            form=form,
            my_dict=my_dict,
            letter_success=True
            )


@app.route("/game", methods=['GET'])
def game():

    return render_template("game.html")


@app.route("/game_result", methods=['POST'])
def game_result():
    form = GameForm()
    chosen_pick = request.form['pick']

    pick = int(chosen_pick)
    pick2 = random.randint(0, 4)

    winner = None

    if pick == "0":
        if pick2 == "0":
            winner = 2
        elif pick2 == "1":
            winner = 1
        elif pick2 == "2":
            winner = 3
        elif pick2 == "3":
            winner = 1
        elif pick2 == "4":
            winner = 3

    elif pick == "1":
        if pick2 == "0":
            winner = 3
        elif pick2 == "1":
            winner = 2
        elif pick2 == "2":
            winner = 1
        elif pick2 == "3":
            winner = 3
        elif pick2 == "4":
            winner = 1

    elif pick == "2":
        if pick2 == "0":
            winner = 1
        elif pick2 == "1":
            winner = 3
        elif pick2 == "2":
            winner = 2
        elif pick2 == "3":
            winner = 3
        elif pick2 == "4":
            winner = 1

    elif pick == "3":
        if pick2 == "0":
            winner = 3
        elif pick2 == "1":
            winner = 1
        elif pick2 == "2":
            winner = 1
        elif pick2 == "3":
            winner = 2
        elif pick2 == "4":
            winner = 3

    elif pick == "4":
        if pick2 == "0":
            winner = 1
        elif pick2 == "1":
            winner = 3
        elif pick2 == "2":
            winner = 3
        elif pick2 == "3":
            winner = 1
        elif pick2 == "4":
            winner = 2

    return render_template("game.html", form=form, pick=pick, game_success=True, pick2=pick2, winner=winner)



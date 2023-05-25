from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError
from FlaskApp1.models import User


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=6, max=15)])
    remember_me = (BooleanField("Remember Me"))
    submit = SubmitField("Login")


class NumbersForm(FlaskForm):
    number_one = IntegerField("First Number")
    number_two = IntegerField("Second Number")
    calculate = SubmitField("Calculate")


class LetterForm(FlaskForm):
    word = StringField("Input word")
    enter = SubmitField("Enter")


class CalcForm(FlaskForm):
    num1 = IntegerField("Num1", validators=[DataRequired()])
    num2 = IntegerField("Num2", validators=[DataRequired()])
    submit = SubmitField("Submit")


class GameForm(FlaskForm):
    submit = SubmitField("Submit")


class RegisterForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=6, max=15)])
    password_confirm = PasswordField("Confirm Password", validators=[DataRequired(), Length
    (min=6, max=15), EqualTo('password')])
    first_name = StringField("First Name", validators=[DataRequired(), Length(min=2, max=55)])
    last_name = StringField("Last Name", validators=[DataRequired(), Length(min=2, max=55)])
    submit = SubmitField("Register Now")

    def validate_email(self, email):
        user = User.objects(email=email.data).first()
        if user:
            raise ValidationError("Email is already in use. Pick another one.")

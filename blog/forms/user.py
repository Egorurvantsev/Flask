from flask_wtf import FlaskForm
from wtforms import StringField, validators, PasswordField, EmailField, SubmitField


class UserRegisterForm(FlaskForm):
    firstname = StringField('Firstname', [validators.DataRequired()])
    lastname = StringField('Lastname')
    email = EmailField('Email', [validators.DataRequired(), validators.Email()])
    password = PasswordField('Password', [validators.DataRequired(), validators.EqualTo('confirm')])
    confirm = PasswordField('Password', [validators.DataRequired()])
    submit = SubmitField('Register')
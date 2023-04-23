from flask_login import UserMixin

from blog.app import db


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(255), unique=True)
    firstname = db.Column(db.String(255))
    lastname = db.Column(db.String(255))
    password = db.Column(db.String(255))

    def __init__(self, email, firstname, lastname,  password):
        self.email = email
        self.firstname = firstname
        self.lastname = lastname
        self.password = password


class Article(db.Model):
    __tablename__ = 'articles'

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(255))
    author_id = db.Column(db.String(255), db.ForeignKey('users.id'))
from flask_login import UserMixin
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

from blog.app import db


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(255), unique=True)
    firstname = db.Column(db.String(255))
    lastname = db.Column(db.String(255))
    password = db.Column(db.String(255))

    author = relationship('Author', uselist=False, back_populates='user')

    def __init__(self, email, firstname, lastname,  password):
        self.email = email
        self.firstname = firstname
        self.lastname = lastname
        self.password = password


class Author(db.Model):
    __tablename__ = 'authors'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey('users.id'), nullable=False)

    user = relationship('User', back_populates='author')
    article = relationship('Article', back_populates='author')



class Article(db.Model):
    __tablename__ = 'articles'

    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, ForeignKey('authors.id'), nullable=False)
    title = db.Column(db.String(255))
    text = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    author = relationship('Author', back_populates='article')
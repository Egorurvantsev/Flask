from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from blog.articles.views import article
from blog.users.views import user


db = SQLAlchemy()



def create_app() -> Flask:
    from .models import User
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '!)zjpg+^i5wf^j6y@9j*c+vhl^_0_lk1a4pg=pqoftvl%8+!14'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"


    db.init_app(app)


    register_blueprints(app)
    return app


def register_blueprints(app: Flask):
    app.register_blueprint(user)
    app.register_blueprint(article)
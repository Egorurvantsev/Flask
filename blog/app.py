from flask import Flask, redirect, url_for
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

from blog.auth.views import auth
from blog.articles.views import article
from blog.users.views import user


db = SQLAlchemy()

login_manager = LoginManager()



def create_app() -> Flask:
    from .models import User
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '!)zjpg+^i5wf^j6y@9j*c+vhl^_0_lk1a4pg=pqoftvl%8+!14'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"


    db.init_app(app)

    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        User.query.get(int(user_id))

    register_blueprints(app)
    return app


def register_blueprints(app: Flask):
    app.register_blueprint(user)
    app.register_blueprint(article)
    app.register_blueprint(auth)
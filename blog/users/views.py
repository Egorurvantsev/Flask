from flask import Blueprint, render_template
from flask_login import login_required
from werkzeug.exceptions import NotFound
from blog.users.models import User

user = Blueprint('users', __name__, url_prefix='/users', static_folder='../static')


@user.route('/')
def user_list():
    users = User.query.all()
    return render_template('users/list.html', users=users)


@user.route('/<int:pk>')
@login_required
def profile(pk: int):
    selected_user = User.query.filter_by(id=pk).one_or_none()
    if not selected_user:
        raise NotFound(f"Пользователя с таким именем нет")

    return render_template('users/profile.html', user=selected_user)
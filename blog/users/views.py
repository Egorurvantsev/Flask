from flask import Blueprint, render_template
from flask_login import login_required
from werkzeug.exceptions import NotFound

user = Blueprint('users', __name__, url_prefix='/users', static_folder='../static')


USERS = {
    1: {'firstname': 'Egor', 'lastname': 'Urvantsev', 'age': '15'},
    2: {'firstname': 'Igor', 'lastname': 'Urvantsev', 'age': '41'},
    3: {'firstname': 'Sasha', 'lastname': 'Involver', 'age': '40'},
}


@user.route('/')
def user_list():
    from blog.models import User
    users = User.query.all()
    return render_template('users/list.html', users=users)


@user.route('/<int:pk>')
# @login_required
def profile(pk: int):
    from blog.models import User
    try:
        _user = User.query.filter_by(id=pk).one_or_none()
    except KeyError:
        raise NotFound(f'Пользователя с id {pk} не существует')

    return render_template('users/profile.html', user=_user)
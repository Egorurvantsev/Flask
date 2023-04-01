from flask import Blueprint, render_template, redirect

user = Blueprint('users', __name__, url_prefix='/users', static_folder='../static')


USERS = {
    1: {'firstname': 'Egor', 'lastname': 'Urvantsev', 'age': '15'},
    2: {'firstname': 'Igor', 'lastname': 'Urvantsev', 'age': '41'},
    3: {'firstname': 'Sasha', 'lastname': 'Involver', 'age': '40'},
}


@user.route('/')
def user_list():
    return render_template('users/list.html', users=USERS)


@user.route('/<int:pk>')
def get_user(pk: int):
    try:
        user_name = USERS[pk]
    except KeyError:
        return redirect('/users/')

    return render_template('users/detail.html', user=user_name)
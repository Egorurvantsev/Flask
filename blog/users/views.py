from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import login_required, current_user, login_user
from werkzeug.exceptions import NotFound
from werkzeug.security import generate_password_hash

from blog.extensions import db
from blog.forms.user import UserRegisterForm
from blog.models import User

user = Blueprint('users', __name__, url_prefix='/users', static_folder='../static')

@user.route('register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('users.profile', pk=current_user.id))

    form = UserRegisterForm(request.form)
    errors = []
    if request.method == 'POST' and form.validate_on_submit():
        if User.query.filter_by(email=form.email.data).count():
            form.email.errors.append('Почта не уникальна')
            return render_template('users/register.html', form=form)

        _user = User(
            email=form.email.data,
            firstname=form.firstname.data,
            lastname=form.lastname.data,
            password=generate_password_hash(form.password.data),
        )

        db.session.add(_user)
        db.session.commit()
        login_user(_user)

    return render_template('users/register.html', form=form, errors=errors)
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
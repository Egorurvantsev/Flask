from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import logout_user, login_user, login_required
from werkzeug.security import check_password_hash


auth = Blueprint('auth', __name__, static_folder='../static')

@auth.route('/login', methods=['POST', 'GET'])
def login():
    from blog.models import User
    if request.method == 'GET':
        return render_template('auth/login.html')

    email = request.form.get('email')
    password = request.form.get('password')
    user = User.query.filter_by(email=email).first()

    if not user or not check_password_hash(user.password, password):
        flash('Проверьте правильность введенных данных!')
        return redirect(url_for('.login'))

    login_user(user)
    return redirect(url_for('users.profile', pk=user.id))


@auth.route('/logout')
# @login_required
def logout():
    logout_user()
    return redirect(url_for('.login'))

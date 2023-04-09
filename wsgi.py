from werkzeug.security import generate_password_hash

from blog.app import create_app, db

app = create_app()


@app.cli.command('init-db')
def init_db():
    db.create_all()


@app.cli.command('create-users')
def create_users():
    from blog.models import User
    admin = User(email='egor@gmail.com', password=generate_password_hash('egorka'))
    db.session.add(admin)
    db.session.commit()
import click
from werkzeug.security import generate_password_hash
from blog.extensions import db


@click.command('create-init-user')
def create_init_user():
    from blog.models import User
    from wsgi import app

    with app.app_context():
        db.session.add(
            User(email='egor@gmail.om', password=generate_password_hash('123'), firstname='Egor', lastname='Urvantsev')
        )
        db.session.commit()


@click.command('create-init-tags')
def create_init_tags():
    from blog.models import Tag
    from wsgi import app

    with app.app_context():
        tags = ['flask', 'django', 'python', 'gb', 'sqlite']
        for item in tags:
            db.session.add(Tag(name=item))
        db.session.commit()
    click.echo('Теги созданы')
from blog.app import create_app, db

app = create_app()
@app.cli.command('init-db')
def init_db():
    db.create_all()
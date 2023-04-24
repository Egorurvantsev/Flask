from flask import Blueprint, render_template
from werkzeug.exceptions import NotFound
from blog.models import Article

article = Blueprint('articles', __name__, url_prefix='/articles', static_folder='../static')


@article.route('/')
def article_list():
    articles = Article.query.all()
    return render_template('articles/list.html', articles=articles)


@article.route('/<int:pk>')
def get_article(pk: int):
    selected_article = Article.query.filter_by(id=pk).one_or_none()
    if not selected_article:
        raise NotFound(f"Статьи с таким именем нет")

    return render_template('articles/detail.html', article=selected_article)
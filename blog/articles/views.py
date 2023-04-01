from flask import Blueprint, render_template, redirect

article = Blueprint('articles', __name__, url_prefix='/articles', static_folder='../static')


ARTICLES = {
    1: {'text': 'qwerty', 'author': 2},
    2: {'text': 'wasd', 'author': 1},
    3: {'text': 'russiaisgood', 'author': 1},
    4: {'text': 'americaissuck', 'author': 3},
}


@article.route('/')
def article_list():
    return render_template('articles/list.html', articles=ARTICLES)


@article.route('/<int:pk>')
def get_article(pk: int):
    try:
        article_name = ARTICLES[pk]
    except KeyError:
        return redirect('/articles/')

    return render_template('articles/detail.html', article=article_name)
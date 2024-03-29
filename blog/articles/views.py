from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from sqlalchemy.orm import joinedload
from werkzeug.exceptions import NotFound

from blog.extensions import db
from blog.forms.article import CreateArticleForm
from blog.models import Article, Author, Tag

article = Blueprint('articles', __name__, url_prefix='/articles', static_folder='../static')


@article.route('/', methods=['GET'])
def article_list():
    articles = Article.query.all()
    return render_template('articles/list.html', articles=articles)


@article.route('/<int:pk>', methods=['GET'])
def get_article(pk: int):
    selected_article = Article.query.filter_by(id=pk).options(joinedload(Article.tags)).one_or_none()
    if not selected_article:
        raise NotFound(f"Статьи с таким именем нет")

    return render_template('articles/details.html', article=selected_article)


@article.route('/create/', methods=['GET'])
@login_required
def create_article_form():
    form = CreateArticleForm(request.form)
    form.tags.choices = [(tag.id, tag.name) for tag in Tag.query.order_by('name')]
    return render_template('articles/create.html', form=form)


@article.route('/', methods=['POST'])
@login_required
def create_article():
    form = CreateArticleForm(request.form)
    form.tags.choices = [(tag.id, tag.name) for tag in Tag.query.order_by('name')]

    if form.validate_on_submit():
        _article = Article(title=form.title.data.strip(), text=form.text.data)

        if current_user.author:
            _article.author_id = current_user.author.id
        else:
            author = Author(user_id=current_user.id)
            db.session.add(author)
            db.session.flush()
            _article.author_id = author.id

        if form.tags.data:
            selected_tags = Tag.query.filter(Tag.id.in_(form.tags.data))
            for tag in selected_tags:
                _article.tags.append(tag)

        db.session.add(_article)
        db.session.commit()

        return redirect(url_for('articles.get_article', pk=_article.id))

    return render_template('articles/create.html', form=form)
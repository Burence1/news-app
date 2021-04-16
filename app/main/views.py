from flask import render_template,request,redirect,url_for
from .import main
from ..requests import get_article

#Views
@main.route('/')
def index():
  '''
  View root page function that returns the index page and its data
  '''

  #Getting latest articles
  latest_articles = get_article('publishedAt')

  title = 'Best news app'

  return render_template('.index', publishedAt=publishedAt)

@main.route('/articles/publishedAt')
def articles(publishedAt):
  articles = get_article(publishedAt)
  title = f'{article_item.title}'
  latest = publishedAt

  return render_template('.index',title=title,latest=publishedAt)
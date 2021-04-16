from flask import render_template,request,redirect,url_for
from .import main
from ..requests import get_source

#Views
@main.route('/')
def index():
  '''
  View root page function that returns the index page and its data
  '''

  #Getting articles sources
  technology_source = get_source('technology')
  business_source = get_source('business')
  entertainment_source = get_source('entertainment')
  science_source = get_source('science')
  sports = get_source('sports')
  general = get_source('general')

  title = 'Best news app'

  return render_template('.index' title=title,technology=technology_source)

@main.route('/articles/publishedAt')
def articles(publishedAt):
  articles = get_article(publishedAt)
  title = f'{article_item.title}'
  latest = publishedAt

  return render_template('.index',title=title,latest=publishedAt)
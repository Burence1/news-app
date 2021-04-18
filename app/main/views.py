from flask import render_template,request,redirect,url_for
from .import main
from ..requests import get_source,get_all_articles,get_articles,get_top_headlines,search_article

#Views
@main.route('/')
def index():
  '''
  View root page function that returns the index page and its data
  '''
  #Getting articles sources
  general_source = get_source('general')
  technology_source = get_source('technology')
  business_source = get_source('business')
  entertainment_source = get_source('entertainment')
  science_source = get_source('science')
  sports_source = get_source('sports')
  health_source = get_source('health')

  title = 'Best news app'

  search_article = request.args.get('article_query')

  if search_article:
    return redirect(url_for('.search',article_name=search_article))
  else:
    return render_template('index.html', title=title,general=general_source,technology=technology_source,business=business_source,science=science_source,
    sports=sports_source,entertainment=entertainment_source,health=health_source)


@main.route('/articles/<source_id>&<int:per_page>')
def articles(source_id,per_page):
  '''
  view function for returning articles
  '''
  article_source = get_articles(source_id,per_page)

  title = f'{source_id}'
  search_article = request.args.get('article_query')

  if search_article:
    return redirect(url_for('.search', article_name=search_article))

  else:
    return render_template('articles.html', title=title, name=source_id,articles=article_source)


@main.route('/topheadlines&<int:per_page>')
def top_stories(per_page):
  '''
  view function for top stories
  '''
  top_stories_articles = get_top_headlines(per_page)

  title = 'Top Stories'

  search_article = request.args.get('article_query')
  if search_article:
    return redirect(url_for('.search',article_name=search_article))
  else:
    return render_template('topstories.html',title=title,name='Top Stories',articles=top_stories_articles)


@main.route('/everything&<int:per_page>')
def all_stories(per_page):
  '''
  view function for all stories
  '''
  all_stories_articles = get_all_articles(per_page)
  
  title = 'All Stories'

  search_article = request.args.get('article_query')
  if search_article:
    return redirect(url_for('.search',article_name=search_article))
  else:
    return render_template('allstories.html',title=title, name='All Stories',articles = all_stories_articles)


@main.route('/search/<article_name>')
def search(article_name):
  '''
  view function that displays articles search results
  '''
  article_name_list = article_name.split(" ")
  article_name_format = "+".join(article_name_list)
  searched_article = search_article(article_name_format)
  title = f"{article_name}'s search results"

  return render_template('search.html', articles=searched_article)
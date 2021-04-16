import urllib.request,json
from .article_model import Article

#Getting APi Key
api_key = None

#getting base url
base_url = None

def configure_request(app):
  global api_key,base_url
  api_key = app.config['NEWS_API_KEY']
  base_url = app.config['NEWS_API_BASE_URL']

def get_article(category):
  '''
  Gets json response to our url request
  '''
  get_article_url = base_url.format(category,api_key)

  with urllib.request.urlopen(get_article_url) as url:
    get_data = url.read()
    get_data_response = json.loads(get_data)

    news_results = None

    if get_data_response['results']:
      article_result_list = get_data_response['results']
      news_results = process_results(article_result_list)

  return news_results

def process_results(articles_list):
  '''
  Function that transforms results into a list of objects

  Args:
    articles_list:A list that contains a dictionary of news objects

    returns: list of resultant articles
  '''

  news_results = []
  for article_item in articles_list:
    title = article_item.get('title')
    name = article_item.get('name')
    author = article_item.get('author')
    image = article_item.get('urlToImage')
    description = article_item.get('description')
    publishedAt = article_item.get('publishedAt')

    if image:
        article_object = Article(
        name, author, title,url, urlToImage, description, publishedAt)
        news_results.append(article_object)

    return news_results
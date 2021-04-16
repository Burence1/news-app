import urllib.request,json
from .models import Sources,Article

api_key = None
base_url = None
search_url = None
article_url = None
topheadline_url = None
everything_url = None


def configure_request(app):
  global api_key,base_url,search_url,topheadline_url,article_url,everything_url
  api_key = app.config['NEWS_API_KEY']
  base_url = app.config["SOURCE_API_BASE_URL"]
  article_url = app.config["EVERYTHING_SOURCE_BASE_URL"]
  topheadline_url = app.config["TOP_HEADLINES_BASE_URL"]
  everything_url = app.config["EVERYTHING_BASE_URL"]
  search_url = app.config["SEARCH_API_BASE_URL"]

def get_source(category):
  '''
  Gets json response to our url request
  '''
  get_source_url = base_url.format(category,api_key)
  print(get_source_url)

  with urllib.request.urlopen(get_source_url) as url:
    get_source_data = url.read()
    source_data_response = json.loads(get_source_data)

    source_results = None

    if source_data_response['results']:
      source_result_list = source_data_response['results']
      source_results = process_results(source_results_list)

  return source_results

def process_results(source_list):
  '''
  Function that transforms results into a list of objects

  Args:
    articles_list:A list that contains a dictionary of news objects

    returns: list of resultant articles
  '''

  source_results = []
  for source_item in source_list:
    id = source_item.get('id')
    name = source_item.get('name')
    description = source_item.get('description')
    category = source_item.get('category')
    country = source_item.get('country')
    language = source_item.get('language')

    source_object = Sources(id, name, description, category,language,country)
    source_results.append(source_object)

    return source_results

def get_articles(source_id,limit):
  '''
  gets json response to our url request
  '''
  get_articles_url = article_url.format(source_id,limit,api_key)

  with urllib.request.urlopen(get_articles_url) as url:
    get_articles_data = url.read()
    articles_data_response = json.loads(get_articles_data)

    articles_results = None

    if articles_data_response['results']:
      articles_results_list = articles_data_response['results']
      articles_results = process_articles(articles_results_list)

  return articles_results

def process_articles(articles_list):
  '''
  Function that transforms results into a list of objects

  Args:
    articles_list:A list that contains a dictionary of news objects

    returns: list of resultant articles
  '''
  articles_results=[]
  for article in articles_list:
    author = article_item.get('author')
    title = article_item.get('title')
    url = article_item.get('url')
    urlToImage = article_item.get('urlToImage')
    description = article_item.get('description')
    publishedAt = article_item.get('publishedAt')

    if urlToImage:
      articles_object = Article(author,title,url,urlToImage,description,publishedAt)
      articles_results.append(articles_object)

  return articles_results


def get_top_headlines(limit):
  '''
  gets json response to our url request
  '''
  get_top_headlines_url = topheadline_url.format(limit,api_key)

  with urllib.request.urlopen('get_top_headlines_url') as url:
    get_headlines_data = url.read()
    get_headlines_response = json.loads(get_headlines_data)

    headlines_results = None

    if get_headlines_response['results']:
      headlines_results_list = get_headlines_response['results']
      headlines_results = process_results.append(headlines_results_list)

  return headlines_results


def get_all_articles(limit):
  '''
  gets json response to our url request
  '''
  all_articles_url = everything_url.format(limit,api_key)

  with urllib.request.urlopen(all_articles_url) as url:
    all_articles_data = url.read()
    all_articles_response = json.loads(all_articles_data)

    all_articles_results=None

    if all_articles_response['results']:
      all_articles_results_list = all_articles_response['results']
      all_articles_results = process_articles(all_articles_results_list)

  return all_articles_results


def search_article(article_name):
  '''
  gets json response to our url request
  '''
  search_article_url = search_url.format(article_name,api_key)

  with urllib.request.urlopen(search_article_url) as url:
    search_article_data = url.read()
    search_article_response = json.loads(search_article_data)

    search_article_results = None

    if search_article_response['results']:
      search_article_results_list = search_article_response['results']
      search_article_results = process_articles(search_article_results_list)

  return search_article_results
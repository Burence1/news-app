import urllib.request,json
from .models import Sources,Article

#Getting APi Key
api_key = None
base_url = None
search_url = None
top_headlines_url = None
breaking_url = None


def configure_request(app):
  global api_key,base_url,search_url,top_headlines_url,breaking_url
  search_url = app.config['']
  api_key = app.config['NEWS_API_KEY']
  base_url = app.config['NEWS_API_BASE_URL']

def get_source(category):
  '''
  Gets json response to our url request
  '''
  get_source_url = base_url.format(category,api_key)

  with urllib.request.urlopen(get_source_url) as url:
    get_data = url.read()
    get_data_response = json.loads(get_data)

    source_results = None

    if get_data_response['results']:
      source_result_list = get_data_response['results']
      source_results = process_results(source_result_list)

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

    source_object = Sources(id, name, description, category)
    source_results.append(newsource_object)

    return source_results
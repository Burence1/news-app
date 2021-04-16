import os

class Config:

  '''
  General Configurations, parent class
  '''

  NEWS_API_BASE_URL = 'http://newsapi.org/v2/sources?&apiKey={}'
  SEARCH_API_BASE_URL = 'https://newsapi.org/v2/everything?q={}&sortBy=relevancy,publishedAt&pageSize=30&apiKey={}'
  TOP_HEADLINES_BASE_URL = 'http://newsapi.org/v2/top-headlines?sources={}&apiKey={}'
  BREAKING_NEWS_BASE_URL = 'http://newsapi.org/v2/top-headlines?country=us&category=general&apiKey={}'
  NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
  SECRET_KEY = os.environ.get('SECRET_KEY')

class prodConfig(Config):
  '''
  production configuration child class

  Args:
      Config: The parent configuration class with General configuration settings
  '''
  pass


class DevConfig(Config):
  '''
  Development configuration child class

  Args:
      Config: The parent configuration class with General configuration settings
  '''
  DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig
}
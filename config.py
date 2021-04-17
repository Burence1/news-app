import os

class Config:

  '''
  General Configurations, parent class
  '''

  SOURCE_API_URL = 'https://newsapi.org/v2/sources?language=en&category={}&apiKey={}'
  EVERYTHING_SOURCE_URL = 'https://newsapi.org/v2/everything?sources={}&pageSize={}&apiKey={}'
  TOP_STORIES_URL = 'https://newsapi.org/v2/top-headlines?language=en&pageSize={}&apiKey={}'
  EVERYTHING_URL = 'https://newsapi.org/v2/everything?sources=bbc-news,al-jazeera-english,cnn,independent,google-news,the-telegraph,mashable,the-lad-bible,buzzfeed,bloomberg,engadget,espn,fortune&sortBy=publishedAt&pageSize={}&apiKey={}'
  SEARCH_API_URL = 'https://newsapi.org/v2/everything?q={}&language=en&sortBy=popularity&apiKey={}'
  NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
  SECRET_KEY = os.environ.get('SECRET_KEY')

class ProdConfig(Config):
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

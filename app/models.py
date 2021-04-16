class Sources:
  '''
  Sources class that defines class objects
  '''

  def __init__(self,id,name,description,category,language,country):

    self.id = id
    self.name = name
    self.description = description
    self.category = category
    self.language = language
    self.country = country


class Article:
  '''
  Article class that defines class objects
  '''

  def __init__(self, author, title, url, urlToImage, description, publishedAt):

    self.author = author
    self.title = title
    self.url = url
    self.urlToImage = urlToImage
    self.description = description
    self.publishedAt = publishedAt

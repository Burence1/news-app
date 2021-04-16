class Article:
  '''
  Article class that defines class objects
  '''

  def __init__(self,name,author,title,url,urlToImage,description,publishedAt):

    self.name =name
    self.author = author
    self.title = title
    self.url = url
    self.urlToImage = urlToImage 
    self.description = description
    self.publishedAt = publishedAt
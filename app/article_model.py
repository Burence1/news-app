class Article:
  '''
  Article class that defines class objects
  '''

  def __init__(self,name,author,title,urlToImage,description,publishedAt):

    self.name =name
    self.author = author
    self.title = title
    self.urlToImage = urlToImage 
    self.description = description
    self.publishedAt = publishedAt
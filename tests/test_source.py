import unittest
from app.models import Sources 

class SourcesTest(unittest.TestCase):
  '''
  Test Class to test the behaviour of the Article class
  '''
  def setUp(self):
    '''
    Set up method that will run before every Test
    '''

    self.new_source = Sources("abc-news", "ABC News", "https: // abcnews.go.com",
                              "Your trusted source for breaking news, analysis, exclusive interviews, headlines, and videos at ABCNews.com.", "general", "us")

  def test_unit(self):
    '''
    check if bjects have been correctly initiated
    '''

    self.assertEqual(self.new_source.id, "abc-news")
    self.assertEqual(self.new_source.name, "ABC News")
    self.assertEqual(self.new_source.url, "https: // abcnews.go.com")
    self.assertEqual(self.new_source.description,
                     "Your trusted source for breaking news, analysis, exclusive interviews, headlines, and videos at ABCNews.com.")
    self.assertEqual(self.new_source.category, "general")
    self.assertEqual(self.new_source.country, "us")

  def test_instance(self):
    '''
    checking if sources class has been properly instantiated
    '''

    self.assertTrue(isinstance(self.new_source, Sources))
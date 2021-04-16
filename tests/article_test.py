import unittest
from app.models import Article


class ArticleTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Movie class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_article = Article("The Wall Street Journal", "Jonathan Cheng",
                                   "Chinese Economy Grew More Than 18% in First Quarter - The Wall Street Journal",
                                   "https://images.wsj.net/im-325989/social", "<ol><li>Chinese Economy Grew More Than 18% in First Quarter  The Wall Street Journal\r\n</li><li>China says its economy grew 18.3% in the first quarter, slightly missing expectations  CNBC\r\n</li><li>China's economy grows 18.3% in post-Covid comeback  BBC News\r\n…",
                                   "2021-04-16T03:04:00Z")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article, Article))

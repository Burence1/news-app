import unittest
from app.models import Article


class ArticleTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Article class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_article = Article("AP", "India's electric vehicles face practical, technical hurdles", "https: // www.thehindu.com/sci-tech/technology/indias-electric-vehicles-face-practical-technical-hurdles/article34355885.ece",
        "https: // www.thehindu.com/sci-tech/technology/gs0awa/article34356481.ece/ALTERNATES/LANDSCAPE_615/EV-india-Reutersjpg", "EVs are a rarity in India, where more than 300 million vehicles, most of them scooters and three-wheel motorized rickshaws, jam the highways", "2021-04-19T07:35:01Z")

    
    def test_unit(self):
        '''
        check if bjects have been correctly initiated
        '''

        self.assertEqual(self.new_article.author, 'AP')
        self.assertEqual(self.new_article.title,"India's electric vehicles face practical, technical hurdles")
        self.assertEqual(self.new_article.url, 'https: // www.thehindu.com/sci-tech/technology/indias-electric-vehicles-face-practical-technical-hurdles/article34355885.ece')
        self.assertEqual(self.new_article.urlToImage, 'https: // www.thehindu.com/sci-tech/technology/gs0awa/article34356481.ece/ALTERNATES/LANDSCAPE_615/EV-india-Reutersjpg')
        self.assertEqual(self.new_article.description,'EVs are a rarity in India, where more than 300 million vehicles, most of them scooters and three-wheel motorized rickshaws, jam the highways')
        self.assertEqual(self.new_article.publishedAt, '2021-04-19T07:35:01Z')
    
    
    def test_instance(self):
        '''
        checking if article class has been properly instantiated
        '''

        self.assertTrue(isinstance(self.new_article, Article))

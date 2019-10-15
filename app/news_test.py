import unittest
from .models import news
News = news.News

class NewsTest(unittest.TestCase):
    """
    test class to test the behaviour of  the News class
    """

    def setUp(self):
        '''
        set up method that will run before every test
        '''
        self.new_news = News('CNN','CNN News','Cable News Network that is a leader in providing news worldwide','cnn.com','general','en','U.S.A')
        
    def test_instance(self):
        self.assertTrue(isinstance(self.new_news,News))



if __name__ == '__main__': 
    unittest.main()
class Config:
    '''
    General configuration parent class
    '''
    SOURCE_API_BASE_URL = 'https://newsapi.org/v2/sources?apiKey=5084802430fe42a38ffbccfb5ecfdb0b'

    NEWS_API_BASE_URL = 'https://newsapi.org/v2/everything?q=bitcoin&apiKey=5084802430fe42a38ffbccfb5ecfdb0b'

class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True
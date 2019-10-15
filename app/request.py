from app import app
import urllib.request
import json
from .models import news, articles

News = news.News
# Getting api key
api_key = app.config['NEWS_API_KEY']

# getting the news base url
source_base_url = app.config['SOURCE_API_BASE_URL']
news_base_url = app.config['NEWS_API_BASE_URL']


def get_sources():
    '''
    Function that gets the json response to our url request
    '''
    get_sources_url = source_base_url

    with urllib.request.urlopen(get_sources_url)as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        sources_results = None

        if get_sources_response['sources']:
            sources_results_list = get_sources_response['sources']
            sources_results = process_results(sources_results_list)

    return sources_results


def process_results(sources_list):
    '''
    Function that proceses the sources results and transforms them to a list of objects
    Args:
        sources_list: A list of dictionaries that contain Sources details

    Returns:
        sources _results: A list of sources objects
    '''
    sources_results = []
    for source_item in sources_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')
        category = source_item.get('category')
        language = source_item.get('language')
        country = source_item.get('country')

        new_object = News(id, name, description, url,
                          category, language, country)
        sources_results.append(new_object)

    return sources_results


def get_news(id):
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = news_base_url

    with urllib.request.urlopen(get_news_url)as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['articles']:
            news_results_list = get_news_response['articles']
            news_results = process_news_results(news_results_list)

    return news_results


def process_news_results(news_list):
    '''
    Function that proceses the sources results and transforms them to a list of objects
    Args:
        sources_list: A list of dictionaries that contain Sources details

    Returns:
        sources _results: A list of sources objects
    '''
    news_results = []
    for news_results in news_list['articles']:
        news_results.append(
            Articals(
                article.get('id')
                article.get('author'),
                article.get('title'),
                article.get('description'),
                article.get('url'),
                article.get('urlToImage'),
                article.get('publishedAt'),
                article.get('content')
            )
        )


    

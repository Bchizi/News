from app import app
import urllib.request,json
from .models import news

News = news.News
#Getting api key
api_key = app.config['NEWS_API_KEY'] 

#getting the news base url
base_url = app.config['NEWS_API_BASE_URL']

def get_sources():
    '''
    Function that gets the json response to our url request
    '''
    get_sources_url= base_url

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

        new_object=News(id,name,description,url,category,language,country)
        sources_results.append(new_object)

       

    return sources_results 







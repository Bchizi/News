from flask import render_template
from app import app
from .request import get_sources,get_news

# Views
@app.route('/')
def home():

    '''
    View root page function that returns the index page and its data
    '''
    #getting sources
    sources = get_sources()
    print(sources)

    title = 'BestNews'
    return render_template('index.html', title = title ,sources = sources )

@app.route('/news/<id>')
def news(id):
    news = get_news(id)
    print(news)

    title= 'Articles'
    return render_template('news.html',title = title, news=news)



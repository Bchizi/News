from flask import render_template
from app import app
from .request import get_sources

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

@app.route('/News')
def news():
    return render_template('news.html')


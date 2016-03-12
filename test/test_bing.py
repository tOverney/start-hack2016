import json

from api.bing_news import BingNews

keywords = ['EPFL', 'lausanne']
market = 'en-GB'
format = 'json'

json = BingNews().getNews(keywords, market)

print(json)
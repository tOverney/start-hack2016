from api.bing_news import BingNews
from news.search_related_news import SearchRelatedNews
import json

keywords = ['EPFL', 'lausanne']
market = 'en-GB'

listArticle = SearchRelatedNews().get(keywords, market)

print(listArticle)

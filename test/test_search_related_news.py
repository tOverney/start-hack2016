from api.bing_news import BingNews
from news.search_related_news import SearchRelatedNews
import json

keywords = ['champignon', 'moisissure']
market = 'fr-CH'

listArticle = SearchRelatedNews().get(keywords, market)

print(listArticle)

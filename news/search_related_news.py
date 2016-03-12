from api.bing_news import BingNews
from newspaper import Article
import json

class SearchRelatedNews:


	def get(keywords, market) -> List[Article]:
		
		jsonArticles = BingNews().getNews(keywords, market)
		acc = []

		for art in jsonArticles['d']['results']:
			acc.append(Article(art['__metadata']['uri']))
			print(art['__metadata']['Title'])

		return acc
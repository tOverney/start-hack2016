from newspaper import Article
from typing import List

from api.bing_news import BingNews


class SearchRelatedNews:


	def get(self, keywords, market) -> List[Article]:
		
		jsonArticles = BingNews().getNews(keywords, market)
		acc = []

		for art in jsonArticles['d']['results']:
			acc.append(Article(art['__metadata']['uri']))
			print(art['Title'])

		return acc
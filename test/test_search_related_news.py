from news.search_related_news import SearchRelatedNews

keywords = ['champignon', 'moisissure']
market = 'fr-CH'

listArticle = SearchRelatedNews().get(keywords, market)

print(listArticle)

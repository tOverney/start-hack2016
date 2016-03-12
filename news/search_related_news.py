from newspaper import Article
from typing import List

from api.bing_news import BingNews


class SearchRelatedNews:

    def get(self, keywords, market) -> List[Article]:
        jsonArticles = BingNews().getNews(keywords, market)
        acc = []

        for art in jsonArticles['d']['results']:
            tmp = Article(art['Url'])
            if not tmp.url:
                tmp.url = art['Url']
            if not tmp.title:
                print(art)
                tmp.title = art['Title']
            acc.append(tmp)


        return acc

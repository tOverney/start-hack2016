from itertools import islice

from newspaper import Article
from typing import List

from api.bing_news import BingNews


def _get_articles(results):
    for art in results:
        tmp = Article(art['Url'])
        tmp.download()
        tmp.parse()
        if tmp.title.strip():
            yield tmp


class SearchRelatedNews:
    def get(self, keywords, market) -> List[Article]:
        jsonArticles = BingNews().getNews(keywords, market)
        arr = jsonArticles['d']['results']
        return islice(_get_articles(arr), 6)

    def getVideo(self, keywords, market) -> List[Article]:
        jsonArticles = BingNews().getVideo(keywords, market)
        arrr = jsonArticles['d']['results']
        return islice(_get_articles(arr), 6)

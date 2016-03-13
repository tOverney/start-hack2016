from itertools import islice

from newspaper import Article, ArticleException
from typing import List

from api.bing_news import BingNews


def _get_articles(results):
    for art in results:
        try:
            tmp = Article(art['Url'])
            tmp.download()
            tmp.parse()
            if tmp.title.strip():
                yield tmp
        except ArticleException:
            pass

def _get_media_url(results):
    for video in results:
        tmp = video['MediaUrl']
        if "youtube" in tmp:
          yield tmp

class SearchRelatedNews:
    def get(self, keywords, market) -> List[Article]:
        jsonArticles = BingNews().getNews(keywords, market)
        arr = jsonArticles['d']['results']
        return islice(_get_articles(arr), 6)

    def getVideos(self, keywords, market) -> List[str]:
        keywords.append("youtube")
        jsonArticles = BingNews().getVideos(keywords, market)
        arr = jsonArticles['d']['results']
        return list(islice(_get_media_url(arr), 3))

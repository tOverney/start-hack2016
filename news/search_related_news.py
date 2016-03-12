from newspaper import Article
from typing import List

from api.bing_news import BingNews


class SearchRelatedNews:

    def get(self, keywords, market) -> List[Article]:
        jsonArticles = BingNews().getNews(keywords, market)
        acc = []
        arr = jsonArticles['d']['results'][:6]
        for art in arr:
            try:
                tmp = Article(art['Url'])
                tmp.download()
                tmp.parse()
            except:
                continue

            acc.append(tmp)

        return list(filter(lambda x: len(x.title.strip()) != 0, acc))

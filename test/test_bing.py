import json
import unittest

from api.bing_news import BingNews
from news.search_related_news import SearchRelatedNews


class TestBing(unittest.TestCase):
    def test_get_news(self):
        keywords = ['EPFL', 'lausanne']
        market = 'en-GB'

        BingNews().getNews(keywords, market)

    def test_related_news(self):
        keywords = ['champignon', 'moisissure']
        market = 'fr-CH'

        SearchRelatedNews().get(keywords, market)

import unittest

from api import Api
from api.base import ApiError


class ApiTest(unittest.TestCase):
    def setUp(self):
        self.api = Api()

    def test_translate_translate(self):
        ret = self.api.language_translation.translate('Bonjour mon ami')

        self.assertEquals(ret, 'Hello my friend')

    def test_translate_identify(self):
        ret = self.api.language_translation.identify('Hello my friend')

        self.assertEquals(ret, 'en')

    def test_synthesize(self):
        self.api.text_to_speech.synthesize('Hello my friend')

    def test_insight_search(self):
        ret = self.api.text_insight.search("aes")

        self.assertGreaterEqual(len(ret), 1)

    def test_insight_annotate_text(self):
        ret = self.api.text_insight.annotate_text(
            'IBM Watson is a cognitive system enabling a new partnership between people and computers.')

        self.assertGreaterEqual(len(ret), 3)

    def test_insight_concepts(self):
        ret = self.api.text_insight.concepts('IBM')

        self.assertEquals(ret.label, 'IBM')

    def test_insight_concepts_weird_return(self):
        ret = self.api.text_insight.concepts('Ben')

        self.assertEquals(ret.label, 'Ben')

    def test_insight_concepts_not_resuts(self):
        self.assertRaises(ApiError, self.api.text_insight.concepts, '__random_string__')

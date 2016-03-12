import unittest

from api import Api


class ApiTest(unittest.TestCase):
    def setUp(self):
        self.api = Api()

    def test_translate(self):
        ret = self.api.language_translation.translate('Hello my friend')

        self.assertEquals(ret, 'Bonjour mon ami')

    def test_synthesize(self):
        self.api.text_to_speech.synthesize('Hello my friend')

    def test_insight(self):
        ret = self.api.text_insight.search("aes")

        self.assertGreaterEqual(len(ret), 1)

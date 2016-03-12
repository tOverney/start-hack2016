import unittest

from api import Api


class ApiTest(unittest.TestCase):
    def test_translate(self):
        api = Api()

        ret = api.language_translation.translate('Hello my friend')

        self.assertEquals(ret, 'Bonjour mon ami')

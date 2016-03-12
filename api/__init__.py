"""
{
  "language_translation": [
    {
      "name": "Language Translation-ky",
      "label": "language_translation",
      "plan": "standard",
      "credentials": {
        "url": "https://gateway.watsonplatform.net/language-translation/api",
        "password": "omnw37f13fP4",
        "username": "232457f3-ccc4-40ea-8a6e-a9dde96eb22b"
      }
    }
  ]
}
"""
from api.language_translation import LanguageTranslation


class Api:
    def __init__(self):
        username = '232457f3-ccc4-40ea-8a6e-a9dde96eb22b'
        password = 'omnw37f13fP4'

        self.language_translation = LanguageTranslation(username, password)


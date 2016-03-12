from typing import Iterable

from api.base import Base
from textblob import TextBlob


class LanguageTranslation(Base):
    def __init__(self) -> None:
        module = ('gateway', 'language-translation/api/v2')
        username = '232457f3-ccc4-40ea-8a6e-a9dde96eb22b'
        password = 'omnw37f13fP4'
        super().__init__(module=module, username=username, password=password)

    def translate(self, text: str, dest_lang: str = 'en') -> str:
        lang = TextBlob(text).detect_language()

        if lang != 'en' and dest_lang != 'en':
            text = self.atomic_translate(text, lang, 'en')
            lang = 'en';
        if lang != dest_lang:
            return self.atomic_translate(text, lang, dest_lang)
        return text


    def atomic_translate(self, text: str, src: str, dst: str) -> str:
        json = {
            'text': text,
            'source': src,
            'target': dst,
        }
        ans = self._post(path='translate', json=json)

        if(ans.status_code == 200):
            return ans.text.strip()
        return str(TextBlob(text).translate(from_lang=src, to=dst))


    def identify(self, text: str) -> str:
        headers = {'content-type': 'text/plain'}
        ans = self._post(path='identify', data=text, headers=headers)

        return ans.text

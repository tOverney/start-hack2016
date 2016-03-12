from typing import Iterable

from api.base import Base


class LanguageTranslation(Base):
    def __init__(self) -> None:
        module = ('gateway', 'language-translation/api/v2')
        username = '232457f3-ccc4-40ea-8a6e-a9dde96eb22b'
        password = 'omnw37f13fP4'
        super().__init__(module=module, username=username, password=password)

    def translate(self, text: str) -> str:
        json = {
            'text': text,
            'source': self.identify(text),
            'target': 'en',
        }

        ans = self._post(path='translate', json=json)

        return ans.text.strip()

    def identify(self, text: str) -> str:
        headers = {'content-type': 'text/plain'}
        ans = self._post(path='identify', data=text, headers=headers)

        return ans.text

from api.base import Base


class LanguageTranslation(Base):

    def __init__(self, username: str, password: str) -> None:
        super().__init__(module='language-translation/api/v2', username=username, password=password)

    def translate(self, text: str) -> str:
        data = {
            'text': text,
            'source': 'en',
            'target': 'fr',
        }

        ans = self._post(url='translate', data=data)

        return ans.text.strip()

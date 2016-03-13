from typing import Iterable

from api.base import Base


class TextToSpeech(Base):
    def __init__(self) -> None:
        module = ('stream', 'text-to-speech/api/v1')
        username = '69a1b8ae-53b7-44d6-b415-8847a79ba2ff'
        password = 'xvwuA0QDYsrg'
        super().__init__(module=module, username=username, password=password)

    def synthesize(self, text: str) -> Iterable[bytes]:
        path = 'synthesize'
        json = {
            'text': text[:5000],
            'format': 'audio/wav',
        }

        ans = self._post(path=path, json=json)

        return ans.content

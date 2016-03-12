from typing import Iterable

from api.base import Base


class Match:
    def __init__(self, id: str, label: str) -> None:
        self.id = id
        self.label = label

    def __repr__(self):
        return 'Match({id!r}, {label!r})'.format(**self.__dict__)


class TextInsight(Base):
    def __init__(self) -> None:
        module = ('gateway', 'concept-insights/api/v2')
        username = '44601611-a7c8-46f2-9bbb-32fafdff3bb2'
        password = 'eKF8QtHBlj7H'
        super().__init__(module=module, username=username, password=password)

        self.account = "wikipedia"
        self.graph = "en-latest"

    def search(self, search: str) -> Iterable[Match]:
        path = 'graphs/{}/{}/label_search'.format(self.account, self.graph)
        params = {
            'query': search
        }

        ans = self._get(path=path, params=params)

        return {Match(match['id'], match['label']) for match in ans.json()['matches']}

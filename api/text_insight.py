from typing import Iterable

from api.base import Base


class TextInsight(Base):
    def __init__(self) -> None:
        module = ('gateway', 'concept-insights/api/v2')
        username = '44601611-a7c8-46f2-9bbb-32fafdff3bb2'
        password = 'eKF8QtHBlj7H'
        self.account = "wikipedia"
        self.graph = "en-latest"
        super().__init__(module=module, username=username, password=password)

    def search(self, search: str) -> None:
        path = 'graphs/{}/{}/label_search'.format(self.account, self.graph)
        query = { "query": search, "prefix": "false"}
        ans = self._get(path=path, data=query)
        print(ans.text)
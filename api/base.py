import requests
from typing import Any, Mapping, Optional


class Base:
    def __init__(self, module: str, username: str, password: str):
        self.module = module
        self.username = username
        self.password = password

    def __request(self, method: str, path: str, data: Optional[Mapping[str, Any]] = None):
        url = 'https://gateway.watsonplatform.net/{}/{}'.format(self.module, path)
        auth = (self.username, self.password)

        ans = requests.request(method=method, url=url, auth=auth, data=data)

        return ans

    def _post(self, url: str, data: Mapping[str, Any]):
        return self.__request(method='POST', path=url, data=data)

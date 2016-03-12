import requests
from typing import Any, Mapping, Optional, Tuple


class Base:
    def __init__(self, module: Tuple[str, str], username: str, password: str):
        self.module = module
        self.username = username
        self.password = password

    def __request(self, method: str, path: str, json: Optional[Mapping[str, Any]] = None):
        url = 'https://{}.watsonplatform.net/{}/{}'.format(self.module[0], self.module[1], path)
        auth = (self.username, self.password)

        ans = requests.request(method=method, url=url, auth=auth, json=json)

        return ans

    def _post(self, path: str, json: Mapping[str, Any]):
        return self.__request(method='POST', path=path, json=json)

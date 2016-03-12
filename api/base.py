import requests
from typing import Any, Mapping, Optional, Tuple


class Base:
    def __init__(self, module: Tuple[str, str], username: str, password: str):
        self.module = module
        self.username = username
        self.password = password

    def __request(self, method: str, path: str, json: Optional[Mapping[str, Any]] = None,
                  data: Optional[Mapping[str, str]] = None,
                  params: Optional[Mapping[str, str]] = None) -> requests.Response:
        url = 'https://{}.watsonplatform.net/{}/{}'.format(self.module[0], self.module[1], path)
        auth = (self.username, self.password)

        ans = requests.request(method=method, url=url, auth=auth, json=json, data=data, params=params)

        return ans

    def _post(self, path: str, json: Mapping[str, Any]) -> requests.Response:
        return self.__request(method='POST', path=path, json=json)

    def _get(self, path: str, params: Optional[Mapping[str, str]] = None) -> requests.Response:
        return self.__request(method='GET', path=path, params=params)

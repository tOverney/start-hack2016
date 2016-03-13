import requests
from typing import Any, Mapping, Optional, Tuple


class ApiError(Exception):
    def __init__(self, error: str, url: Optional[str] = None, code: Optional[int] = None,
                 code_description: Optional[str] = None) -> None:
        self.code_description = code_description
        self.code = code
        self.error = error
        self.url = url


class Base:
    def __init__(self, module: Tuple[str, str], username: str, password: str):
        self.module = module
        self.username = username
        self.password = password

    def __request(self, method: str, path: str, json: Optional[Mapping[str, Any]] = None,
                  data: Optional[Mapping[str, str]] = None,
                  params: Optional[Mapping[str, str]] = None,
                  headers: Optional[Mapping[str, str]] = None) -> requests.Response:
        url = 'https://{}.watsonplatform.net/{}/{}'.format(self.module[0], self.module[1], path)
        auth = (self.username, self.password)

        ans = requests.request(method=method, url=url, auth=auth, json=json, data=data, params=params, headers=headers)

        if ans.text.startswith('{'):
            ans_json = ans.json()
            if 'error' in ans_json:
                print(ans_json)
                raise ApiError(error=ans.json()['error'])

        return ans

    def _post(self, path: str, data: Optional[str] = None,
              json: Optional[Mapping[str, Any]] = None,
              headers: Optional[Mapping[str, str]] = None) -> requests.Response:
        return self.__request(method='POST', data=data, path=path, headers=headers, json=json)

    def _get(self, path: str, params: Optional[Mapping[str, str]] = None,
             headers: Optional[Mapping[str, str]] = None) -> requests.Response:
        return self.__request(method='GET', path=path, params=params, headers=headers)

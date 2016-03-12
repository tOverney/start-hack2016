import requests
from typing import Any, Mapping, Optional, Tuple


class BingBase:
    def __init__(self, username: str, password: str):
       
        self.username = username
        self.password = password

    def __request(self, method: str, keywords, market, formatRes = None):
        url = "https://api.datamarket.azure.com/Bing/Search/v1/News?Query='{}'&$format={}&Market='{}'".format(' '.join(keywords), formatRes, market)
        auth = (self.username, self.password)

        ans = requests.request(method=method, url=url, auth=auth)

        return ans

    def _post(self, keywords, formatRes, market):
        return self.__request('POST', keywords, market, formatRes)

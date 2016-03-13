from api.bing_base import BingBase


class BingNews(BingBase):
    def __init__(self) -> None:
        username = ''
        password = 'D1ZVa7VSEUxcF7jEhGfv7X1SrcXTxfg4xeERNiflNL8='
        super().__init__(username=username, password=password)

    def getNews(self, keywords, market):
        formatRes = 'json'
        ans = self._post(keywords, formatRes, market, "News")
        return ans.json()

    def getVideos(self, keywords, market):
        formatRes = 'json'
        ans = self._post(keywords, formatRes, market, "Video")
        return ans.json()

import requests

from utils.environment import conf

class User:
  def __init__(self, *, telegramId: str) -> None:
    self._headers = {"Accept": "text/html", "Authorization": f"Bearer {conf.getRemnaAPIkey()}"}
    self._response = requests.get(conf.getRemnaUrl() + f'/api/users/tg/{telegramId}', headers=self._headers)
    self._data = self._response.json()
    self._subscription = requests.get(self._data.get("response")[0].get("subscriptionUrl"), headers=self._headers) if self._response.status_code != 404 else None

  def getExpireAt(self) -> str | None:
    return (self._data.get("response")[0].get("expireAt") if self._response.status_code != 404 else None)

  def getSubscriptionUrl(self) -> str | None:
    return (self._subscription.json().get("subscriptionUrl") if self._subscription != None else None)

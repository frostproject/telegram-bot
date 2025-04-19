import os
from dotenv import load_dotenv, dotenv_values

class config:
  def __init__(self):
    self._config = dotenv_values(".env")
    load_dotenv()

  def getToken(self) -> str:
    return os.getenv("TELEGRAM_TOKEN")

  def getRemnaAPIkey(self) -> str:
    return os.getenv("REMNAWAVE_API_KEY")

  def getRemnaUrl(self) -> str:
    return "https://" + os.getenv("REMNAWAVE_BASE_URL")

conf = config()

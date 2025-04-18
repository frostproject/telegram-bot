import os
import json

current_dir = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(current_dir, '..', 'translations', 'en.json')
json_path = os.path.normpath(json_path)

class TranslationWrapper:
  def __init__(self):
    with open(json_path, 'r', encoding='utf-8') as f:
      self._data = json.load(f)

  def __getattr__(self, name):
    if name.startswith("get") and len(name) > 3:
      key = name[3:].lower()
      return lambda: self._data.get(key)
    raise AttributeError(f"{name} not found")

en = TranslationWrapper()

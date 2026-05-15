# применение динамическиъ атрибутов для обработки данных
import keyword
from collections import Mapping, MutableSequence
from urllib.request import urlopen
import warnings
import os
import json
import datetime

URL = 'https://jsonplaceholder.typicode.com/users'
# JSON = 'users-sample.json'
JSON = 'osconfeed-sample.json'


def load() -> dict:
    file_exist = os.path.exists(JSON)
    file_is_updated = False

    if file_exist:
        modified_timestamp = os.path.getmtime(JSON)
        modified_date = datetime.datetime.fromtimestamp(modified_timestamp)
        today_date = datetime.datetime.today()
        file_is_updated = modified_date == today_date

    if not file_exist or not file_is_updated:
        msg = 'downloading {} to {}'.format(URL, JSON)
        warnings.warn(msg)
        with urlopen(url=URL) as remote, open(JSON, 'wb') as handler:
            handler.write(remote.read())

        with open(JSON) as handler:
            return json.load(handler)
    else:
        msg = 'data is present, skip task'
        warnings.warn(msg)
        return {}


class FrozenJSON:

    def __init__(self, mapping):
        if isinstance(mapping, MutableSequence):
            self.__data = next(iter(mapping))
        else:
            self.__data = dict(mapping)

        for key, value in self.__data.copy().items():
            if keyword.iskeyword(key): # проверка на зарезервированое слово (class...)
                key += '_'
            self.__data[key] = value

    def __getattr__(self, item):
        if hasattr(self.__data, item):
            return getattr(self.__data, item)
        else:
            return FrozenJSON.build(self.__data[item])

    def __len__(self):
        return len(self.__data)

    @classmethod
    def build(cls, item):
        if isinstance(item, Mapping):
            return cls(item)
        elif isinstance(item, MutableSequence):
            return [cls.build(i) for i in item]
        else:
            return item


def main():
    raw_feed = load()
    if raw_feed:
        feed = FrozenJSON(raw_feed)
        print(len(feed))
        pk, name = feed.id, feed.name
        print(pk, name)
        grad = FrozenJSON({'name': 'jim bo', 'class': 1982})
        print(grad.class_)


if __name__ == '__main__':
    main()

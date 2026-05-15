# изменение структуры набора данных с помощью shelve
import shelve
import warnings
import os
import datetime
from urllib.request import urlopen
import json

URL = 'https://raw.githubusercontent.com/fluentpython/example-code/master/19-dyn-attr-prop/oscon/data/osconfeed.json'
# JSON = 'users-sample.json'
JSON = 'osconfeed-sample.json'


def load() -> dict:
    file_exist = os.path.exists(JSON)
    file_is_updated = False

    if file_exist:
        modified_timestamp = os.path.getmtime(JSON)
        modified_date = datetime.datetime.fromtimestamp(modified_timestamp).date()
        today_date = datetime.datetime.today().date()
        file_is_updated = modified_date == today_date

    if not file_exist or not file_is_updated:
        msg = 'downloading {} to {}'.format(URL, JSON)
        warnings.warn(msg)
        with urlopen(url=URL) as remote, open(JSON, 'wb') as handler:
            handler.write(remote.read())
    else:
        msg = 'data is present, skip task'
        warnings.warn(msg)

    with open(JSON) as handler:
        return json.load(handler)


DB_NAME = 'schedule.db'


class Record:

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)


def load_db(db):
    raw_data = load()
    warnings.warn('loading ' + DB_NAME)
    for collection, rec_list in raw_data['Schedule'].items():
        record_type = collection[:-1]
        for record in rec_list:
            key ='{}.{}'.format(record_type, record['serial'])
            record['serial'] = key
            db[key] = Record(**record)


def main():
    db = shelve.open(DB_NAME)
    load_db(db=db)

if __name__ == '__main__':
    main()

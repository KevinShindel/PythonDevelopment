from collections import UserDict
from types import MappingProxyType


class StrKeyDict(UserDict):
    ''' создаёт касмтомный словарь '''

    def __missing__(self, key):
        ''' проверка ключа на тип строка '''
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def __contains__(self, key):
        ''' поиск на вхождение '''
        return str(key) in self.data

    def __setitem__(self, key, value):
        ''' добавляет значение к стровому представлению ключа'''
        self.data[str(key)] = value


def dict_testing():
    d = StrKeyDict()
    d['key'] = 'value'
    d[1] = 'value2'
    print(d)


def mapping_proxy_type():
    d = {1: 'a'}
    d_proxy = MappingProxyType(d)
    d[2] = 'B'
    d_proxy[2] = 'C' # mappingproxy' object does not support item assignment -> словарь защищен от изменений!
    print(d, d_proxy)


def main():
    mapping_proxy_type()

if __name__ == '__main__':
    main()
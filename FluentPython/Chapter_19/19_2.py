# гибкое создание объектов с помощью метода new
import keyword
from collections import MutableSequence, Mapping


class Foo:

    def __init__(self, *args):
        self._args = args


def object_maker(the_class, some_arg):
    new_object = the_class.__new__(some_arg)
    if isinstance(new_object, the_class):
        the_class.__init__(new_object, some_arg)
    return new_object


class FrozenJSON:

    def __new__(cls, *args, **kwargs):
        if isinstance(args, Mapping):
            return super().__new__(cls)
        elif isinstance(args, MutableSequence):
            return [cls(i) for i in args]
        else:
            return args

    def __init__(self, mapping):
        self.__data = {}
        for key, value in mapping.items():
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
    x = Foo('bar')
    print(x)
    x = object_maker(Foo, 'bar')
    print(x)


if __name__ == '__main__':
    main()


# как работает генераторная функция

'''
Определение генераторной функции
 - Любая функция которая возвращает значение
   с помощью слова yield называется генераторной
'''
import re
import reprlib


def get_123(): # функция порождает значения с помощью yield
    yield 1
    yield 2
    yield 3


class Sentence4:
    RE_WORD = re.compile(r'\w+')

    def __init__(self, text):
        self._text = text  # хранить список слов не нужно

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self._text)

    def __iter__(self):
        for match in self.RE_WORD.finditer(self._text):  # строит генератор совпадений
            yield match.group()  # извлекает сопоставленный обьект и возвращает его


class Sentence5:
    RE_WORD = re.compile(r'\w+')

    def __init__(self, text):
        self._text = text  # хранить список слов не нужно

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self._text)

    def __iter__(self):
        yield from [match.group() for match in self.RE_WORD.finditer(self._text)] # создаём генератор


def main():
    print(get_123())
    for i in get_123():
        print(i)

    g = get_123()
    print(next(g))
    print(next(g))
    print(next(g))

    # print(next(g)) # StopIteration

    s = Sentence4('Some words found in 4 here 4 now i try 5555 to check 101=23 myself')
    i = iter(s)
    print(next(i))
    print(next(i))
    print(next(i))
    print(next(i))

    s = Sentence5('Some words found in 4 here 4 now i try 5555 to check 101=23 myself')
    i = iter(s)
    print(next(i))
    print(next(i))
    print(next(i))
    print(next(i))
    print(next(i))
    print(next(i))
    print(next(i))



if __name__ == '__main__':
    main()
import re
import reprlib
from collections.abc import Iterable


class Sentence:
    REWORD = re.compile('\w+')

    def __init__(self, text):

        self._text = text
        self.words = self.REWORD.findall(text) # отдаёт список всех слов

    @property
    def text(self):
        return self._text

    def __getitem__(self, item):
        return self.words[item]

    def __len__(self): # по требованию протокола необходим метод len
        return len(self.words)

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)


class Foo:

    def __iter__(self):  # лучше реализовывать метод __iter__
        pass

class Iterator(Iterable):
    # Итераторы в Python следует считать не типом а протоколом.
    # Многие

    __slots__ = ()

    def __next__(self):
        ''' Возвращает следующий доступный элемент '''
        raise StopIteration

    def __iter__(self):
        ''' Возвращает self. Это позволяет использовать итератор где
        ожидается итерируемый обьект, например в цикле for '''
        return self

    @classmethod
    def __subclasshook__(cls, C):
        if cls is Iterator:
            if (any("__next__" in B.__dict__ for B in C.__mro__)
                and
                any("__iter__" in B.__dict__ for B in C.__mro__)):
                return True
        raise NotImplemented


def test_range():
    yield from range(10)


def main():
    s = Sentence('>>The time has come, >> the Walrus said,')
    print(s)
    for w in s:
        print(w)
    print('++++++++++++++++++++++')


    print(issubclass(Foo, Iterable))
    print(isinstance(Foo(), Iterable))
    print('++++++++++++++++++++++')


    s = 'ABC'
    for it in s:
        print(it)

    it = iter(s)  # альтернативный вариант итерировать обьект
    while True:
        try:
            print(next(it))
        except StopIteration:
            del it
            break
    print('++++++++++++++++++++++')
    s3 = Sentence('Pig and Pepper')
    it = iter(s3)
    print(it)
    print(next(it))
    print(next(it))
    print(next(it))

    print(
        list( # получаем список
            iter( # создаём итератор
                test_range() # используем функцию для получения генератора
            )
        )
    )


class SentenceIterator:

    def __init__(self, words):
        self._words = words
        self.index = 0

    def __next__(self):
        try:
            word = self._words[self.index]
        except IndexError:
            raise StopIteration
        self.index += 1
        return word

    def __iter__(self):
        return self


class Sentence3:

    REWORD = re.compile('\w+')

    def __init__(self, text):

        self._text = text
        self.words = self.REWORD.findall(text)

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self._text)

    def __iter__(self):
        for word in self.words: # обходим self.words
            yield word # отдаём текущее слово
        return None # генераторная функция не возбуждает StopIteration, return показан визуального понимания



if __name__ == '__main__':
    main()

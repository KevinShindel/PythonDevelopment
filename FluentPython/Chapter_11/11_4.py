
# from numbers import \
#    Number,  суперкласс верхнего уровня
#    Complex,  промежуточный класс
#    Real,   число с плавающей точкой
#    Rational,
#    Integral целые числа

'''
Для проверки является ли число целым нужно вызвать
isinstance(x, Integral)
Для проверки на число с плавающей точкой
isinstance(x, Real)
'''

# Опеределение и использование ABC
import abc
import random
from typing import Iterable

'''
Что бы оправдать создание абстрактного базового класса
нужен контекст для использования его в качестве точки расширения  
'''


class Tombola(abc.ABC):

    @abc.abstractmethod
    def load(self, iterable):
        ''' добавить элементы из итерируемого обьекта '''

    @abc.abstractmethod
    def pick(self):
        ''' извлечь случайный элемент и вернуть его
        иначе возбудить LookupError '''

    def loaded(self):
        ''' вернуть True если есть хотя бы 1 элемент, иначе False '''
        return bool(self.inspect())

    def inspect(self): # у абстрактного метода может быть реализация но она обязана быть переопределена или вызвана методом super()
        ''' Вернуть осортированный кортеж содержащий
        находящиеся в контейнере элементы '''
        items = []
        while True:
            try:
                items.append(self.pick())
            except LookupError:
                break
        self.load(items)
        return tuple(sorted(items))


class BingoCage(Tombola):  # наследование класса Tombola

    def __init__(self, items):
        self.__randomizer = random.SystemRandom()  # реализует случайный выбор
        self._items = []
        self.load(items)  # загрука данных

    def load(self, iterable):
        self._items.extend(iterable)
        self.__randomizer.shuffle(self._items)  # перетасовываем список

    def pick(self):  # реализация метода базового класса
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty BingoCage')

    def __call__(self, *args, **kwargs):  # реализация метода вызова
        self.pick() # его нет в базовом классе, но никакого вреда он не принесёт


class LotteryBlower(Tombola):

    def __init__(self, iterable: Iterable):
        self._balls = list(iterable) # строим список конвертируя через list

    def load(self, iterable):
        self._balls.extend(iterable) # расширение списка

    def pick(self):
        try:
            position = random.randrange(len(self._balls)) # ищем позицию в списке
        except ValueError:
            raise LookupError('pick from empty BingoCage')
        return self._balls.pop(position) # по индексу отдаем значение

    def loaded(self):  # override метода loaded
        return bool(self._balls)

    def inspect(self):  # override метода inspect
        return tuple(sorted(self._balls))


def main():
    b = BingoCage(range(100))
    p = b.pick()
    print(p)


if __name__ == '__main__':
    main()

from abc import ABC, abstractmethod, ABCMeta
from random import randrange


class Tombola(ABC):

    @abstractmethod
    def load(self, iterable):
        ''' добавить элементы из итерируемого обьекта '''

    @abstractmethod
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


@Tombola.register #
class TomboList(list):

    def pick(self):
        if self:
            position = randrange(len(self))
            return self.pop(position)
        else:
            raise LookupError('pop from empty TomboList')

    load = list.extend

    def loaded(self):
        return bool(self)

    def inspect(self):
        return tuple(sorted(self))

# Tombola.register(TomboList) # методя для регистрации Python <= 3.3


class Sized(metaclass=ABCMeta):
    __slots__ = ()

    @abstractmethod
    def __len__(self):
        return 0

    @classmethod
    def __subclasscheck__(cls, subclass):
        if cls is Sized:
            if any("__len__" in B.__dict__ for B in subclass.__mro__): # если в словаре любого класса существует аттрибут __len__
                return True # возвращаем True
            else:
                return NotImplemented # иначе возвращаем NotImplemented что бы продолжить проверку


def main():
    t = TomboList(range(100))
    p = t.pick()
    print(p)
    i = issubclass(TomboList, Tombola)
    print(i)


if __name__ == '__main__':
    main()

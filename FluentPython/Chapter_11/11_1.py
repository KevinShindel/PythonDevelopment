# интерфейсы и протоколы в культуре Python
from collections import abc


class Vector2D:
    typecode = 'd'

    def __init__(self, x, y):
        self.__x = float(x)
        self.__y = float(y)

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def __iter__(self):
        return (i for i in (self.x, self.y))


class Foo:
    ''' для реализации итерируемого обьекта досточно обьявить метод getitem '''

    def __getitem__(self, item):
        return range(0, 30, 10)[item]


class Struggle:
    '''
    для реализации подкаласа не обязательно наследоватся от базового класса
    досточно реализовать его методы
    '''

    def __len__(self):
        return 23


def main():
    f = Foo()
    print(f[1])
    for i in f:
        print(i)
    print(isinstance(Struggle(), abc.Sized)) # проверка на тип


if __name__ == '__main__':
    main()

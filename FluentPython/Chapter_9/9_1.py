# представления обьекта

# repr() -> вернуть строку представляющий обьект удобный для виде для разработчика
# str() -> вернуть строку представляющий обьект удобный для виде для пользователя

'''
__repr__, __str__, __format__ -> должны возвращать строки
__bytes__ -> должны возвращать последовательность байтов
'''
import math
from array import array


class Vector2d:
    typecode = 'd'  # атрибут класса для последовательности байтов

    @classmethod  # применяется как альтернативный коснтруктор
    def frombytes(cls, octets):
        typecode = chr(octets[0])  # читаем первый символ для typecode
        memv = memoryview(octets[1:]).cast(typecode)  # создаем memoryview для двоичной последовательности
        return cls(*memv)

    def __init__(self, x: [float or int], y: [float or int]):
        self.x = float(x)  # преобразование защищает от неподходящих аргументов
        self.y = float(y)

    def __iter__(self):
        return (i for i in (self.x, self.y))  # наличие метода делает класс итерируемым

    def __repr__(self):
        class_name = type(self).__name__
        return '{} ({!r}, {!r})'.format(class_name, *self)  # метод строит строку представления, итерируя конструктор

    def __str__(self):
        return str(tuple(self))  # отображение в видде упорядоченой пары

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) +  # преобразуем typecode в bytes и конкатенируем
                bytes(array(self.typecode, self)))

    def __eq__(self, other):
        return tuple(self) == tuple(other)  # метод снравнения

    def __abs__(self):
        return math.hypot(self.x, self.y)  # преобразуем в абсолютное значение и любое число отличное от нуля
                                          # вернет True

    def __bool__(self):
        return bool(abs(self))


def main():
    v1 = Vector2d(3, 4)
    print(v1.x, v1.y)
    x,y = v1
    print(x, y)
    print(v1.__repr__())
    print(v1)
    v1_clone = eval(repr(v1))
    print(v1 == v1_clone)
    print(v1)
    octets = bytes(v1)
    print(octets)
    print(abs(v1))
    print(bool(v1), bool(Vector2d(0, 0)))
    print('++++++++++++++++++++++')
    v2 = Vector2d.frombytes(b'd\x00\x00\x00\x00\x00\x00\x08@\x00\x00\x00\x00\x00\x00\x10@')
    print(v2)

if __name__ == '__main__':
    main()

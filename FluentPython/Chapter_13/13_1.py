# перегрузка операторов
# - оператор __neg__
# + оператор __pos__
# ~ оператор инверсии __invert__
import itertools
import math
import numbers
import reprlib


class Vector:

    def __init__(self, components):
        self._components = list(components)

    def __iter__(self):
        return iter(self._components)

    def __repr__(self):
        components = reprlib.repr(self._components)
        components = components[components.find('['):-1]
        return 'Vector({})'.format(components)

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return (bytes(ord(self)) + bytes(self._components))

    def __add__(self, other):
        pairs = itertools.zip_longest(self._components, other._components, fillvalue=0)
        return Vector(map(sum, pairs))

    def __radd__(self, other):
        self + other

    def __abs__(self):  # расчитываем абсолютное значение
        return math.sqrt(sum(x*x for x in self)) # возвродим в степень и вычисляем корень

    def __neg__(self):
        return Vector(-x for x in self) # возвращаем все отрицательные значения

    def __pos__(self):
        return Vector(self) # возвращаем инстанс

    def __mul__(self, other):
        if isinstance(other, numbers.Real):
            return Vector(other * n for n in self)
        else:
            return NotImplemented

    def __rmul__(self, other):
        return self * other



def main():
    v1 = Vector(range(10))
    v2 = Vector([10,20,30])
    res = v1 + v2
    print(res)
    r = v1 * 1
    print(r)
    r = 2 * v1
    print(r)



if __name__ == '__main__':
    main()

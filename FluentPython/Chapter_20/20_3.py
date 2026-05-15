# усовершенствование дескриптора
import abc


class AutoStorage: # предоставляет большую часть логики ...
    ''' дескрипторный класс который автоматически управляет атрибутами '''
    __counter = 0

    def __init__(self):
        cls = self.__class__
        prefix = cls.__name__
        index = cls.__counter
        self.storage_name = '_{}#{}'.format(prefix, index)
        cls.__counter += 1

    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            return getattr(instance, self.storage_name)

    def __set__(self, instance, value):
        setattr(instance, self.storage_name, value)  # ... за исключением проверки


class Validated(abc.ABC, AutoStorage): # абстрактный но наследует AutoStorage
    ''' класс управления методом __set__ '''

    def __set__(self, instance, value):
        value = self.validate(instance, value) # переопределяет метод set и делегирует методу validate
        super().__set__(instance, value) # и выполняет метод super

    @abc.abstractmethod
    def validate(self, instance, value):
        ''' возвразает провереное значение или возбуждает ValueError'''


class Quantity(Validated):
    ''' число больше нуля '''

    def validate(self, instance, value):
        if value <= 0:
            raise ValueError('Value must be > 0')
        else:
            return value


class NonBlank(Validated):
    ''' строка содержит хотя бы один непробельный симсвол '''

    def validate(self, instance, value):
        value = value.strip()
        if len(value) == 0:
            raise ValueError('value cannot be empty or blank')
        else:
            return value


class LineItem:
    description = NonBlank()
    price = Quantity()
    weight = Quantity()

    def __init__(self, description, price, weight):
        self.description = description
        self.price = price
        self.weight = weight

    def subtotal(self):
        return self.weight * self.price


def main():
    i = LineItem('item', 15.95, 3.5)
    total = i.subtotal()
    print(total)


if __name__ == '__main__':
    main()

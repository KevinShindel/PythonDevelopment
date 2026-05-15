# дескрипторы атрибутов

class Quantity:  # дескриптор основан на протоколе, поэтому доплнительное наследование не требуется

    def __init__(self, storage_name):
        self.storage_name = storage_name  # в каждом экземляре имеется поле для хранения значения

    def __set__(self, instance, value): # метод set вызывается при любой попытке присвоить значение
        if value > 0:
            instance.__dict__[self.storage_name] = value  # необходимо работать с атрибутом __dict__
        else:
            raise ValueError('Value must be > 0')


class LineItem:

    weight = Quantity('weight')  # первый экземпляр дексриптора
    price = Quantity('price')  # второй экземляр дескриптора

    def __init__(self, description, weight, price): # конструктор класса
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price

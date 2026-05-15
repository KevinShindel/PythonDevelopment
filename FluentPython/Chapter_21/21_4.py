# специальный метод prepare
import collections

from Chapter_20 import model


class EntityMeta(type):

    @classmethod
    def __prepare__(cls, name, bases):
        return collections.OrderedDict() # возвращаем пустой экземляр в кором будут хранится атрибуты класса

    def __init__(cls, name, bases, attr_dict):
        super().__init__(name, bases, attr_dict)
        cls._field_names = [] # создаём атрибут в конструкторе класса
        for key, attr in attr_dict.items(): # attr_dict <-- экземрял класса OrderedDict
            if isinstance(attr, model.Validated):
                type_name = type(attr).__name__
                attr.storage_name = '_{}#{}'.format(type_name, key)
                cls._field_names.append(key) # помещаем поля


class Entity(metaclass=EntityMeta):

    @classmethod
    def field_names(cls):  # метод класса просто отдаёт все поля
        yield from cls._field_names


class LineItem(Entity):
    description = model.NonBlank()
    weight = model.Quantity()
    price = model.Quantity()

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price


def main():
    for name in LineItem.field_names():
        print(name)


if __name__ == '__main__':
    main()

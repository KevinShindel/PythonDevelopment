# метакласс Entity
from Chapter_20 import model


class EntityMeta(type):

    def __init__(cls, name, bases, attr_dict):
        super().__init__(name, bases, attr_dict)
        for key, attr in cls.__dict__.items():
            if isinstance(attr, model.Validated):
                type_name = type(attr).__name__
                attr.storage_name = '_{}#{}'.format(type_name, key)


class LineItem(metaclass=EntityMeta):
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
    l = LineItem(description='Some desc', weight=30, price=10)
    total = l.subtotal()
    print(total)

if __name__ == '__main__':
    main()

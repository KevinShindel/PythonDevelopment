# программирование фабрики свойств

def quantity(storage_name):

    def qty_getter(instance):
        return instance.__dict__[storage_name]

    def qty_setter(instance, value):
        if value:
            instance.__dict__[storage_name] = value
        else:
            raise ValueError('value must be > 0')

    return property(qty_getter, qty_setter)


class LineItem:

    weight = quantity('weight') # используем фабрику для определения свойства класса
    price = quantity('price')

    def __init__(self, desc, weight, price):
        self.desc = desc
        self.weight = weight # здесь свойство уже работает
        self.price = price

    def subtotal(self):
        return self.weight * self.price


def main():
    l = LineItem('some stuff', 0, 0)
    print(l)

if __name__ == '__main__':
    main()



# автоматическая генерация имен атрибутов хранения


class Quantity:
    __counter = 0 # атрибут класса для посчёта экземляпров класса

    def __init__(self):
        cls = self.__class__  # ссылка на класс
        prefix = cls.__name__ # имя класса
        index = cls.__counter
        self.storage_name = '_{}#{}'.format(prefix, index) # генерация уникального идентификатора
        cls.__counter += 1  # инкрементация счётчика

    def __get__(self, instance, owner):
        if instance is None:
            return self #
        else:
            return getattr(instance, self.storage_name)

    def __set__(self, instance, value):
        if value > 0:
            setattr(instance, self.storage_name, value) # установка значения
        else:
            raise ValueError('value must be > 0')


class LineItem:
    weight = Quantity()
    price = Quantity()

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price


def main():
    l = LineItem('item', 10, 2)
    print(l.subtotal())

if __name__ == '__main__':
    main()

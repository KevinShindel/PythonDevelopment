# использование свойств для контроля атрибутов

class LineItem:
    def __init__(self, desc, weight, price):
        self.desc = desc
        self.weight = weight  # метод установки с гарантией что значение будет больше 0
        self.price = price

    def subtotal(self):
        return self.weight * self.price

    @property  # декоратором указывается метод для чтения
    def weight(self):  # имя атрибута реализующего свойство совпадает с иминем открытого атрибута
        return self.__weight  # фактическое значение будет хранится в закрытом атрибуте

    @weight.setter  # декоратор для установки значения
    def weight(self, value):
        if value > 0:
            self.__weight = value # если значение больше нуля присваиваем его закрытому атрибуту
        else:
            raise ValueError('Value must be > 0') # иначе созбуждаем исключение


def main():
    raisins = LineItem('Golden raisins', 10, 6.95)
    total = raisins.subtotal()
    print(total)

    raisins = LineItem('Golden raisins', -10, 6.95)
    total = raisins.subtotal()
    print(total)




if __name__ == '__main__':
    main()

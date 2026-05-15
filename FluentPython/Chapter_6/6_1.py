# паттерн стратения
from abc import ABC, abstractmethod
from collections import namedtuple

"""
Паттерн Стратегия:
Определить семейство алгоритком, инкапсулировать каждый
из них и сделать их взаимозаменяемыми. Стратегия позволяет заменять
алгоритм независимо от использующих его клиентов.
"""

Customer = namedtuple('Customer', 'name fidelity')


class LineItem:

    def __init__(self, product: str, quantity: int, price: float):
        self.product = product
        self.quantity = quantity
        self.price = price

    def total(self):
        return self.price * self.quantity


class Promotion(ABC):
    '''
    Стратегия
    Интерфейс обищй для всех компонентов реализующих разнчыне алгоритмы.
    '''

    @abstractmethod
    def discount(self, order):
        """ вернуть скидку в виде положительной сумы в долларах """


class Order:
    '''
    Контекст
    Предоставляет службу делегируя часть вычислений взаимозаменяемым компонентам реализующим различные алгоритмы
    '''

    def __init__(self, customer: Customer, cart: [LineItem], promotion: Promotion = None):
        self.customer = customer
        self.cart = cart
        self.promotion = promotion

    def total(self):
        if not hasattr(self, '__total'):
            self.__total = sum(item.total() for item in self.cart)
        return self.__total

    def due(self):
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion.discount(self)
        return self.__total - discount

    def __repr__(self):
        fmt = '<Order total: {:.2f} due: {:.2f} discount: {:.2f}>'
        return fmt.format(self.total(), self.due(), self.total() - self.due())


class FidelityPromo(Promotion):
    """
    Конкретная стратегия
    5-% скидка для заказчиков, имеющих не менее 1000 балов лояльности
    """

    def discount(self, order):
        return order.total() * 0.05 if order.customer.fidelity >= 1000 else 0


class BulkItemPromo(Promotion):
    """
    Конкретная стратегия
    10-% скидка для каджой позиции ListItem в которой заказано не менее 20 единиц
    """

    def discount(self, order):
        discount = 0
        for item in order.cart:
            if item.quantity >= 20:
                discount += item.total() * 0.1
        return discount


class LargeOrderPromo(Promotion):
    '''
    Конкретная стратегия
    7-ми % скидка для заказчиков, включащих не менее 10 различных позиций
    '''

    def discount(self, order):
        distinct_items = {item.product for item in order.cart}
        if len(distinct_items) >= 10:
            return order.total() * 0.07
        else:
            return 0


def main():
    joe = Customer('John Doe', 0)
    ann = Customer('Anna Smith', 1100)
    cart = [LineItem('banana', 4, 0.5), LineItem('apple', 10, 1.5), LineItem('watermelon', 5, 5)]
    discount = Order(joe, cart, FidelityPromo())
    print(discount)
    discount = Order(ann, cart, FidelityPromo())
    print(discount)
    banana_cart = [LineItem('banana', 30, 0.5), LineItem('apple', 10, 1.5)]
    discount = Order(joe, banana_cart, BulkItemPromo())
    print(discount)


if __name__ == '__main__':
    main()



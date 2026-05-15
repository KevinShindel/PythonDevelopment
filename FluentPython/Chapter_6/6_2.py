# функционально-ориентированая стратегия
from collections import namedtuple

Customer = namedtuple('Customer', 'name fidelity')


class LineItem:

    def __init__(self, product: str, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price

    def total(self):
        return self.price * self.quantity

class Order:
    '''
    Контекст
    Предоставляет службу делегируя часть вычислений взаимозаменяемым компонентам реализующим различные алгоритмы
    '''

    def __init__(self, customer: Customer, cart: [LineItem], promotion=None):
        self.customer = customer
        self.cart = list(cart)
        self.promotion = promotion

    def total(self):
        if not hasattr(self, '__total'):
            self.__total = sum(item.total() for item in self.cart)
        return self.__total

    def due(self):
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion(self)
        return self.total() - discount

    def __repr__(self):
        fmt = '<Order total: {:.2f} due: {:.2f} discount: {:.2f}>'
        return fmt.format(self.total(), self.due(), self.total() - self.due())


def fidelity_promo(order: Order):
    return order.total() * 0.5 if order.customer.fidelity >= 1000 else 0


def bulk_item_promo(order: Order):
    discount = 0
    for item in order.cart:
        if item.quantity >= 20:
             discount += item.total() * 0.1
    return discount


def large_order_promo(order):
    distinct_items = {item.product for item in order.cart}
    if len(distinct_items) >= 10:
        return order.total() * 0.07
    return 0


# promos = [fidelity_promo, bulk_item_promo, large_order_promo]  # выбор лучшей стратегии
# globals() -> вызывает словарь глобальных символов, 
promos = [globals()[name] for name in globals() if name.endswith('_promo') and name != 'best_promo'] # поиск доступных стратегий


def best_promo(order):
    ''' выбрать максимально возможную скидку '''
    return max(promo(order) for promo in promos)


def main():
    joe = Customer('John Doe', 0)
    ann = Customer('Anna Smith', 1100)
    cart = [LineItem('banana', 4, 0.5), LineItem('apple', 10, 1.5), LineItem('watermelon', 5, 5)]
    banana_cart = [LineItem('banana', 30, 0.5), LineItem('apple', 10, 1.5)]

    discount = Order(joe, cart, fidelity_promo)
    print(discount)
    discount = Order(ann, banana_cart, large_order_promo)
    print(discount)

    discount = Order(ann, banana_cart, best_promo)
    print(discount)





if __name__ == '__main__':
    main()

# Паттерн стратегия дополненый декоратором

promos = [] # Вначале список пуст


def promotion(promo_func):  # декоратор добавляет функции в общий список
    promos.append(promo_func)
    return promo_func


@promotion
def fidelity(order):
    return order.total() * 0.05 if order.customer.fidelity >= 1000 else 0


@promotion
def bulk_item(order):
    discount = 0
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * 0.1
    return discount


@promotion
def large_order_promo(order):
    distinct_items = {item.product for item in order.cart}
    if len(distinct_items) >= 10:
        return order.total() * 0.07
    return 0


def best_promo(order):  # на момент вызова список с функциями уже будет готов
    return max(promo(order) for promo in promos)


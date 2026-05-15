from collections import defaultdict, OrderedDict, Counter


def dictionary_creating():
    ''' методы создания словарей '''
    a = dict(one=1, two=2, three=3)
    b = {'one': 1, 'two': 2, 'three': 3}
    c = dict(zip(['one', 'two', 'three'], [1,2,3]))
    d = dict([('one', 1), ('two', 2), ('three', 3)])
    e = dict({'one': 1, 'two': 2, 'three': 3})
    print(a == b == c == d == e)


def dict_inclusion():
    ''' словарное включение '''
    DIAL_CODES = [
        (86, 'CHINA'),
        (91, 'INDIA'),
        (1, 'USA'),
        (880, 'BANGLADESH'),
    ]
    country_code = {country: code for code, country in DIAL_CODES}
    print(country_code)
    country_code.clear()
    print(country_code)

def set_default():
    ''' пример работы метода setdefault '''
    market = {
        "sku10666": [1,2,3,4],
        "sku666": [4,5,6,7],
        "sku999": [8,9,0]
    }
    # car.setdefault(key, value)
    # аналогично
    # if 'sku333' not in car:
    #     car['sku333'] = [1]
    x = market.setdefault("sku333", []).append(1)
    print(x, market)

    dd = defaultdict(list) # создает словарь , вместо KeyError будет создан ключ и пустой список
    dd.update({
        "sku10666": [1,2,3,4],
        "sku666": [4,5,6,7],
        "sku999": [8,9,0]
    })
    print(dd)

    od = OrderedDict({ # хранит ключи в порядке их вставки
        "sku10666": [1,2,3,4],
        "sku666": [4,5,6,7],
        "sku999": [8,9,0]
    })
    print(market, od)


def counter_using():
    data = Counter(list('aannvasda')) # считает колво совпадений
    print(data.most_common())
    data = Counter({'a': 10, 'b': 20, 'c': 99, 'e': 4})
    print(data.most_common(4))  # выведет топ 4 самых больших даных






if __name__ == '__main__':
    # dictionary_creating()
    # dict_inclusion()
    # set_default()
    counter_using()

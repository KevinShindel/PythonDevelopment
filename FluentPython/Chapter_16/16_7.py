import collections
import itertools


Result = collections.namedtuple('Result', 'count average')


def averager():
    ''' субгенератор '''
    total, count, average = 0, 0, None
    while True:
        term = yield
        if term is None:
            break  # когда встречается None цикл прерывается и возвращается результат
        total += term
        count += 1
        average = total/count
    return Result(count, average)  # когда цикл закончится (значение term будет равно None) генератор вернёт результат


def grouper(results, key):
    ''' делегирующий генератор '''
    while True:
        results[key] = yield from averager()


def report(results: {str: Result}):
    ''' функция для отображения результатов '''
    for key, value in sorted(results.items()):  # сортирует ключ и значения
        group, unit = key.split(';')  # разбивает ключ на две части
        print('{:2} {:5} average {:.2f}{}'.format(  # форматирование строки
            value.count, group, value.average, unit
        ))


def frange(start, stop, step):
    ''' генератор цифр с плавающей точкой '''
    return itertools.takewhile(lambda x: x < stop, itertools.count(start, step))  # создаёт генератор float


data = {
    'girls;kg': frange(start=30, stop=40, step=0.5),
    'girls;m': frange(start=1.4, stop=1.7, step=0.01),
    'boys;kg': frange(start=50, stop=60, step=0.5),
    'boys;m': frange(start=1.7, stop=2, step=0.01),
}


def main_logic(data: dict):
    ''' клиентский код или вызывающая сторона '''
    results = {}  # результирующий словарь
    for keys, values in data.items():  # итерируем ключ и значение
        group = grouper(results, key=keys)  # групируем данные делигирующим генератором
        next(group)  # инициируем генератор
        for value in values:  # итерируем значения словаря
            group.send(value)  # отправляем данные сопрограмме
        group.send(None)  # останавливаем цикл while True
    print(results)  # вывести содержимое словаря
    report(results)  # детальная информация о данных


def main():
    main_logic(data)


if __name__ == '__main__':
    main()

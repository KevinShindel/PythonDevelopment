import bisect
import random
from array import array
from collections import namedtuple, deque
from string import ascii_lowercase
from sys import getsizeof
from time import perf_counter


def main():
    ''' фильтрация символов '''
    symbols = ascii_lowercase
    beyond = [ord(i) for i in symbols if ord(i) > 110]
    print(beyond)


def decart_mul():
    ''' декартово произведение '''
    colors = ['black', 'white']
    sizes = ['S', 'M', 'L']
    tshirts = [(color, size) for color in colors for size in sizes]
    print(tshirts)


def named_tuple():
    ''' делаем именованый кортеж '''
    City = namedtuple('City', 'name country population coordinates')
    tokyo = City('Tokyo', 'JP', '36.933', (35.689722, 139.691664))
    print(tokyo.name)
    print(tokyo.population)
    print(tokyo.coordinates)
    print(tokyo[0])
    print(City._fields)
    print(tokyo._asdict())


def sorted_list():
    fruits = ['grape', 'raspberry', 'apple', 'banana', 'lime']
    print(sorted(fruits)) # сортировка в алфавитном порядке
    print(sorted(fruits, key=len)) # сортировка по длинне строки
    print(sorted(fruits, key=str.lower, reverse=True)) # сортировка в алфавитном порядке задом на перед


def grade(score, breakpoints=[60, 70, 80, 90], grades='FDCBA'):
    i = bisect.bisect(breakpoints, score)
    return grades[i]


def calculate_grade():
    ''' конверсия цифр в буквы оценок '''
    result = [grade(score) for score in [33, 99, 77, 89, 90, 100]]
    print(result)


def insort_example():
    ''' вставляет элементы и одновременно сортирует '''
    my_list = []
    for i in range(7):
        new_item = random.randrange(7*2)
        bisect.insort(my_list, new_item)
        print(f'{new_item} -> {my_list}')


def list_vs_array_compersation():
    floats = array('d', (random.random() for _ in range(10**7))) # массив из милиона чисел
    floats2 = [random.random() for _ in range(10**7)] # список из милиона чисел
    floats_bytes = getsizeof(floats) # посчитать обьем памяти массива
    floats_bytes2 = getsizeof(floats2) # посчитать обьем памяти списка

    print(floats_bytes)
    print(floats_bytes2)

    floats_size_mb = getsizeof(floats) / 1024 / 1024
    floats_size2_mb = getsizeof(floats2) / 1024 / 1024

    print(floats_size_mb, 'Mb')
    print(floats_size2_mb, 'Mb')

    print(floats_size2_mb / floats_size_mb)


def deque_principal():
    # dq = deque(range(10), maxlen=10)
    # print(dq)
    # dq.rotate(3)  # цикличный сдвиг вправо на 3 ячейки
    # print(dq)
    # dq.rotate(-4)  # цикличный сдвиг влево на 4 ячейки
    # print(dq)
    # dq.extend([11, 22, 33]) # добавить справа 3 ячейки
    # print(dq)
    # dq.extendleft([10, 20, 30]) # добавить слева 3 ячейки
    # print(dq)



    start = perf_counter() # засекаем начало операции
    dq = deque(range(10 ** 6))  # создать список 1 миллион
    dq = [dq.append(random.random()) for _ in range(10**6)] # в цикле добавляем еще миллион
    end = perf_counter()
    total = round(end - start, 2)
    print(f'done at {total} seconds')


    start = perf_counter() # засекаем начало операции
    def_list = [random.random() for _ in range(10 ** 6)]  # создать список 1 миллион
    def_list = [def_list.append(random.random()) for _ in range(10**6)] # в цикле добавляем еще миллион
    end = perf_counter()
    total = round(end - start, 2)
    print(f'done at {total} seconds')




if __name__ == '__main__':
    # main()
    # decart_mul()
    # named_tuple()
    # sorted_list()
    # calculate_grade()
    # insort_example()
    # list_vs_array_compersation()
    deque_principal()

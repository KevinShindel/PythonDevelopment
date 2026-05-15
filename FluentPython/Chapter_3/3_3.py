# теория множеств
import random
import time
from dis import dis


def set_example():
    l = ['span'] * 3 + ['egges']
    print(l)
    s = set(l)
    print(s)
    # set building example
    a = {1,1,2,2,3,3,4}
    b = set([1,2,3,4,4,5,6])
    a.add(6)
    print(a, b)
    c = frozenset({1,1,2,2,3,3,4,4,5,6,7,8})
    print(c)

    print(c)


def productivity_example():
    ''' сравнение производительности вхождений списков и сетов '''
    found = 0
    r = [random.randint(a=0, b=100) for _ in range(100)]
    l = [random.randint(a=0, b=100) for _ in range(10**6)]
    s = set(l)

    start = time.perf_counter()
    for i in l:
        if i in r:
            found += 1
    end = time.perf_counter()
    print('done at ', round(end-start, 3), ' seconds')

    start = time.perf_counter()
    found = len(s.intersection(set(r)))
    end = time.perf_counter()
    print('done at ', round(end-start, 3), ' seconds')


def set_constructor_vs():
    ''' сравнение скорости работы конструктора '''
    r = dis('{1,2,3}') # работает быстрее, 4 шага
    r2 = dis('set([1,2,3])') # работает медленее 6 шагов
    print(r)
    print(r2)

    #   1           0 BUILD_SET                0
    #               2 LOAD_CONST               0 (frozenset({1, 2, 3}))
    #               4 SET_UPDATE               1
    #               6 RETURN_VALUE

    #   1           0 LOAD_NAME                0 (set)
    #               2 BUILD_LIST               0
    #               4 LOAD_CONST               0 ((1, 2, 3))
    #               6 LIST_EXTEND              1
    #               8 CALL_FUNCTION            1
    #              10 RETURN_VALUE


def set_comphersation():
    ''' множественное включение '''
    s = {i for i in range(100)}


if __name__ == '__main__':
    # set_example()
    # productivity_example()
    set_constructor_vs()

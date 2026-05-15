# yield from объяснение и примеры
import functools
import operator


def chain(*iterable): # сцепляющий генератор
    for it in iterable:
        for i in it:
            yield i


def chain2(*iterable): # сцепляющий генератор с реализацией yield from
    for it in iterable:
        yield from it


def main():
    sample1 = 'ABC'
    sample2 = range(3)
    rez = list(chain(sample1, sample2))
    print(rez)
    rez = list(chain2(sample1, sample2))
    print(rez)

# функции редуцирования итерируемого обьекта
# all/any/max/min/reduce/sum


def main2():
    r = all([1,2,3])
    r2 = all([1,0,1])
    r3 = all([])
    print('all', r,r2,r3)

    a = any([1,2,3])
    a2 = any([1,0,0])
    a3 = any([0,0,0])
    print('any', a,a2,a3)

    m = max([1,9,6,99])
    print('max', m)
    m2 = min([9,1,0,3])
    print('min', m2)
    r = functools.reduce(operator.mul, range(1, 6))
    print('reduce', r)
    s = sum([1,2,3,4,5])
    print('sum', s)


if __name__ == '__main__':
    main()
    main2()

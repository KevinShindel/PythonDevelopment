# построение арифметической прогрессии используя itertools
import itertools
import operator
from random import shuffle


def aritprog_gen(begin, step, end=None):
    ''' реализация с помощью itertools '''
    first = type(begin+step)(begin)
    ap_gen = itertools.count(first, step)
    if end is not None:
        ap_gen = itertools.takewhile(lambda n: n > end, ap_gen)
    return ap_gen


def vowel(c: str) -> bool:
    return c.lower() in 'aeiou'


def main():
    gen = itertools.takewhile(lambda n: n < 3,  # фунция останавливается по условию
                              itertools.count(1, .5))  # функция бесконечно генерирует данные
    print(list(gen)) # [1, 1.5, 2.0, 2.5]

    r = list(filter(vowel, 'Aardvark'))  #
    print(r)  # ['A', 'a', 'a']

    r = list(itertools.filterfalse(vowel, 'Aardvark'))  # принимает похожее на ложь значение
    print(r)  # ['r', 'd', 'v', 'r', 'k']

    r = list(itertools.dropwhile(vowel, 'Aardvark'))  #
    print(r)  # ['r', 'd', 'v', 'a', 'r', 'k']

    r = list(itertools.takewhile(vowel, 'Aardvark')) # отдаёт элементы пока принимает похожее на истину значение, затем останавливается
    print(r) # ['A', 'a']

    r = list(itertools.compress('Aardvark', (1, 0, 11, 10, 1))) #
    print(r)  # ['A', 'r', 'd', 'v']

    r = list(itertools.islice('Aardvark', 4))  # отдаёт все элементы со среза, операция ленивая
    print(r) # ['A', 'a', 'r', 'd']

    r = list(itertools.islice('Aardvark', 4, 7)) #   # отдаёт все элементы со среза, операция ленивая
    print(r) # ['v', 'a', 'r']

    sample = [9, 0, 1, 3, 5, 10, 1, 4, 1]
    rez = list(itertools.accumulate(sample)) # аккумулирует все значения
    print(rez) # [0, 1, 3, 6, 10, 15, 21, 28, 36, 45]
    rez = list(itertools.accumulate(sample, min)) # выбирает минималльное значение
    print(rez)  # [2, 2, 2, 2, 2, 0, 0, 0, 0, 0]
    rez = list(itertools.accumulate(sample, max)) # выбирает максимальное значение
    print(rez)  # [5, 8, 8, 8, 8, 8, 8, 8, 8, 9]

    rez = list(enumerate('albatroz', 1)) # отдаёт кортеж с нумерацией
    print(rez)
    rez = list(map(operator.mul, range(11), range(11)))  # выполняет функцию к каждому элементу
    print(rez)
    rez = list(map(operator.mul, range(11), [2,4,8]))  # выполняет функцию к каждому элементу
    print(rez) #

    rez = list(itertools.starmap(operator.mul, enumerate('albatroz', 1)))  #
    print(rez) # ['a', 'll', 'bbb', 'aaaa', 'ttttt', 'rrrrrr', 'ooooooo', 'zzzzzzzz']

    rez = list(itertools.chain(range(5), range(4))) # связывает последовательности
    print(rez)
    rez = list(itertools.chain.from_iterable(enumerate('ACAB'))) #
    print(rez)

    rez = list(itertools.product(range(10), range(10), range(10))) # декартово произведение (комбинаторика)
    # print(rez)

    rez = list(zip(range(10), sorted(range(10), reverse=True))) # связывает итерируемые элементы в кортежи
    print(rez)

    rez = list(itertools.zip_longest(range(5), range(10), fillvalue=0)) # связывает неравнодлинные итерируемые списки
    print(rez)

    rez = list(itertools.product(range(10), repeat=3)) # 000 - 999
    print(rez)
    # count/cycle/repeat
    ct = itertools.count()
    print(next(ct))
    cy = itertools.cycle('ABC')
    print(list(itertools.islice(cy, 7)))
    rpt, *args = itertools.repeat(8, 4)
    print(rpt, *args)

    # groupby/reversed/tee
    sample = 'KYKKAHABHBLLYYAYAYY'
    gb = itertools.groupby(sorted(sample))
    for char, group in gb:
        print(char, '-->', list(group))

    animals = ['duck', 'dolphin', 'cat', 'bear', 'shark', 'lion', 'tiger', 'elephant']
    gb = itertools.groupby(sorted(animals, key=len), len)
    for char, group in gb:
        print(char, '-->', list(group))

    g1, g2, g3 = itertools.tee('ABC', 3)  # породить 3 потока для итерации
    print(next(g1), next(g2), next(g3))




if __name__ == '__main__':
    main()

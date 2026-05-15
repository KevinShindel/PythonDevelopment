# пакеты для функционального программирования
from functools import reduce
from operator import mul, methodcaller


def fact(n):
    # return reduce(lambda a,b: a*b, range(1, n+1))
    return reduce(mul, range(1, n+1)) # метод mul аналогичени лямбда функции


def method_caller_example():
    ''' функция вызывает метод по имени для обьекта '''
    s = 'The time is now'
    upcase = methodcaller('upper')
    print(upcase(s))
    hiphetade = methodcaller('replace', ' ', '-')
    print(hiphetade(s))


if __name__ == '__main__':
    method_caller_example()
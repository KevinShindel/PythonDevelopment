# создание декоратора с помощью wraps
from functools import wraps
from time import perf_counter


def clock(func):
    @wraps(func)  # реализует правильно именованные параментры и копирует основные атррибуты функции
    def clocked(*args, **kwargs):
        start = perf_counter()
        result = func(*args, **kwargs)
        end = perf_counter() - start
        name = func.__name__
        arg_lst = []
        if args:
            arg_lst.append(''.join(repr(arg) for arg in args))
        if kwargs:
            pairs = [{k, '=', w} for k, w in kwargs.items()]
            arg_lst.append(pairs)
        arg_str = ', '.join(arg_lst)
        print('[%0.8fs] %s(%s) -> %r ' % (end, name, arg_str, result))
        return result

    return clocked


@clock
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n-2) + fibonacci(n-1)


def main():
    fibonacci(6)


if __name__ == '__main__':
    main()

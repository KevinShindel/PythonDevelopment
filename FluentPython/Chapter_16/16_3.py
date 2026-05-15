# декоратор для инициации сопрограмм
import functools
import inspect


def coroutine(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        gen = fn(*args, **kwargs) # выполняем генератор
        next(gen)  # инициация генератор
        return gen  # возвращаем его
    return wrapper


@coroutine
def gen_example():
    x = None # инициируем переменную
    value = yield x # ожидаем получения данных
    print(value)


def main():
    cor = gen_example()
    resp = inspect.getgeneratorstate(cor)
    print(resp)
    cor.send(10)

if __name__ == '__main__':
    main()



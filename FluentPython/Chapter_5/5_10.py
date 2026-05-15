# фиксация аргументов с помощью functools.partial

from operator import mul
from functools import partial
from unicodedata import normalize

def partial_test():
    ''' ползволяет вызвать функцию с двумя аргументами там где требуется вызываемый обьект с одним '''
    triple = partial(mul, 3) # создаём частичный вызов функции и фиксируем аргумент
    res = triple(7) # вызываем функцию со вторым аргументом
    print(res)

    nfc = partial(normalize, 'NFC') # фиксируем первым аргументом NFC
    res = nfc('açaí') # вызываем метод только со вторым аргументом
    print(res)


if __name__ == '__main__':
    partial_test()
# Декораторы и замыкания

# @decorate
# def target():
#     print('running target')
#
# def target():
#     print('running target')
#     target = decorate(target)


def deco(fn):  # передача декорируемой функции как аргумента
    def inner(*args, **kwargs):  # # передача дополнительных параметров для внутриней функции
        print('running inner')  # производит доплднительные операции
        fn(*args, **kwargs)  # выполняет декорируемую функцию
    return inner  # возвращает внутренний обьект-функцию inner


@deco
def target():
    print('running target')


def main():
    target()


if __name__ == '__main__':
    main()

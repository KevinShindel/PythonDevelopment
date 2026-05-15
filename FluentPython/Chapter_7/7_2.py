# этапы выполнения декораторов

registry = []


def register(fn):
    print('running register {%s}' % fn)
    registry.append(fn)
    return fn


@register
def f1():
    print('running f1()')

@register
def f2():
    print('running f2()')

def f3():
    print('running f3()')

def main():
    '''
    running register {<function f1 at 0x7f519b4b70d0>} # Декораторы выполняются сразу после обьявления
    running register {<function f2 at 0x7f519b4d1ee0>}
    running main # потом выполняется основная функция
    running f1() # и декорируемые
    running f2()
    running f3() # эта функция не декорирована
    '''
    print('running main')
    f1()
    f2()
    f3()


if __name__ == '__main__':
    main()


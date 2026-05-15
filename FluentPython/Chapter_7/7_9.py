# параметризованые декораторы

registry = set() # указываем тип set для ускорения добавления\удаления функций


def register(active=True): # функция принимает не обязательный именованый аргумент
    def wrapper(fn):
        print('running register(active=%s) -> decorate(%s)' % (active, fn))
        if active:
            registry.add(fn) # регистрируем функцию если только True
        else:
            registry.discard(fn) # иначе удаляем
        return fn
    return wrapper


@register(active=False)
def f1():
    print('running f1()')


@register(active=True)
def f2():
    print('running f2()')


def main():
    print('running main()')
    print('registry -> ', registry)
    f1()
    f2()


if __name__ == '__main__':
    main()
